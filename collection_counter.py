import collections

numShoes = int(input())
shoes = collections.Counter(map(int, input().split()))
if sum(shoes.values())!=numShoes:
    print(sum(shoes.values()))
    print('The shoe count does not equal shoes entered.  Please restart and try again.')

numCust = int(input())

income = 0

for i in range(numCust):
    size, price = map(int, input().split())
    if shoes[size]: 
        income += price
        shoes[size] -= 1

print (income)