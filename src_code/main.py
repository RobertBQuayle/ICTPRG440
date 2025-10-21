# Programmer BBQ
# Version 1  Import file, confirm cordinate system, change and export
# Version number 1.9999


def Passwordaccess():
    Password = "555666"
    guess = ""
    counter = 1

    while guess != Password and counter < 4:
        guess = input(f"Enter Password, 3 tries allowed, Attempt {counter} - ")
        counter += 1
    if guess == Password:
        print("Access Granted")
        return True
    else:
        print("Go Away")
        return False

if Passwordaccess():

    import geopandas as gpd
    INPUT_DATA = r"C:\TAFE Programming\ICTPRG440-Assignemt\Input\Newcastle_Railways.kml"
    OUTPUT_PATH = r"C:\TAFE Programming\ICTPRG440-Assignemt\Output\Newcastle_Railway_GDA2020Zone56.shp"




    gdf = gpd.read_file(INPUT_DATA)

    def ShowAttributes(gdf):    

        print("Attribute Table:")
        for index, row in gdf.iterrows():
            print(row)

    ShowAttributes(gdf)

    EPSG = None

    if gdf.crs:
        try:
            EPSG = gdf.crs.to_epsg()
        except Exception:
            EPSG = None

    if EPSG is not None:
        print("Original Coordinate system: EPSG:" + str(EPSG),"\n")
    else:
        print("nil coordinate system present")

    print(gdf.head(),"\n")


    def CordsystemTransformation(FilePath,EPSG=7856):

        gdf = gpd.read_file(FilePath)
        gdf = gdf.to_crs(epsg=EPSG)  # GDA2020 / MGA zone 56
        return gdf

    Transformed = CordsystemTransformation(INPUT_DATA,EPSG=7856)
    print(Transformed.head(),"\n")
    print("Coordinate System is now GDA2020 / MGA zone 56""\n")
    Transformed.to_file(OUTPUT_PATH, driver="ESRI Shapefile")
