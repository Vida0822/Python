class Member:
    
    value = [] # 클래스 변수 -> 모든 인스턴스에서 공유! 

    def __init__(self, name, age, address, money):
        self.name = name # 멤버변수 선언을 생성자 선언과 함께한다  
        self.age = age  # 즉, 인스턴스 속성 
        self.address = address 
        self.__money = money

    def info(self):
        print('저의 이름은 {0}이고, 나이는 {1}, 사는 곳은 {2}입니다'.format(self.name, self.age,self.address))

    def deposit(self, plus):
        print('입금 후 총 통장 금액은 {0}원 입니다'.format(self.__money))
            