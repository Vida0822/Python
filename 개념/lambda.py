# lambda 형식  - 'lambda 매개변수 : ㅍ현식 
print((lambda x, y : x+y)(10,20)) #30 

f = lambda x : x+1 
print(f(3)) # 4 



# map(함수, 리스트) : 리스트의 원소를 하나씩 꺼내 함수 적용

l = map(lambda x : x**2 , range(5)) #  [0, 1, 2, 3, 4]
l = list(l) # 리스트로 변환
print(l[::]) # [0, 1, 4, 9, 16]



# reduce(함수, 시퀀스)
# : 시퀀스(문자열, 리스트, 튜플) 원소를 하나씩 꺼내 함수 적용 -> 이전 결과값에 누적
# => x에 이전 누적값, y에 새로 읽은 원소 대입
from functools import reduce 
l = reduce(lambda x, y: y+x, 'abcde') 
print(l) # edcba

l = reduce(lambda x, y: x+y, [0,1,2,3,4])
print(l) # 10

# filer(함수, 리스트)
# 리스트의 원소를 함수에 적용해 결과가 참인 값들만 반환
l = filter(lambda x: x< 5, range(10))
print(list(l)) # [0, 1, 2, 3, 4]

l = filter(lambda x : x%2, range(10)) # 2로 나누어 떨어지지 않는 수만 반환
print(list(l)) # [1, 3, 5, 7, 9]








