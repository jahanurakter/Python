#find the largest number from a list
x = [2,5,6,1,9,11,14]

a = x[0]

for i in x:
    if i > a:
        a=i
print("Large:",a)
