from flask import Flask, render_template, request
import folium
from geopy.distance import geodesic
from Place_to_Coordinate import *

app = Flask(__name__)

# Constants for cost and fuel consumption
COST_PER_NAUTICAL_MILE = 2  # Cost per nautical mile in dollars
FUEL_CONSUMPTION_PER_NAUTICAL_MILE = (
    0.1  # Fuel consumption per nautical mile in gallons
)
AVERAGE_SPEED = 1000  # Average speed in knots (nautical miles per hour) - Replace this with the actual value


def create_sea_route_map(start_point, destination, map_filename):
    # Calculate the distance between the two points (in nautical miles)
    distance = geodesic(start_point, destination).nautical

    # Calculate cost, time, and fuel consumption
    cost = distance * COST_PER_NAUTICAL_MILE
    time = distance / AVERAGE_SPEED
    fuel_consumption = distance * FUEL_CONSUMPTION_PER_NAUTICAL_MILE

    # Create a map centered around the starting point
    map_route = folium.Map(location=start_point, zoom_start=4)

    # Add markers for the starting point and destination
    folium.Marker(location=start_point, popup="Start Point").add_to(map_route)
    folium.Marker(location=destination, popup="Destination").add_to(map_route)

    # Draw a line between the starting point and destination to represent the sea route
    folium.PolyLine(
        [start_point, destination], color="blue", weight=2.5, opacity=1
    ).add_to(map_route)

    # Save the map to an HTML file in the static folder
    map_route.save(map_filename)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        start_location = request.form["start_location"]
        destination_location = request.form["destination_location"]
        start_point = place_call(start_location)
        destination = place_call(destination_location)
        width = float(request.form["width"])
        height = float(request.form["height"])
        weight = float(request.form["weight"])
        map_filename = "static/flight_route_map.html"
        create_sea_route_map(start_point, destination, map_filename)
        print("Map created successfully.")

        # Calculate distance, cost, time, and fuel consumption again for display
        distance = geodesic(start_point, destination).nautical
        cost = distance * COST_PER_NAUTICAL_MILE
        time = distance / AVERAGE_SPEED
        fuel_consumption = distance * FUEL_CONSUMPTION_PER_NAUTICAL_MILE

        # Additional cost based on width, height, and weight of cargo
        additional_cost = (
            width * height * weight * 0.01
        )  # Adjust the factor according to your pricing model

        # Total cost including additional cost
        total_cost = cost + additional_cost

        return render_template(
            "index.html",
            map_filename=map_filename,
            cost=total_cost,
            time=time,
            fuel_consumption=fuel_consumption,
        )
    return render_template("index.html", map_filename=None)


if __name__ == "__main__":
    app.run(debug=True, port=8080)
