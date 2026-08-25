#print the multiplication table of number 5

x=5

for i in range(1,11):
    print(f"{x}X{i}={x*i}")
#-------------------------------------
'''Read a number from input.
Print its multiplication table from 1 to 10.'''

n = int(input("Enter your number: "))

for i in range(1,11):
    print(f"{n}X{i}={n*i}")
