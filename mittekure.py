a = input("수식을 입력: ")
ran = range(len(a))
comp = []
s = ['(', '+', '-', '*', '/', ')']
for i in ran:
    chr = a[i]
    if comp == []:
        comp.append(chr)
        
    elif chr in s:
        comp.append(chr)
        
    elif comp[-1] in s:
        comp.append(chr)      
        
    else:
        comp[-1] = comp[-1]+chr
        
comp
