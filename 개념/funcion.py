def add(a,b):
    return a+b

print(add(3,7)) 

def add(a, b) : 
    print('함수의 결과 : ', a+b) 
add(3,7)
add(b = 3 , a = 7)

# 글로벌 변수 
a = 0 

def func():
    global a 
    a += 1 
for i in range(10):
    func()
print(a) 

result = (lambda a, b : a+b)(3,7) 
print(result) 
