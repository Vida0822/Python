S = input()
result = [] 
value = 0 

for c in S:
    if c.isalpha() : 
        result.append(c) 
    else: 
        value += int(c)

result.sort() 

if value != 0:
    result.append(str(value))

print(''.join(result))






