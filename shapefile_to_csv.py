import geopandas as gpd
import pandas as pd

# Specify the path to the shapefile
shapefile_path = 'path/to/your/shapefile.shp'

# Specify the path for the output CSV file
csv_path = 'path/to/output/file.csv'

# Read the shapefile into a GeoDataFrame
try:
    gdf = gpd.read_file(shapefile_path)
except Exception as e:
    print(f"Error reading shapefile: {e}")
    exit()

# (Optional) Perform data manipulation if needed
# For example, rename a column:
# gdf = gdf.rename(columns={'old_column_name': 'new_column_name'})

# Export the GeoDataFrame to a CSV file
try:
    gdf.to_csv(csv_path, index=False)
    print(f"Successfully exported data to {csv_path}")
except Exception as e:
    print(f"Error writing to CSV: {e}")
