class Ssafy: #클래스 정의
    region = '부울경' # 클래스 변수
    name = '' # 클래스 변수
    def __init__(self,name,region): # 매직 메서드
        self.name = name # 인스턴스 변수
        self.region = region # 인스턴스 변수

    def talk(self): # 인스턴스 메서드
        print(f'{self.region}의 {self.name}는 피곤해!!!')

    @classmethod # 클래스메서드
    def good(cls):
        print(f'{cls.region}은 좋다.')
    
    @staticmethod # 스테틱메서드
    def check_tired(tired):
        return tired > 10

person_1 = Ssafy('김싸피','울산') #인스턴스 생성(person_1은 Ssafy의 인스턴스다.)
print(Ssafy.name) # 
print(Ssafy.region) # 부울경
print(person_1.name) # 김싸피
print(person_1.region) # 울산
person_1.talk() # 메서드 호출
# 울산의 김싸피 피곤해!!!
person_1.good() # 인스턴스는 클래스 메서드,인스턴스 메서드 둘 다 접근가능
# 부울경은 좋다.
Ssafy.good()
# 부울경은 좋다.
# Ssafy.talk() # 오류발생 클래스는 인스턴스 메서드 사용 불가능
print(Ssafy.check_tired(20)) # True
print(person_1.check_tired(20)) # True