import streamlit as st
import requests
from PIL import Image
from io import BytesIO
import folium
from streamlit_folium import folium_static

API_KEY = 'AIzaSyBuj-NL2uCSDKfvH9lhrU-b4MfQGT4FNKs'

# Function to fetch store info
def fetch_store_details(place_id):
    """ Fetch detailed information for a store using its place ID """
    url = "https://maps.googleapis.com/maps/api/place/details/json"
    params = {
        'place_id': place_id,
        'fields': 'formatted_phone_number,rating,opening_hours',
        'key': API_KEY
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json().get('result', {})
    return {}

# Function to fetch store locations and return their place IDs from Google Maps API
def fetch_store_place_ids(query):
    url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
    params = {
        'query': query,
        'key': API_KEY
    }
    response = requests.get(url, params=params)
    results = response.json().get('results', [])
    return results[:8]  # Get only the top 6 results for display

# Function to fetch photos for each store based on their place IDs
def fetch_photos_for_stores(place_ids):
    all_photos = []
    for place_id in place_ids:
        detail_url = "https://maps.googleapis.com/maps/api/place/details/json"
        detail_params = {
            'place_id': place_id,
            'fields': 'photos',
            'key': API_KEY
        }
        response = requests.get(detail_url, params=detail_params)
        result = response.json().get('result', {})
        photo_references = [photo['photo_reference'] for photo in result.get('photos', [])[:2]]  
        photos = [fetch_store_photo(photo_reference) for photo_reference in photo_references]
        all_photos.append(photos)  # Store a list of photos for each store
    return all_photos

def fetch_store_photo(photo_reference):
    url = "https://maps.googleapis.com/maps/api/place/photo"
    params = {
        'photoreference': photo_reference,
        'maxheight': 400,
        'key': API_KEY
    }
    response = requests.get(url, params=params, stream=True)
    if response.status_code == 200:
        image = Image.open(BytesIO(response.content))
        return image
    else:
        return None

# Function to display a map with markers for each location
def display_map(locations):
    if not locations:
        return None
    start_loc = [locations[0]['geometry']['location']['lat'], locations[0]['geometry']['location']['lng']]
    map_obj = folium.Map(location=start_loc, zoom_start=12)
    for location in locations:
        folium.Marker(
            location=[location['geometry']['location']['lat'], location['geometry']['location']['lng']],
            popup=location['name']
        ).add_to(map_obj)
    return map_obj

# Streamlit UI
def main():
    st.title("Milk Tea Store Locator")
    st.write("Discover your favorite milk tea spots now!")

    examples = ["Milk tea store near Los Angeles", "Chatime near 90012", "珍珠奶茶店 - Boba Tea Store"]
    st.write("Try searching for...")
    for example in examples:
        st.write(f"- {example}")

    query = st.text_input("Enter here", key="query_input")

    if st.button("Search"):
        locations = fetch_store_place_ids(query)  # Fetch store place IDs from Google Maps API
        if locations:
            photos = fetch_photos_for_stores([location['place_id'] for location in locations])
            map_obj = display_map(locations)
            if map_obj:
                folium_static(map_obj)
            for idx, location in enumerate(locations):
                details = fetch_store_details(location['place_id'])  # Assume this function is defined to fetch additional details
                with st.expander(location['name']):
                    st.write(f"**Address:** {location['formatted_address']}")
                    phone = details.get('formatted_phone_number', 'No phone number available')
                    rating = details.get('rating', 'No rating available')
                    opening_hours = details.get('opening_hours', {}).get('weekday_text', 'Opening hours not available')
                    
                    st.write(f"**Phone:** {phone}")
                    st.write(f"**Rating:** {rating}")
                    if isinstance(opening_hours, list):
                        st.write("**Opening Hours:**")
                        for day in opening_hours:
                            st.write(day)
                    else:
                        st.write(f"**Opening Hours:** {opening_hours}")

                    if photos[idx]:
                        cols = st.columns(len(photos[idx]))
                        for col, photo in zip(cols, photos[idx]):
                            col.image(photo, use_column_width=True)
        else:
            st.write("No store locations found. Please try a different query.")

if __name__ == "__main__":
    main()