# Programmer: BBQ
# Creation Date: 19/10/2025
# Company: Gelos Enterprises 
# Client: Equinox Surveyors
# Version number 2.9999

"""
Purpose of program.
    The client, Equinox Surveyors, has asked for a program to read and check the coordinate system of some given data.
    This data is then to be transformed to GDA 2020 ZOne 56 and exported in Esri shapefile format. 
    The supplied information is provided in kml format. the client has specified that the reading and writing of this dta can be hardwired into the program.
    Password protect has been enabled.
"""
# Defining password 
def Passwordaccess():               #Creates password funtion.  
    Password = "555666"             #Sets password.
    guess = ""
    counter = 1                     #Sets guess counter to 1.

    while guess != Password and counter < 4:    # sets number of guesses to 3.
        guess = input(f"Enter Password, 3 tries allowed, Attempt {counter} - ")   #Text sent to comand line, if entered password is incorrect it will loop 3 times.
        counter += 1
    if guess == Password:
        print("Access Granted")     #Displayed text When a correct password is given.
        return True
    else:
        print("Go Away")            #Displayed text When 3 failed password attempts are made.
        return False

if __name__ == "__main__":          #Ensures this script only runs when executed directly, not when imported


    if Passwordaccess():                #Invokes password.

        import geopandas as gpd         #GeoPandas library is used for reading and exporting geospatial vector data. gpd is alias.

        '''
        The next 2 lines define the location of the data file to be read and the location of the output file
        the files are hardwired into this code as per clients request however in a more complex program this could become variable.
        Note the output file is labeled with the transformed coordinate system to avoid confusion.
        ''' 

        INPUT_DATA = r"C:\TAFE Programming\ICTPRG440-Assignemt\Input\Newcastle_Railways.kml"
        OUTPUT_PATH = r"C:\TAFE Programming\ICTPRG440-Assignemt\Output\Newcastle_Railway_GDA2020Zone56.shp"


        gdf = gpd.read_file(INPUT_DATA) # Loads data into a GeoDataFrame (gdf) for processing.

        def ShowAttributes(gdf): #Displays attribute table row by row
        
            print("Attribute Table:")
            for index, row in gdf.iterrows():
                print(row)

        ShowAttributes(gdf)


        EPSG = None                     # Initialise EPSG to None before querying original data file.

        """
        Next checks if the spatial data (gdf) has a defined coordinate reference system (CRS)
        Extracts EPSG code and prints to command line.
        If no CRS is found or the EPSG extraction fails, it prints a fail message.
        It then displays the first few rows of the data.
        """
        
        if gdf.crs:
            try:
                EPSG = gdf.crs.to_epsg()
            except Exception:
                EPSG = None

        if EPSG is not None:
            print("Original Coordinate system: EPSG:" + str(EPSG),"\n")
        else:
            print("nil coordinate system present")

        print(gdf.head(),"\n")  #Show first five rows of the gdf. head() is default 5 lines. 
                                #The coordinates can be seen displayed here in Lat/long.


        def CordsystemTransformation(FilePath,EPSG=7856):

            gdf = gpd.read_file(FilePath)
            gdf = gdf.to_crs(epsg=EPSG)  # GDA2020 / MGA zone 56
            return gdf

        Transformed = CordsystemTransformation(INPUT_DATA,EPSG=7856)    #Invokes the Coordinate transformation.
        print(Transformed.head(),"\n")                                  #Shows first five rows of the transformed data. Coordinates can be seen and verified after transformation.
        print("Coordinate System is now GDA2020 / MGA zone 56""\n")     #Prints Confirmation that the program has run and transformed the data.
        Transformed.to_file(OUTPUT_PATH, driver="ESRI Shapefile")       #Creates ESRI Shapefile and saves in Output directory.
