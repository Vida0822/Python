n = int(input())
data = list(map(int, input().split())) 
# input() : 입력받은걸, split() : 공백기준으로 오려서, int : int형으로 변환해서, list : list 자료형으로 만든다 
data.sort()

result = 0 # 총 그룹의 수 
count = 0 # 현재 그룹에 포함된 모험가의 수 

for i in data :  # 공포도를 낮은 것부터 하나씩 확인하며
    count += 1  # 현재 그룹에 해당 모험가 포함시키기
    if count >= i : # 현재 그룹에 포함된 모험가 수가 현재의 공포도 이상이라면 
        result+=1 # 그룹 결성
        count = 0  # 모험가 수 초기화 

print(result)

