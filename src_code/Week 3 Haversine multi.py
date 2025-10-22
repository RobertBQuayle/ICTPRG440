# Programmer BBQ
from CityDistanceV1 import haversine
import csv

FILEPATH_IN = r"C:\TAFE Programming\ICTPRG440\Resources\CountryList.csv" 
FILEPATH_OUT = r"C:\TAFE Programming\ICTPRG440\src_code\output.csv"

SYDNEY_LAT, SYDNEY_LONG = -33.8727, 151.2057 

def distmanyplaces(Listin,resultout,originalLAT,OriginalLong):

    if not isinstance(Listin, str) or not Listin:
        raise ValueError("Listin must be a non-empty string")
    if not isinstance(resultout, str) or not resultout:
        raise ValueError("Resultout must be a non-empty string")

    if not (-90.0 <= originalLAT < 90.0):
        raise ValueError("originalLAT must be between -90 and 90 deg")
    if not (-180.0 <= OriginalLong < 180.0):
        raise ValueError("OriginalLong must be between -180 and 180 deg")
    
    Coordslist = []

    try:
        with open(Listin,"r",newline="", encoding="UTF-8") as f_in:
            reader = csv.DictReader(f_in)


            for row in reader:
                Coordslist.append({
                    "country": row["Country"],
                    "capital": row["Capital"],
                    "lat": float(row["Latitude"]),
                    "lon": float(row["Longitude"])
                })
    except Exception as e:
        print("Error in Reading the file", e)



    try:
        with open(resultout,"w", newline="", encoding="UTF-8") as f_out:
            writer = csv.writer(f_out)

            for capital in Coordslist:
                distance = haversine(originalLAT, OriginalLong, capital["lat"], capital["lon"])
                print(capital["capital"], distance, "km")
                if distance  < 100000:
                    writer.writerow(["Distance from Sydney to " + capital["capital"] + " is " + str(distance) + "km"])
                    
 #                   print(f"{capital['capital']} → {distance} km (type: {type(distance)})")
    
    except Exception as e:
        print("Error in writing file", e)

    print(Coordslist)




if __name__ == "__main__":
    distmanyplaces(FILEPATH_IN,FILEPATH_OUT,SYDNEY_LAT,SYDNEY_LONG)