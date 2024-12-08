from pyproj import Transformer

def convert_utm_to_latlong(x, y):
    transformer = Transformer.from_crs("EPSG:32748", "EPSG:4326", always_xy=True)
    longs, lats = transformer.transform(x, y)
    return lats, longs

def extract_coordinates(geojson):
    # Get coordinates from first feature (assuming single polygon)
    coordinates = geojson['features'][0]['geometry']['coordinates'][0][0]
    
    # Create lists for lat/long
    longitudes = []
    latitudes = []
    
    # Extract coordinates
    for coord in coordinates:
        # coord[0] is longitude, coord[1] is latitude (x,y format in UTM)
        longitudes.append(coord[0])
        latitudes.append(coord[1])
    
    return latitudes, longitudes