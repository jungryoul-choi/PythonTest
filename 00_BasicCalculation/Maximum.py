# 주어진 데이터 중 가장 큰 값
import sys

def main():
    # Input
    max_val = -sys.maxsize -1

    # numbers = [2, 6, 3, 1, 4, 7, 8, 9]
    numbers = [-2, -5, -3, -7, -1]


    # Process
    for i in range(len(numbers)):
        if numbers[i] > max_val:
            max_val = numbers[i]
            # print(max_val)

    # Output
    print(f'The maximum number is {max_val} ')

if __name__ == "__main__":
    main()

