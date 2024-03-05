for ic in range(int(input())):  # 테스트 케이스 입력 받은만큼 반복 
    n , m = map(int, input().split())
    array = list(map(int, input().split())) # n*m개 금 리스트 + 초기화 

    # n행 m열 2차원 배열 
    dp = [] 
    index = 0 
    for i in range(n) : # 총 n개 요소로 구성 -> 2차원 배열 
        dp.append(array[index:index+m]) # m개씩 잘라서 (m열) -> 1차원 배열 
        index += m 

    # dp 실행 
    for j in range(1, m):  # 두번째 행부터 
        for i in range(n) : 

            # 맨 윗행 초기화 하는 경우 
            if i == 0 : 
                left_up = 0 
            else :
                left_up = dp[i-1][j-1] 

            # 맨 아랫행 초기화 하는 경우 
            if i == n-1 : 
                left_down = 0 
            else : 
                left_down = dp[i+1][j-1]
            
            left = dp[i][j-1] 

            # 점화식
            dp[i][j] = dp[i][j] + max(left_up, left, left_down) 

    result = 0 
    for i in range(n):
        result = max(result, dp[i][m-1])
    print(result)
    
            



