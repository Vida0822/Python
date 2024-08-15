# n+1일에 퇴사 --> 남은 N일 동안 최대한 많은 상담 
# T : 상담을 완료하는데 걸리는 기간 
# P : 받을 수 있는 금액 
# N = 15 --> 시간 복잡도 생각 X 

# 상담을 적절히 했을 때 얻는 최대 수익 
n = int(input())
T = []
P = []
for _ in range(n): 
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)

    
# 거꾸로 DP 수행 
dp = [0] * (n+2)  

# 초기 조건 
if T[n-1] == 1 :
    dp[n-1] = P[n-1] 

# 점화식 
m = dp[n-1] 
for i in range(n-1,-1,-1):
    if i+T[i] <= n : 
        m = max(m,P[i] + dp[i+T[i]])  
    dp[i] = m

print(max(dp))
