# 원본 데이터 중에서 대상 데이터와 가장 가까운 값
import sys

# 근사값 알고리즘: 가까운 값 -> 차잇값의 절댓값의 최솟값

def main():
    # Initialize
    min = sys.maxsize
    
    # Input
    numbers = [10, 20, 50, 28, 49, 23, 94, 76, 22, 48]
    target = 25
    near = 0
    
    # Process
    for i in range(len(numbers)):
        _abs = abs(numbers[i] - target)
        if _abs < min:
            min = _abs
            near = numbers[i]
            print(f"min = {min}, near = {near}")
    
    # Output
    print(f"{target}과 가장 가까운 값 : {near} (차이 {min})")
    
    pass

if __name__ == '__main__':
    main()
