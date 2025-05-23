# n명의 점수 중에서 80점 이상인 점수의 합계

# Input
scores = [90, 85, 70, 95, 60, 80]
sum = 0
N = len(scores)

# Process
for i in range(N):
    if scores[i] >= 80:
        sum += scores[i]

# Output
print(f"{N}명의 점수 중에서 80점 이상인 점수의 합계는 {sum}입니다.")