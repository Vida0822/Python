def find_parent(parent,x):
    if parent[x] != x : 
        parent[x] = find_parent(parent,parent[x]) 
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if(a < b):
        parent[b] = a 
    else : 
        parent[a] = b 


v , e = map(int,input().split())
parent = [0]*(v+1)

edges = [] # 튜플 배열 
result = 0 

for i in range(1, v+1):
    parent[i] = i 

for _ in range(e): 
    a,b,cost = map(int,input().split())
    edges.append((cost,a,b)) # 튜플 

edges.sort() # 간선 비용순 정렬 (튜플의 첫번째 원소가 기준)

for edge in edges:
    cost, a, b = edge  # 튜플의 각각의 원소를 변수에 담음 
    if find_parent(parent, a) != find_parent(parent,b):
        union_parent(parent, a, b)
        result += cost 
print(result)



    