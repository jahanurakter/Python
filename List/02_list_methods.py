stu = ["Laboni", "Ratul", "Samia", "Harry", "Oishi", "Masiha"]

stu.append("JEFFY")         #append means add somenthing at the last of list
stu.insert(2, "Jeffy")      #insert index e bose
print(stu)
stu.remove("Ratul")     #kono item remove korar jonno remove method use kora hoy
stu.pop(5)          #pop() faka thakle last item remove kore
                    #pop index diyeo kora jay
print(stu)


roll = [1, 7, 0, 2, 9]
roll[2] = roll[4]           #roll er modde e index k 4 index k replace kore
print(roll)
roll.sort()
print(roll)
roll.extend(stu)            # extend e koyekta list add kra jabe
print("After Extend:", roll)
