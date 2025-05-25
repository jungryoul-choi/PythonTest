#1. Input
count = 0

#2. Process
for i in range(1, 1001):
    # print(f'i = {i}')
    if i % 13 == 0:
        count += 1
        print(f'i = {i}')

#3. Output
print(f'1부터 1000까지의 정수 중 13의 배수의 개수: {count}')

