
# 0 : 빈칸, 1 : 벽, 2 : 바이러스 
# n,m <= 8 --> 엄청 작음 (시간 복잡도 생각X)

import sys 
f = sys.stdin.readline

n,m = map(int,f().split())
lab = []

for _ in range(n):
    lab.append(list(map(int, f().split())))
cop_lab = [[0] * m for _ in range(n)]
l = 0 

# 1) 바이러스 퍼트리기 --> dfs 
def virus(x, y) : 

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(4) :
        nx = x + dx[i] 
        ny = y + dy[i] 

        if nx < 0 or nx >= n or ny < 0 or ny >= m : 
            continue
        if cop_lab[nx][ny] == 0 :
            cop_lab[nx][ny] = 2 
            virus(nx, ny)
    return 


# 2) 안전 영역 크기 계산 : 선형 탐색 하면서 갯수 count 
def safe_zones(cop_lab):   
    count = 0 
    for i in range(n) : 
        for j in range(m):
            if cop_lab[i][j] == 0 : 
                count+=1
    return count 



# 3) 연구소 벽 건립 : 전체 0 중에 3개 설립 --> dfs (모든 조합, 넣다 뺏다 기법)
def build_walls(count) :
    global l 

    if count == 3 :
        global cop_lab
        for i in range(n) : 
            for j in range(m) : 
                cop_lab[i][j] = lab[i][j]

        for i in range(n) : 
            for j in range(m) : 
                if cop_lab[i][j] == 2 : 
                    virus(i, j)
        l = max(l,safe_zones(cop_lab))  
        return 

    for i in range(n):
        for j in range(m) : 
            if lab[i][j] == 0 : 
                lab[i][j] = 1 
                count += 1 
                build_walls(count)
                lab[i][j] = 0   
                count -= 1    
    return

# main
build_walls(0)
print(l)
