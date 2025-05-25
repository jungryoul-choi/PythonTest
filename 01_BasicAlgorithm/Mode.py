# 주어진 데이터에서 가장 많이 나타난(중복된) 값
# 최빈값 알고리즘(Mode Algorithm): 점수 인덱스(0~n)의 개수(Count)의 최댓값(MAX)
import sys

def main():
    # Input
    scores = [1, 2, 4, 3, 5, 3, 3, 5, 4]
    indexes = [0] * (5+1)
    max = -sys.maxsize -1
    mode = 0

    # Process
    for i in range(0, len(scores)):
        indexes[scores[i]] = indexes[scores[i]] + 1
    
    for i in range(0, len(indexes)):
        if indexes[i] > max:
            max = indexes[i]
            mode = i                      

    # Output
    print(f"최빈값은 {mode} 가 {max} 번 나타남.")
    
if __name__ == '__main__':
    main()
