y = [10,20,30]

try:
    index, x = map(int, input('인덱스와 나눌 숫자를 입력하세요').split())
    # map() : 지정된 함수 (int 함수)를 입력받은 값들(리스트) 각각에 적용 
    #       <-> 리스트의 각 부분 문자열을 int 자료형으로 변환
    # => 그렇게 int 형으로 변환된 값을 각각 index,x에 담기
    print(y[index]/x)
except ZeroDivisionError: 
    # 숫자를 0으로 나눠서 에러가 발생
    print('숫자를 0으로 나눌 수 없습니다')
except IndexError as e: # as 뒤에 변수를 지정하면 발생한 예외의 에러메세지를 받아올 수 있다.
     # 범위를 벗어난 인덱스에 접근
    print('잘못된 인덱스입니다.', e)
finally:
    print('어쨌든 코드는 끝났습니다')
    