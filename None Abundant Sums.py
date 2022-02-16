"""
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

"""



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

nums = range(1,28124)
abnums = []
for i in nums:
    if i < sum(divisors(i)):
        abnums.append(i)

sumofab = []
for i in abnums:
    for j in abnums:
        if i + j <= 28123:
            sumofab.append(i+j)
        else:
            pass
sum(nums) - sum(list(set(sumofab)))
