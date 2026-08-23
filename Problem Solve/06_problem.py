#Count how many odd or even number from 1 to 20
Odd=0
Even=0 
# x = [2,5,6,1]     #jodi list theke count korte bolo
# for value in x:
for value in range(1,21):
    if (value%2==0):
        Odd += 1
    else:
        Even += 1

print(f"Odd: {Odd}, Even:{Even}")        
