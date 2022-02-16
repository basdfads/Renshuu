def divisors(x):
    ran = list(range(1,int((x ** 0.5) + 1)))
    div_list = []

    for i in ran:
        if x % i == 0:
            if i == 1:
                div_list.append(1)
            
            elif i ** 2 == x:
                div_list.append(i)
        
            elif i != 1:
                div_list.append(i)
                div_list.append(int(x / i))
                
    return sorted(div_list)
