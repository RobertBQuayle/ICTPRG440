import geopandas as gpd
import argparse
import pyproj
import fiona
 
# INPUT_PATH = r"C:\TAFE Programming\ICTPRG440\Lect4\spatial_data_original\Railway.kml"
# OUTPUT_PATH = r"C:\TAFE Programming\ICTPRG440\Lect4\output\Railway_GDA2020Zone56.kml"
 
 
def trans_From_Web_MTo_Geog_WGS84(InputPath,EPSG=4326):
    """
    this function trnsform coordinates from CRS TO ANOTHER
    """
    if not isinstance(InputPath,str):
        raise ValueError("you passed not a string")
   
    if not isinstance(EPSG,int):
        raise ValueError("you passed not integer")
   
    try:
        gdf = gpd.read_file(InputPath)
        gdf = gdf.to_crs(epsg=EPSG)  # transofmed from web mercator to Geographic wgs84
    except Exception as e:
        print(".........................Er..............................\n", e)
 
 
    return gdf # returns a geodatafram object
 
def stripDataToOnlySpecificState(gdf, state="New South Wales"):
 
    """
    -this function takes gdf and returns a gdf with only data from the state specified
    """
 
    if not isinstance(gdf, gpd.GeoDataFrame):
        raise ValueError("you passed not a Geodatafram")
   
    gdf = gdf[gdf["state"] == state]
 
    # print(gdf)
    return gdf
 
def export_gdf_to_GeoJson(gdf,OUTPUT_PATH):
 
    """-This function takes a geodataframe as a preameter gdf
       -It takes outfolder as string paramater
       -Returns None
       -This function exports the file name as output output.geojson.
       
    """
    if not isinstance(gdf, gpd.GeoDataFrame):
        raise ValueError("you passed not a Geodatafram")
   
 
    fulloutputPathWithFileName = OUTPUT_PATH + "\\" + "output.geojson"
 
    #print(fulloutputPathWithFileName)
 
    gdf.to_file(fulloutputPathWithFileName, driver="GeoJSON")
 
    return None
   
 
def constructParser():
 
    parser = argparse.ArgumentParser() #construct the parser instance from the class
 
    parser.add_argument("--i", required=True, help="INPUT_PATH")
    parser.add_argument("--o", required=True , help="OUTPUT_PATH")
    parser.add_argument("--e", required=True , help="ESPG")
 
    args = parser.parse_args()
 
    return args.i, args.o, args.e
 
 
 
if __name__  == "__main__":
 
 
    args_i, args_o, args_e = constructParser()
 
    trnformedgdf = trans_From_Web_MTo_Geog_WGS84(args_i, int(args_e))
 
    stripedGDF = stripDataToOnlySpecificState(trnformedgdf, state="Victoria")
 
    export_gdf_to_GeoJson(stripedGDF,args_o )