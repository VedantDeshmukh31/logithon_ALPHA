from flask import Flask, render_template, request, redirect, url_for
import requests
import json
import folium
import os
from Place_to_Coordinate import *
from math import radians, sin, cos, sqrt, atan2

app = Flask(__name__)


def get_sea_route(start_coords, end_coords, api_key):
    # API call to get sea route data
    url = f"https://api.searoutes.com/route/v2/sea/{start_coords[1]},{start_coords[0]};{end_coords[1]},{end_coords[0]}?"
    headers = {
        "accept": "application/json",
        "x-api-key": api_key
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        sea_route_data = response.text
        return sea_route_data
    else:
        print("Error fetching sea route data:", response.text)
        return None


def get_sea_route1(start_coords, end_coords, api_key,):
    # API call to get sea route data
    dict={1:11112, 2:11117, 3:11135}
    url = f"https://api.searoutes.com/route/v2/sea/{start_coords[1]},{start_coords[0]};{end_coords[1]},{end_coords[0]}?blockAreas=11117"
    headers = {
        "accept": "application/json",
        "x-api-key": api_key
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        sea_route_data = response.text
        return sea_route_data
    else:
        print("Error fetching sea route data:", response.text)
        return None


def extract_coordinates_from_json(json_response):
    data = json.loads(json_response)
    coordinates = []
    for feature in data["features"]:
        if feature["geometry"]["type"] == "LineString":
            coordinates.extend(feature["geometry"]["coordinates"])
    return coordinates


def reverse_tuples(arr):
    return [(t[1], t[0]) for t in arr]


def create_map_with_route(coordinates):
    coordinates = reverse_tuples(coordinates)
    mymap = folium.Map(location=coordinates[0], zoom_start=4)
    folium.PolyLine(locations=coordinates, color='blue', weight=5).add_to(mymap)
    mymap.save("static/map_with_route.html")


def calculate_distance(coordinates):
    total_distance = 0
    for i in range(len(coordinates) - 1):
        lat1, lon1 = coordinates[i]
        lat2, lon2 = coordinates[i + 1]
        radius = 6371  # Earth radius in kilometers
        dlat = radians(lat2 - lat1)
        dlon = radians(lon2 - lon1)
        a = sin(dlat / 2) * sin(dlat / 2) + cos(radians(lat1)) * \
            cos(radians(lat2)) * sin(dlon / 2) * sin(dlon / 2)
        c = 2 * atan2(sqrt(a), sqrt(1 - a))
        distance = radius * c
        total_distance += distance
    return total_distance


def calculate_time(distance, average_speed):
    time_hours = distance / average_speed
    time_days = time_hours / 24  # Convert hours to days
    return time_days


def calculate_co2_emissions(distance):
    co2_emissions = distance * 2.3  # Assuming a CO2 emission rate of 2.3 kg per km for maritime transport
    return co2_emissions


def calculate_cost(width, height, weight):
    volume = width * height * weight
    cost_per_cubic_meter = 1000  # Example cost per cubic meter
    cargo_cost = volume * cost_per_cubic_meter * 0.000005
    fuel_surcharge = cargo_cost * 0.0005  # Assuming a fuel surcharge of 5% of cargo cost
    total_cost = cargo_cost + fuel_surcharge
    return cargo_cost, fuel_surcharge, total_cost


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        start_point = request.form.get("start_point")
        end_point = request.form.get("end_point")
        width = float(request.form.get("width"))
        height = float(request.form.get("height"))
        weight = float(request.form.get("weight"))
        start_coords = place_call(start_point)
        end_coords = place_call(end_point)

        api_key = "winO7z9rEZ4iaIt1VaX2i9sHNI8lXvZI9f0tnFRz"
        sea_route_data = get_sea_route(start_coords, end_coords, api_key)
        extracted_sea_route_data = extract_coordinates_from_json(sea_route_data)
        extracted_sea_route_data = [tuple(sublist) for sublist in extracted_sea_route_data]
        create_map_with_route(extracted_sea_route_data)

        # Calculate distance, time, CO2 emissions, and cost
        distance = calculate_distance(extracted_sea_route_data)
        average_speed = 25  # Average speed in knots (nautical miles per hour)
        time_days = calculate_time(distance, average_speed)
        co2_emissions = calculate_co2_emissions(distance)
        cargo_cost, fuel_surcharge, total_cost = calculate_cost(width, height, weight)

        return render_template("index.html", distance=distance, time=time_days, co2_emissions=co2_emissions,
                               cargo_cost=cargo_cost, fuel_surcharge=fuel_surcharge, total_cost=total_cost)
    else:
        return render_template("index.html")


@app.route("/refactor", methods=["GET"])
def refactor():
    start_point = request.form.get("start_point")
    end_point = request.form.get("end_point")
    width = float(request.form.get("width"))
    height = float(request.form.get("height"))
    weight = float(request.form.get("weight"))
    start_coords = place_call(start_point)
    end_coords = place_call(end_point)

    if start_coords is None or end_coords is None:
        # Handle the case where coordinates couldn't be obtained
        return "Error: Could not obtain coordinates for start or end point."

    api_key = "winO7z9rEZ4iaIt1VaX2i9sHNI8lXvZI9f0tnFRz"
    sea_route_data = get_sea_route1(start_coords, end_coords, api_key)
    extracted_sea_route_data = extract_coordinates_from_json(sea_route_data)
    extracted_sea_route_data = [tuple(sublist) for sublist in extracted_sea_route_data]
    create_map_with_route(extracted_sea_route_data)

    # Calculate distance, time, CO2 emissions, and cost
    distance = calculate_distance(extracted_sea_route_data)
    average_speed = 25  # Average speed in knots (nautical miles per hour)
    time_days = calculate_time(distance, average_speed)
    co2_emissions = calculate_co2_emissions(distance)
    cargo_cost, fuel_surcharge, total_cost = calculate_cost(width, height, weight)

    return render_template("index.html", distance=distance, time=time_days, co2_emissions=co2_emissions,
                           cargo_cost=cargo_cost, fuel_surcharge=fuel_surcharge, total_cost=total_cost)

if __name__ == "__main__":
    app.run(debug=True)
