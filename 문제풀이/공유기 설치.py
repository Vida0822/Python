
# 집 N개 (x1~xn) --> 공유기 C개 설치 
# 가장 인접한 공유기 사이의 거리가 가능한 최대가 되도록 (최대한 띄엄띄엄 설치해야 함)  
# 공유기 영향 범위 고려 X --> 그냥 설치하고, 그 서로의 거리가 되도록 멀리 떨어지는게 good  
import sys
f = sys.stdin.readline

n, c = map(int,f().split())
# n : 200,000 --> 큰 수 : N 또는 N log N 
# c : 2 < < N  
# 2s 

# 집 좌표 입력 
loc = []
for _ in range(n+1):
    loc.append(int(input()))

loc.sort() # 이진 탐색 조건 : 정렬

# 설치하고 --> 해당 거리가 최대인지 반환 --> 공유기 조정 
# 찾고자하는 값(검새 대상): 각 공유기 사이 최소 거리 

start = 1 # 가능한 인접거리 중 최소 
end = loc[-1] - loc[0] # 가능한 인접 거리 중 최대  

answer = 0 
while(start <= end) : 
    mid = (start+end) // 2 # 최소 거리 예상치
    
    value = loc[0] # 첫번째 집엔 공유기 설치
    count = 1 # 설치한 공유기 갯수 
    
    for i in range(1,n) : 
        if loc[i] >= value + mid :  # 설치 좌표 + 최소 거리 예상치보다 더 멀리 집 좌표가 있을 땐 
            
            # 설치 
            value = array[i]
            count += 1 
        # 설치 좌표 + 최소 거리 예상치보다 더 가까운 곳에 집이 있을 땐 
        # --> 설치하면 X : 그럼 예상 최소 거리가 갱신되기 때문에 
        
    if count >= c :  # 결과적으로 c개 이상 공유기 설치 --> 최소거리 예상치를 너무 작게잡음 (더 떨어트릴 수 있음)
        answer = mid 
        start = mid +1  
    else : # 결과적으로 공유기 c개 설치 못함 --> 최소거리 예상치를 너무 크게 잡음(이걸 만족시키려고 공유기를 설치 X )
        end = mid - 1 
   