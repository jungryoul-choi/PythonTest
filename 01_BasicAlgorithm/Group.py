# 컬렉션 형태의 데이터를 특정 키 값으로 그룹화
# 그룹 알고리즘(Group Algorithm): 특정 키 값에 해당하는 그룹화된 합계 리스트 만들기
class Record():
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

def main():
    # Input
    records = [Record("RADIO", 3), Record("TV", 1), Record("RADIO", 2), Record("DVD", 4)]
    groups = []
    N = len(records)
    
    # Process: Group 알고리즘(Sort -> Sum -> Group)
    # Sort
    for i in range(N - 1):
        for j in range(i + 1, N):
            if (records[i].name > records[j].name):
                temp = records[i]
                records[i] = records[j]
                records[j] = temp

    # Group
    subtotal = 0
    for i in range(N):
        subtotal = subtotal + records[i].quantity
        # 다음 레코드가 없거나 현재 레코드와 다음 레코드가 다르면 저장.
        if (i + 1) == N or records[i].name != records[i + 1].name:
            groups.append(Record(records[i].name, subtotal))
            subtotal = 0
    
    # Output
    print("정렬된 원본 데이터")
    for r in records:
        print(f"{r.name.rjust(6)} : {r.quantity}")

    print("이름으로 그룹화된 데이터")
    for g in groups:
        print(f"{g.name.rjust(6)} : {g.quantity}")

if __name__ == '__main__':
    main()