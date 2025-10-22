# Programmer BBQ

myList = [2.0,4,6,4,"Your Text Here","ClassA",4,4,3,4]
myList2 = [2.0,4,6,4,"Your Text Here","ClassB"]

counter = 0

for i in myList:
    if i == 4:
       counter = counter + 1
       continue
    elif i == "ClassC":
        print("There is a class B","\n")    
        break
    else:
        print("Nill")
print (counter)
