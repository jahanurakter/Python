#tuple immutable
# #tuple k unpack kora jay tuple er soman value niye tuple er variable k rakhle 
#a(10,) , na dile int hoye jay tuple hoy nah

fruits=("apple","banana","cherry","orange","mango")
print(fruits)           
a,b,*c=fruits           #(*means sob gulo value or modde jabe)
print(fruits)     

x=(10,)                     # , er karone tuple
print(type(x))              #signle element k tuple banate hole, dite hbe 
y=10
print(type(y))
z=(y,)
print(type(z))

