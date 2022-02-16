"""
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""


num = 1000000

def factorial(n):
    fac = 1
    for i in range(1,n+1):
        fac = fac * i
    return fac

sets = []

for i in reversed(range(1,10)):
    c = (num - 1) // factorial(i)
    sets.append(c)
    num = num - c * factorial(i)
    
sets.append(0)

mil_lexper = ''

ran = [0,1,2,3,4,5,6,7,8,9]

for i in range(len(ran)):
    mil_lexper = mil_lexper + str(ran.pop(sets[i]))

print(mil_lexper)
