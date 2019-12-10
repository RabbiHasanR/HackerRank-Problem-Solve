from itertools import product
a=input().split()
b=input().split()
numbers1 = [ int(x) for x in a ]
numbers2 = [ int(x) for x in b]
result=list(product(numbers1,numbers2))
for i in result:
    print(i,end=" ")