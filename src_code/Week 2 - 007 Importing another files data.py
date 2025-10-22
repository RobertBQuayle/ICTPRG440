# Programmer BBQ
from math import sqrt                       #import sqrt funtion only
from myData import mylist1,mylist2,mylist3   #note origianl line import mydata did not work

def calculateDistance(mylist):
    
    x1 = mylist[0][0]
    y1 = mylist[0][1]
    x2 = mylist[1][0]
    y2 = mylist[1][1]

    distance = sqrt(((x2 - x1))**2 + ((y2 - y1))**2)    #math removed from math.sqrt
    return (distance)      
   
def calculateDistancemanylist(mylist1,mylist2,mylist3):

    myMultiList = []
    myMultiList.append(mylist1)
    myMultiList.append(mylist2)
    myMultiList.append(mylist3)

    for mylist in myMultiList:
        calculateDistance(mylist)

        print(f"Distance between {mylist[0]} and {mylist[1]} is {calculateDistance(mylist)}")
        


calculateDistancemanylist(mylist1,mylist2,mylist3)




