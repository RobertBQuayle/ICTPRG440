import geopandas as gpd

# Define input and output paths
INPUT_DATA_LOCATION = r"C:\TAFE Programming\ICTPRG440\Lect4\spatial_data_original\Railway.kml"
DATA_OUTPUT_LOCATION = r"C:\TAFE Programming\ICTPRG440\Lect4\output\Railway_GDA2020Zone56.kml"

# Read the KML file
gdf = gpd.read_file(INPUT_DATA_LOCATION, driver='KML')

# Print the original coordinate system
print("Co-ordinate System:", gdf.crs)

# Transform to GDA2020 / MGA Zone 56 (EPSG:7856)
gdf_transformed = gdf.to_crs(epsg=7856)

# Print the new coordinate system
print("Transformed to:", gdf_transformed.crs)

# Save the transformed data back to KML
gdf_transformed.to_file(DATA_OUTPUT_LOCATION, driver='KML')

print(f"File saved to: {DATA_OUTPUT_LOCATION}")