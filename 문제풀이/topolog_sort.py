from collections import deque

v, e = map(int, input().split())

indegree = [0]*(v+1)

graph = [[] for i in range(v+1)]

for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b) 
    indegree[b] += 1

def topology_sort():
    result = []
    q = deque() 

    for i in range(1,v+1) : #노드들 검사 
        if indegree[i] == 0:
            q.append(i)
    
    while q: # 큐가 비지 않았으면 (존재하면)
        now = q.popleft()
        result.append(now)

        for i in graph[now] :  # 해당 노드와 연결된 노드들 하나씩 가져와서 
            indegree[i] -= 1
            if indegree[i] == 0 : 
                q.append(i)
            
        for i in result : 
            print(i, end = ' ')

topology_sort()



