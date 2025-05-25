# 주어진 데이터 중에서 가장 작은 짝수 값?
import sys

# 최소값 알고리즘
def main():
    # Initialize
    min = sys.maxsize

    # Input
    numberts = [5, 7, 8, 9, 4, 1, 2]

    # Process
    for i in range(len(numberts)):
        if numberts[i] < min and numberts[i] % 2 == 0:
            min = numberts[i]
            # print(f'i = {numberts[i]}')

    # Output
    print(f'even min number is {min}')

if __name__ == '__main__':
    main()
