def myfunc(a):
  return len(a)

x = map(myfunc, ('apple', 'banana', 'cherry'))    #map - loop er moto kaj kore
print(list(x))              #list na likhle print hbe na


def multiply(a, b):
    return b * 2

numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]

result = map(multiply, numbers1, numbers2)      #map choose (function name and value)
print(list(result))