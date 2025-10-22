# Programmer BBQ

myList = [2,4,6,8.2,"not feeling it"]

#print((myList[-2]))

myList2 = [[321,312,23,"Pt1"],[432,532,12,"Pt2"],[123,312,43,"Pt3"],[432,532,34,"Pt4"],[231,345,67,'Pt5'],[5324,5432,543,"Pt6"]]


print(myList2[1])
print((myList2[0][3]))

for Coords in myList2:
    print(Coords[3])


print(len(myList))
print(len(myList2))

for i in range((len(myList2))):
   print(i)
   print(myList2[i])



for i in range(len(myList2)):
    for x in range(len(myList2[i])):
        print(i)
        print(x)
        print(myList2[i][x])


