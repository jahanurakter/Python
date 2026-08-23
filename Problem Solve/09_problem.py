# separate odd or even number from a list
x = [2,5,6,1,9,11,14]
odd = []
even = []
for i in x:
    if (i%2==0):
        even.append(i)
    else:
        odd.append(i)
print("Odd =",odd)
print("Even =",even)