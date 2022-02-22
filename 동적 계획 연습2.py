#https://codingdojang.com/scode/504?answer_mode=hide

numod = [0]*10
for i in range(1,1001):
    string = str(i)
    for d in str(i):
        numod[int(d)] = numod[int(d)] + 1
numod
