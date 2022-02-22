### https://codingdojang.com/scode/478?answer_mode=hide

n = int(input('입력할 정수의 개수', ))

interger_memory = [0] * n

for i in range(len(interger_memory)):
    interger_memory[i] = int(input(f'{i+1} 번쨰 정수를 입력',))

print(f'입력한 {n}개 정수의 합:', sum(interger_memory))
print(f'입력한 {n}개 정수의 평균:', sum(interger_memory) / n)

interger_memory = []
