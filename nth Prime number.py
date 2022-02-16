Pl = [2]

n = Pl[-1]+1

def div(x):
    return n % x

while len(Pl) < 10:
    if all(list(map(div,Pl))) == True:
        Pl.append(n)
        n = n +1
    else:
        n = n + 1
print(Pl[-1])
