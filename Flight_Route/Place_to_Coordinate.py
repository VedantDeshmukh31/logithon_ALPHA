from opencage.geocoder import OpenCageGeocode

# Define your OpenCage Geocoding API key


# Initialize the geocoder


# Function to convert place name to coordinates
def place_to_coordinates(place_name,api_key):
    geocoder = OpenCageGeocode(api_key)
    # Perform forward geocoding to get coordinates
    result = geocoder.geocode(place_name)

    if result and len(result):
        # Extract latitude and longitude from the result
        latitude = result[0]['geometry']['lat']
        longitude = result[0]['geometry']['lng']
        return latitude, longitude
    else:
        return None

def place_call(place_name):
  
  api_key = '2a7477dc01e84533a125087859217a39'
  coordinates = place_to_coordinates(place_name,api_key)
  
  if coordinates:
      return coordinates
  else:
      print(f"No coordinates found for {place_name}")

