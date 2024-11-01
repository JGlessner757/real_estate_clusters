
# Real Estate Clustering Analysis with Foursquare Data

This project analyzes real estate values in Hampton Roads using K-Means clustering to identify neighborhoods based on proximity to attractions. The analysis uses data from Foursquare's API to pull information on nearby venues and attractions, allowing for a spatial clustering of neighborhoods.

## Project Overview

This analysis aims to:
1. Cluster neighborhoods based on real estate data and the density of nearby attractions.
2. Visualize clusters on an interactive map to understand neighborhood characteristics.
3. Provide insights into how attraction proximity correlates with neighborhood clustering.

## Data Sources

- **Real Estate Data**: A CSV file with latitude, longitude, and neighborhood names for properties in Hampton Roads.
- **Foursquare API**: Used to pull data on nearby venues and attractions for each neighborhood.

## Methodology

### 1. Data Preparation
   - Load the neighborhood data, including coordinates and names, from a CSV file.
   - Use geolocation services to center the map on Virginia Beach.

### 2. Data Collection with Foursquare API
   - Configure and authenticate API access using the Foursquare API.
   - For each neighborhood, query Foursquare to retrieve nearby venues within a 1km radius.
   - Process and store the returned venue data for each neighborhood.

### 3. Clustering Analysis
   - Perform K-Means clustering on neighborhood data, factoring in the number and types of nearby venues.
   - Assign a unique color to each cluster to enhance visualization clarity.

### 4. Visualization
   - Use Folium to create an interactive map of Hampton Roads.
   - Plot each neighborhood as a circle marker, color-coded by its cluster label.

## Installation

To run this notebook, install the necessary libraries:

```bash
pip install numpy pandas requests folium scikit-learn geopy
```

## Usage

1. **Run the Notebook**: Execute each cell in sequence to pull, process, and visualize the data.
2. **Explore the Map**: The output map displays clustered neighborhoods. Click on each marker for additional details.
3. **Adjust Clustering**: Modify the number of clusters in the K-Means algorithm to experiment with different groupings.

## Key Findings

- Neighborhoods are grouped based on proximity to popular attractions.
- Clustering reveals insights into real estate value patterns and potential correlations with nearby amenities.

## Dependencies

- Python 3.x
- Libraries: `numpy`, `pandas`, `requests`, `folium`, `scikit-learn`, `geopy`

## License

This project is licensed under the MIT License.
