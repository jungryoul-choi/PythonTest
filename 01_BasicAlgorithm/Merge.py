# 2개의 정수 배열 합치기: 단, 2개의 배열은 오름차순으로 정렬되어 있다고 가정
# 병합 알고리즘(Merge Algorithm): 오름차순으로 정렬되어 있는 정수 배열을 하나로 병합합
def main():
    # Input
    first = [1, 5, 9, 14, 18, 23, 26, 38]
    second = [2, 4, 8, 12]
    M = len(first); N = len(second)
    merge = [0] * (M + N)
    i = 0; j = 0; k = 0
    
    # Process: Merge
    while (i < M and j < N):
        if first[i] < second[j]:
            merge[k] = first[i]; k += 1; i += 1
        else:
            merge[k] = second[j]; k += 1; j += 1
    
    while (i < M):
        merge[k] =  first[i]; k += 1; i += 1

    while (j < N):
        merge[k] = second[j]; k += 1; j += 1
    
    # Output
    for item in merge:
        print(item, end=", ")

if __name__ == '__main__':
    main()
