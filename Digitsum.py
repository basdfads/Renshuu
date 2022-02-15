num = int(input())
ran = range(len(str(num)))
digitsum = 0
for d in ran:
    a = int(str(num)[int(d)])
    digitsum = digitsum + a 
print('Digit sum:',digitsum)
