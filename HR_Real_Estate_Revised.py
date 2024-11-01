
# Required Libraries
import numpy as np
import pandas as pd
import requests
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.colors as colors
from sklearn.cluster import KMeans
from geopy.geocoders import Nominatim
import folium

# Initialize and verify all dependencies
print('All systems go...')

# Function to load neighborhood data from a CSV file
def load_data(file_path):
    """Load neighborhood data from a specified CSV file."""
    return pd.read_csv(file_path)

# Function to get geographical coordinates of a location
def get_coordinates(address, user_agent="geo_explorer"):
    """Get latitude and longitude for a given address."""
    geolocator = Nominatim(user_agent=user_agent)
    location = geolocator.geocode(address)
    return location.latitude, location.longitude

# Function to initialize a Folium map
def initialize_map(latitude, longitude, zoom=11, tiles="OpenStreetMap"):
    """Create and return a folium map centered at specified coordinates."""
    map_vb = folium.Map(
        location=[latitude, longitude],
        zoom_start=zoom,
        tiles=tiles,
        attr='Map tiles by Stamen Design, CC BY 3.0 — Map data © OpenStreetMap'
    )
    return map_vb

# Function to add cluster markers to the map
def add_cluster_markers(map_obj, data, kclusters):
    """Add color-coded cluster markers to a folium map."""
    # Color scheme for clusters
    colors_array = cm.rainbow(np.linspace(0, 1, kclusters))
    rainbow = [colors.rgb2hex(i) for i in colors_array]
    
    # Add circle markers for each neighborhood in the data
    for lat, lon, poi, cluster in zip(data['Lat'], data['Long'], data['Neighborhood'], data['Cluster Labels']):
        if not np.isnan(cluster):  # Skip NaN cluster labels
            label = folium.Popup(f"{poi} Cluster {int(cluster)}", parse_html=True)
            folium.CircleMarker(
                [lat, lon],
                radius=3,
                popup=label,
                color=rainbow[int(cluster) - 1],
                fill=True,
                fill_color=rainbow[int(cluster) - 1],
                fill_opacity=0.5
            ).add_to(map_obj)
    return map_obj



# Main execution
if __name__ == "__main__":
    # Load neighborhood data
    vbhoods_path = 'ML\HRDF.csv'  # Update with your actual file path
    vbhoods = load_data(vbhoods_path)
    
    # Obtain coordinates for the central location (Virginia Beach)
    address = '310 Edwin Dr, Virginia Beach, VA 23462'
    latitude, longitude = get_coordinates(address)
    print(f'The geographical coordinates of Virginia Beach, VA are {latitude}, {longitude}.')

    # Initialize the map centered around Virginia Beach
    map_vb = initialize_map(latitude, longitude)
    
    # Clustering parameters and adding markers
    kclusters = 5  # Define number of clusters
    vbhoods['Cluster Labels'] = KMeans(n_clusters=kclusters).fit_predict(vbhoods[['Lat', 'Long']])
    
    # Add the cluster markers to the map
    map_vb = add_cluster_markers(map_vb, vbhoods, kclusters)
    
    # Display the map
    map_vb  # This will show the map in a Jupyter Notebook

    # Display the map by saving it to an HTML file and opening it
import webbrowser

def display_map(map_vb, filename='map_output.html'):
    """Save the map as an HTML file and open it in a web browser."""
    map_vb.save(filename)
    webbrowser.open(filename)

# Example usage after creating the map
display_map(map_vb)

