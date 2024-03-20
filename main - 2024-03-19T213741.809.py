
import requests
import json
from datetime import datetime

def get_florists_in_area(api_key, location, radius=5000, keyword='florist'):
    endpoint = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json'
    params = {
        'key': api_key,
        'location': location,
        'radius': radius,
        'keyword': keyword
    }
    response = requests.get(endpoint, params=params)
    if response.status_code == 200:
        data = json.loads(response.text)
        if 'results' in data:
            return data['results']
    return None

def inquire_florists_about_tossed_flowers(florists):
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    for florist in florists:
        print(f"Inquiring at {florist['name']} ({florist['vicinity']})...")
        # Here you can implement code to contact the florist, such as sending an email or making a phone call
        # For demonstration purposes, we'll just print a message
        print(f"Hello, we are interested in any flowers that are being discarded. Can you please let us know when they are available for pickup? Current time: {current_time}\n")

# API key for Google Places API (replace with your own key)
api_key = 'YOUR_GOOGLE_PLACES_API_KEY'

# Location coordinates (latitude, longitude)
location = '37.7749,-122.4194'  # Example location (San Francisco, CA)

# Get florists in the specified area
florists = get_florists_in_area(api_key, location)
if florists:
    print(f"Found {len(florists)} florists in the area.")
    inquire_florists_about_tossed_flowers(florists)
else:
    print("No florists found in the specified area.")
