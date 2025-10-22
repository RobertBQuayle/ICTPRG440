# Programmer BBQ
import math


# Coordinates of Sydney in Decimal Deg 

LatS = -33.8727
LongS = 151.2057 

# Coordinates of Melbourne in Decimal Deg

LatM = -37.8136
LongM = 144.9631

#conversion Deg to Radians

LatSradian = math.radians(LatS)
LongSradian = math.radians(LongS)
LatMradian = math.radians(LatM)
LongMradian = math.radians(LongM)

# Alternative way to convert to radians,   xlat,xlong,y,lat,ylong = map(radians,(xlat,xlong,y,lat,ylong))



def haversine(LatSradian, LongSradian, LatMradian, LongMradian, R=6371):
    
    a= math.sqrt(math.sin((LatMradian-LatSradian)/2)**2 + math.cos(LatMradian)* math.cos(LatSradian)* math.sin((LongMradian-LongSradian)/2)**2)

    d = 2*math.asin(a)*R

#    print(d) 
    return d    


haversine(LatSradian, LongSradian, LatMradian, LongMradian)



