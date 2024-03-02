n = input()
length = len(n)
summary = 0 

# 왼쪽 부분의 자릿수 합 더하기 
for i in range(length//2): # in range(toindex)
    summary += int(n[i]) # 문자열 -> 정수 변환 

# 오른쪽 부분의 자릿수 합 빼기 
for i in range(length // 2, length): # in range(fromIndex : toIndex)
    summary -= int(n[i])

if summary == 0 : 
    print("LUCKY")
else:
    print("READY")


