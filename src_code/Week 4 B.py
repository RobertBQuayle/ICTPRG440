import geopandas as gpd

FILE_PATH = r"C:\TAFE Programming\ICTPRG440\Lect4\spatial_data_original\Railway.kml"

def CordsystemTransformation(FilePath,ESPG=7856):

    gdf = gpd.read_file(FilePath)
    gdf = gdf.to_crs(epsg=4326)

    return gdf

Transformed = CordsystemTransformation(FILE_PATH,ESPG=7856)

print(Transformed.head())





#print(gdf.crs)

#print(gdf.head())
#print(gdf.columns)

#gdf = gdf.to_crs(epsg=4326)
#print(gdf.head())