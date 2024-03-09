import heapq 
import sys
input = sys.stdin.readline 
INF = int(1e9)

# 노드 개수, 간선 개수 입력
n, m = map(int, input().split()) 

# 시작 노드 입력
start = int(input()) 

# 그래프 선언 
graph = [[] for i in range(n+1)]

# 최단 거리 테이블 초기화 
distance = [INF] * (n+1)

# 간선 정보 입력 (그래프 구성)
for _ in range(m):
    a, b, c = map(int,input.split()) 
    # a번 노드에서 b번 노드로 가는 비용이 c (튜플 사용 )
    graph[a].append((b,c))  

def dijkstra(start):
    q = [] 

    # 시작 노드로 가기 위한 최단 경로는 0으로 설정해 큐에 삽입 
    heapq.heappush(q, (0, start))
    distance[start] = 0 
    while q: 
        dist , now = heapq.heappop(q) 

        if distance[now] < dist : 
            continue 

        # 인접 노드 방문 
        for i in graph[now] : 
            cost = dist + i[1] # 튜플 중 두번째 요소 꺼내기 
            if cost < distance[i[0]]:
                distance[i[0]] = cost 
                heapq.heappush(q, (cost,i[0]))

dijkstra(start)

for i in range(1, n+1): 
    if distance[i] == INF : 
        print("INFINITY")
    else :
        print(distance[i]) 
        
