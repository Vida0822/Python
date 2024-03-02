# 입력
N = int(input())
K = int(input())
ingredients = list(map(int, input().split()))

# 각 재료별 남은갯수 
ingredient_left = {} 
for ingredient in ingredients : 
    ingredient_left[ingredient] = ingredient_left.get(ingredient, 0) + 1

# 만들 수 있는 음료 개수 
drinks = 0
for ingredient in ingredients :
    pair = K - ingredient 
    if pair in ingredient_left : 
        used_count = min(ingredient_left[ingredient], ingredient_left[pair])
        drinks += used_count
        
        if ingredient_left.get(ingredient) - used_count <= 0 : 
            del ingredient_left[ingredient]        
        if ingredient_left.get(pair) - used_count <= 0 : 
            del ingredient_left[pair] 

# 음료 갯수 출력
print(drinks)
