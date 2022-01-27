inp = str(input('수식을 입력: '))

comp = inp.split()


def arith(x):
    while '/' in x:
        div = x.index('/')
        divex = 1 / float(x[div+1])
        del x[div:div+2]
        x.insert(div,'*')
        x.insert(div+1, str(divex))
        
    while '-' in x:
        sub = x.index('-')
        minex = -float(x[sub+1])
        del x[sub:sub+2]
        x.insert(sub,'+')
        x.insert(sub+1, str(minex))
        
    while '*' in x:
        mul = x.index('*')
        mulre = float(x[mul-1]) * float(x[mul+1])
        del x[mul-1:mul+2]
        x.insert(mul-1, str(mulre))
        
    while '+' in x:
        add = x.index('+')
        addre = float(x[add-1]) + float(x[add+1])
        del x[add-1:add+2]
        x.insert(add-1, str(addre))
        
    return float(x[0])



while '(' in comp:
    pars = comp.index('(')
    parc = comp.index(')')
    adv = comp[pars+1:parc]
    print(adv)
    adva = arith(adv)
    print(adva)
    del comp[pars:parc+1]
    comp.insert(pars, adva)
    del adv
  
ans = arith(comp)
print('결과 :', ans)
