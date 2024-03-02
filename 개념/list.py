a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a)
print(a[4])

# 빈 리스트
a = list()
print(a)

a = [] 
print(a)

# 초기화
n = 10
a = [0]*n
print(a) 

# 인덱싱 
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a[-1]) # 9 : 뒤에서 첫번째 원소
print(a[-3]) # 7: 뒤에서 세번째 원소 

a[3] = 7 
print(a) 

# 슬라이싱 
print(a[1:4]) # [2, 3, 7] : 2번째 ~ 4번째 원소까지 

# 리스트 컴프리헨션 
array = [i for i in range(20) if i % 2 == 1] # [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
print(array)

array = [i * i for i in range(1, 10)] # [1, 4, 9, 16, 25, 36, 49, 64, 81]
print(array)

n = 3 
m = 4 
array = [[0] * m for _ in range(n)] # n행 m열  : [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
# _ : 반복을 위한 변수의 값을 무시하고자 할때 (필요 없을때)
print(array)

# 메서드 
a = [1, 4, 3]
print("기본 리스트 : ", a ) # 문자열 연결은 쉼표로

a.append(2)
a.sort()
a.sort(reverse = True)
a.reverse()
a.insert(2, 3)
print(a.count(3))
a.remove(1)

remove_set = {3,5} 
result = [i for i in a  # a의 요소 하나씩 돌면서 i에 담고, 만약 그 i 가 remove_set에 없으면 result 리스트에 삽입  
          if i not in remove_set] # 여러 원소 삭제 , [1,4,3]



