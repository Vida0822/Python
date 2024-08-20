# ===================================================
#   Dijkstra 알고리즘 
# : 한 노드에서 다른 노드들로의 최단거리를 구할 수 있다. 
# ===================================================
# 핵심 원리 : 가장 비용이 적은 노드를 매번 선택하는 '그리디' 알고리즘 

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
    # a번 노드에서 c번 노드로 가는 비용이 b (튜플 사용)
    graph[a].append((b,c))  

def dijkstra(start):
    q = [] 

    # 시작 노드로 가기 위한 최단 경로는 0으로 설정해 큐에 삽입 
    heapq.heappush(q, (0, start))

    # 시작 노드까지의 거리는 0 
    distance[start] = 0 

    while q: 
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기 
        # heapq는 튜플의 첫 번째 항목을 기준으로 우선순위를 가진다. 
        dist , next = heapq.heappop(q) 

        # 지금 노드를 거쳐가는 것이 해당 노드까지의 최단 거리보다 짧을 땐 이동X    
        if distance[next] < dist : 
            continue 

        # else : 이동 

        # 해당 노드의 인접 노드 방문 
        for i in graph[next] : 
            cost = dist + i[0] # 튜플 중 두번째 요소 꺼내기 
            if cost < distance[i[1]]: # 인접 노드까지가는 다른 경로보다 next 노드를 거치는게 더 좋으면 
                distance[i[1]] = cost  # 최단 거리 갱신 
                heapq.heappush(q, (cost,i[1])) # 해당 노드 기준 release 

dijkstra(start)

for i in range(1, n+1): 
    if distance[i] == INF : 
        print("INFINITY")
    else :
        print(distance[i]) 

# Dijkstra 시간 복잡도 
# O(E log V) - E : 간선 수, V : 정점 수 
# 1. 간선은 최대 한번만 검사되기 때문에 최악의 경우 총 간선수 E만큼 검사한다.  : O(E)
# 2. 최악의 경우 모든 간선을 우선 순위 큐에 넣고 뺀다.  : log(E)
# E의 최댓값은 모든 노드가 연결된 경우인 Vx(V-1), 즉 V^2이기 때문에 
# O(log E)의 최악의 경우는 O(log V^2) = O(2xlog V) = O(log V) 이다. 
# 따라서 O(E log E)의 최악의 경우는 O(E log V)로 볼 수 있다. 