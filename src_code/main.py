# Programmer: BBQ
# Creation Date: 19/10/2025
# Company: Gelos Enterprises 
# Client: Equinox Surveyors
# Version number 3.9999

"""
Purpose of program.
    The client, Equinox Surveyors, has asked for a program to read and check the coordinate system of some given data.
    This data is then to be transformed to GDA 2020 ZOne 56 and exported in Esri shapefile format. 
    The supplied information is provided in kml format. the client has specified that the reading and writing of this dta can be hardwired into the program.
    This program has gone through several iterations with more functionality added with each version.
    Password protection has been enabled
"""
'''
import os

def Passwordaccess():               #Creates password function.  
    Password = "555666"             #Sets password.
    guess = ""
    counter = 1                     #Sets guess counter to 1.

    while guess != Password and counter < 4:    # sets number of guesses to 3.
        guess = input(f"Enter Password, 3 tries allowed, Attempt {counter} - ")   #Text sent to command line, if entered password is incorrect it will loop 3 times.
        counter += 1
    if guess == Password:
        print("Access Granted")     #Displayed text When a correct password is given.
        return True
    else:
        print("You have exceeded the maximum allowed attempts! BYE BYE")            #Displayed text When 3 failed password attempts are made.
        return False

if __name__ == "__main__":                  #Protects main loop from running on import

    if  not Passwordaccess():                   #Invokes password. Modified from original code for looping.
        exit()
    while True:
'''

import geopandas as gpd         #GeoPandas library is used for reading and exporting geospatial vector data. gpd is alias.
import os

'''
        The next lines define the location of the data file to be read, verified as kml and then location of the output file.
        this section has been modified from the original code from having the data file input and output hard coded to allowing the user to enter the file names.
        This allows for more lexibility and reuse of this program with different files.
        ''' 
    

filename = input("Enter the name of the file to import - include extension ")
input_dir = r"C:\TAFE Programming\ICTPRG440-Assignemt\Input"
INPUT_DATA = os.path.join(input_dir, filename)
            
if not os.path.exists(INPUT_DATA):                              #Checks if file exisist.
    print("Error: The input file does not exist.")
    exit()

if not INPUT_DATA.lower().endswith(".kml"):                     #Check if the input file is a KML file using operating system module.
    print("Error: The input file is not a KML file.","\n")       #If file is not a *.kml file then program terminates.
    exit()
else:
    print("data comfirmed as kml","\n")
    input("Press Enter to continue...",)

output_name = input("Enter the base name for the output shapefile (no extension): ")
output_dir = r"C:\TAFE Programming\ICTPRG440-Assignemt\Output"
output_filename = output_name + "_GDA2020_MGA_zone_56.shp"
OUTPUT_PATH = os.path.join(output_dir, output_filename)

if os.path.exists(OUTPUT_PATH):                                             #Places a warning if output already exists.
    print("Warning: Output file already exists and will be overwritten!")
    input("Press Enter to continue or Ctrl+C to cancel...")
    

gdf = gpd.read_file(INPUT_DATA) # Loads data into a GeoDataFrame (gdf) for processing.


def ShowAttributes(gdf): #Displays attribute table row by row
        
    print("Attribute Table:","\n")
    for index, row in gdf.iterrows():
        print(row)

ShowAttributes(gdf)
input("Press Enter to continue...")

print("Column headers:", gdf.columns.tolist())  #This lists the column headers from the kml file. Shape files, which will be the output have a 10 charater limit.
input("Press Enter to continue...")             #Pauses the program so the headers can be read. 

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


import warnings                                                 #Column names longer than 10 characters will be truncated, this supresses the error messages from this.
warnings.filterwarnings("ignore", category=UserWarning)         #Suppressing warnings is not ideal but the client insisted on using a shape file export.
warnings.filterwarnings("ignore", category=RuntimeWarning)      #This can be avoided by altering the original KML file.

def CordsystemTransformation(FilePath,EPSG=7856):               #Transforms the coordinate system

    gdf = gpd.read_file(FilePath)
    gdf = gdf.to_crs(epsg=EPSG)                                 #Reprojects the data to the specified EPSG coordinate system
    return gdf

Transformed = CordsystemTransformation(INPUT_DATA,EPSG=7856)    #Invokes the Coordinate transformation to GDA2020 / MGA zone 56
print(Transformed.head(),"\n")                                  #Shows first five rows of the transformed data. Coordinates can be seen and verified after transformation.
print("Coordinate System is now GDA2020 / MGA zone 56","\n")     #Prints Confirmation that the program has run and transformed the data.
Transformed.to_file(OUTPUT_PATH, driver="ESRI Shapefile")       #Creates ESRI Shapefile and saves in Output directory.

print("Output saved to:","\n", OUTPUT_PATH)                              #conformation of output location


again = input("Would you like to convert another file? (yes/no): ").strip().lower()     #Repeats if user wants to process another file.
if again != "yes":
    print("Have a nice day!","\n")
            
                                                                               
