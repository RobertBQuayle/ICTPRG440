# Programmer BBQ

myList = [2.0,4,6,4,"Your Text Here","ClassA"]
myList2 = [2.0,4,6,4,"Your Text Here","ClassB"]

#for items in myList:
#    print (items)

isClassA = False
isClassB = False

#print(type(isClassA))

if myList[-1] == "ClassA":
    isClassA = True

#print(isClassA)

if myList2[-1] == "ClassA":
    isClassB = True

#print(isClassB)

for i in myList:
    if i == 4:
        print("YES!")
    elif i == "ClassA":
        print("There is a class B","\n")    
    else:
        pass

for i in myList:
    if i == 4:
        print("YES!")
    elif i == "ClassA":
        print("There is a class B","\n")    
    else:
        print("Nill")

counter = 0

for i in myList:
    if i == 4:
       counter = counter + 1
#   elif i == "ClassA":
#        print("There is a class B","\n")    
#    else:
#        print("Nill")
print (counter)
