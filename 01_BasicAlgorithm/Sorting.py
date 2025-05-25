# 무작위 데이터를 순서대로 [오름차순(Asc)|내림차순(Desc)] 정렬렬
# 정렬 알고리즘(Sort Algorithm): 가장 작은/큰 데이터를 왼쪽으로 순서대로 이동
def main():
    # Input
    data = [3, 2, 1, 5, 4]
    N = len(data)
    # print(data)
    
    # Process: Selection Sort (선택 정렬)
    for i in range(0, N-1):
        for j in range(i+1, N):
            if data[i] > data[j]:
                temp = data[i]; data[i] = data[j]; data[j] = temp

        # print(data)
    
    # Output
    for i in range(N):
        print(data[i])

if __name__ == '__main__':
    main()