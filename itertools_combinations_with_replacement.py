from itertools import combinations_with_replacement
s,n = input().split()
print(*[''.join(i) for i in combinations_with_replacement(sorted(s),int(n))],sep='\n')