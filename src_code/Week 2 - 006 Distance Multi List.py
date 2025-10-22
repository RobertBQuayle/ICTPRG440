# Programmer BBQ
import math

mylist1= [[0, 0], [3, 4]]
mylist2= [[0, 0], [5, 12]]
mylist3= [[0, 0], [7, 24]]

def calculateDistance(mylist):
    
    x1 = mylist[0][0]
    y1 = mylist[0][1]
    x2 = mylist[1][0]
    y2 = mylist[1][1]

    distance = math.sqrt(((x2 - x1))**2 + ((y2 - y1))**2)
    return (distance)      #for raw answer the line could read "return print(distance)"
   
def calculateDistancemanylist(mylist1,mylist2,mylist3):

    myMultiList = []
    myMultiList.append(mylist1)
    myMultiList.append(mylist2)
    myMultiList.append(mylist3)

    for mylist in myMultiList:
        calculateDistance(mylist)

        print(f"Distance between {mylist[0]} and {mylist[1]} is {calculateDistance(mylist)}") #This was a fancy way to provide output, required madification to line 16
        


calculateDistancemanylist(mylist1,mylist2,mylist3)




