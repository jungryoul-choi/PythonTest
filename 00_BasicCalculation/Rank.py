# 주어진 데이터의 순위를 구하는 로직

# 순위 알고리즘(Rank Algorithm): 점수 데이터에 대한 순위 구하기
def main():
    # Input
    scores = [90, 87, 100, 95, 80]
    N = len(scores)
    rankings = [1] * 5    
    print(rankings)
    
    # Process    
    for i in range(N):
        rankings[i] = 1
        for j in range(N):
            if scores[i] < scores[j]:
                rankings[i] += 1
        
    # Output
    for i in range(N):
        print(f"rankings[{i}] = {scores[i]} ranking = {rankings[i]}")
    
    pass

if __name__ == '__main__':
    main()
