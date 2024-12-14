import pandas as pd
import numpy as np

def generate_geojson_and_dataframe(precipitation_data, date, offset=0.025):
    features = []
    lats = []
    longs = []
    precips = []
    locs = []
    
    precipitation_selected = precipitation_data.sel(time=date)

    latitude_values = precipitation_selected.latitude.values
    longitude_values = precipitation_selected.longitude.values

    for lat in latitude_values:
        for lon in longitude_values:
            precip_value = precipitation_selected.sel(latitude=lat, longitude=lon).values.item()
            if not np.isnan(precip_value):

                square_coords = [
                    [lon - offset, lat - offset],
                    [lon + offset, lat - offset],
                    [lon + offset, lat + offset],
                    [lon - offset, lat + offset],
                    [lon - offset, lat - offset],
                ]

                feature = {
                    "type": "Feature",
                    "geometry": {"type": "Polygon", "coordinates": [square_coords]},
                    "properties": {"id": f"{lat:.2f}, {lon:.2f}"},
                }

                features.append(feature)
                lats.append(lat)
                longs.append(lon)
                precips.append(precip_value)
                locs.append(f"{lat:.2f}, {lon:.2f}")
    
    geojson = {"type": "FeatureCollection", "features": features}
    
    data = pd.DataFrame(
        {
            "Latitude": lats,
            "Longitude": longs,
            "Precipitation": precips,
            "Location": locs,
            "Date": date
        }
    )
    
    return geojson, data