INF = int(1e9)

n = int(input()) 
m = int(input()) 

graph = [[INF]*(n+1) for _ in range(n+1)]

# 자기자신에서 자기자신으로 가는 비용은 0으로 초기화 
for a in range(1, n+1):
    for b in range(1, n+1) : 
        if a == b : 
            graph[a][b] = 0 

# 각 간선에 대한 정보를 입력받아 초기화 
for _ in range(m):
    a, b, c = map(int, input().split()) 
    graph[a][b] = c 

# 점화식 (플로이드 워셜 알고리즘 수행)
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b] , graph[a][k]+ graph[k][b])

