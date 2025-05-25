# 정렬되어 있는 데이터를 이진검색을 사용하여 반씩 나누어서 검색
# 검색 알고리즘(Search Algorithm): 주어진 데이터에서 특정 데이터 확인
def main():
    # Input
    #idx = [0, 1, 2, 3,  4,  5,  6,  7,  8,  9]
    data = [1, 3, 7, 9, 14, 16, 23, 39, 42, 54]
    N = len(data)
    search = 16
    flag = False
    index = -1
    
    # Process: 이진 검색(Binary Serch) Full Scan -> Index Scan
    low = 0
    high = N-1
    while low <= high:
        mid = int((low + high) / 2)
        print(data[mid])
        if data[mid] == search:
            flag = True; index = mid; break;
        if data[mid] > search:
            high = mid -1
        else:
            low = mid + 1

    
    # Output
    if flag:
        print(f"{search}을(를) {index} 위치에서 찾았습니다.")
    else:
        print("찾지 못했습니다.")
    
    pass

if __name__ == '__main__':
    main()
