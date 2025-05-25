# Input
sum = 0

# Process
for i in range(1, 20):
    if i % 2 != 0:
        sum = sum + i
        print(i, end='\t')

# Output
print(f'\n1부터 20까지의 홀수의 합은 {sum}입니다.')