# 입력
A, B, C, X, Y = map(int, input().split())

# 후라이드, 양념치킨만 구입
option1 = A * X + B * Y 

# 반반 치킨 구입
possible_count = min(X,Y) 
option2 = 2 * C * possible_count+ A * max(0, X- possible_count) + B * max(0 , Y-possible_count) 

# 더 비용이 적은 선택지 출력
print(min(option1, option2))
