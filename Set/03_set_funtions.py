#set() - it's called empty set
#dict{}- it's called empty dictionary
#set doesn't support indexing

x = {1,2,4}
x.add(5)            #add function of set
print(x)
x.update(6,7,8)
# x.clear()
print(x)       


a={1,2,3}
b={3,4,5}

z=a.difference(b)               #difference between x and y

print(z)