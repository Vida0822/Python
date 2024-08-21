# ==========================================
# Floydwarshall 알고리즘 : 모든 노드에서 모든 노드로의 최단거리를 구하는 알고리즘 
# ==========================================
#  ㄴ 행렬 그래프 + 3중 반복문 --> O(V^3) 
#   --> N이 충분이 작을 때 사용
#  *** 단순 최단 거리 뿐 아니라 어딘가를 '거쳐가는 거리' 자체를 구할 때 굉장히 유용 
#  핵심 알고리즘 : DP --> 점화식을 사용해 최단거리를 bottom-up 방식으로 채워나감 


INF = int(1e9)

n = int(input()) # 노드 수 
m = int(input()) # 간선 수 

# [그래프 만들기]
graph = [[INF]*(n+1) for _ in range(n+1)] 
# [INF] * (n+1) = [INF, INF, INF, INF] --> 요소 넣어주기 
# x for (n+1) 
#       ↓
# [ [INF, INF, INF, INF]
#  [INF, INF, INF, INF]
#       ...             ] --> 가장 바깥 [] 로 묶어줌 : 각 배열을 요소로 
# => 길이가 정해진 '행렬'처럼 ! 

# vs ' graph = [[] for i in range(n+1)] '
# [], [], [], [], []  --> 빈 리스트 복제 
# [[], [], [], [], [] ] <-- 가장 바깥 []로 묶어줌 
# => 각각이 길이가 유동적인 '리스트'처럼 ! 


# 자기자신으로 가는 비용은 0으로 초기화 --> O(N^2)
for a in range(1, n+1) : 
    for b in range(1, n+1) : 
        if a==b : 
            graph[a][b] == 0 

# 간선 정보 반영 
for _ in range(m) : 
    a, b, c = map(int, input().split())
    # a에서 b로 가는 비용이 c 
    graph[a][b] = c 
    # vs dijkstra : graph[a].append(c, b)



# [알고리즘 수행] : 점화식 --> O(N^3)
for k in range(1, n+1) :  # k : 거쳐갈 노드 (passing point)
    for a in range (1, n+1) :  # 출발지
        for b in range(1, n+1) :  # 도착지 

            graph[a][b] = min(graph[a][b] ,graph[a][k] + graph[k][b] ) 
#            *** 개념 이해 중요 
#              a -> b의 최단거리를 현재까지 구한 a->b 최단거리와 k를 거쳐갈때의 거리를 비교해 작은 값으로 갱신 
#              ※ 만들어준 graph 에 그대로 적용하는 것이 특징 ! 


    

