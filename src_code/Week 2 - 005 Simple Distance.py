# Programmer BBQ
import math

mylist= [[0, 0], [5, 12]]

print("My Coords are ",mylist,"\n")

def calculateDistance(mylist):
    
    x1 = mylist[0][0]
    y1 = mylist[0][1]
    x2 = mylist[1][0]
    y2 = mylist[1][1]

    distance = math.sqrt(((x2 - x1))**2 + ((y2 - y1))**2)
    return distance      
   
   
print(calculateDistance(mylist))
