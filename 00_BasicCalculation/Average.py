#1. Input
data = [90, 65, 78, 50, 95, 88, 67, 81, 83]
sum = 0
count = 0
N = len(data)

#2. Process
avg = 0.0

for i in range(N):
    if data[i] >= 80 and data[i] <= 95:
        sum += data[i]
        count += 1

if sum != 0 and count != 0:
    avg = sum / count

#3. Output
print(f'80점 이상 95점 이하인 점수의 평균은? {avg:.2f}')