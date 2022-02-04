from itertools import permutations, combinations, product
from timeit import repeat

a = ['a','b','c']
result = list(permutations(a,2))
result1 = list(combinations(a,3))
result2 = list(product(a,repeat=2))
print("per",result)
print("com",result1)
print("pro",result2)

