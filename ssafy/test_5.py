# list_num=list(range(1,1001))
# print(list_num)
# list_2=[]
# list_7=[]
# list_14=[]
# for i in range(len(list_num)):
#     if list_num[i] % 2 ==0:
#         list_2.append(list_num[i])
# for j in range(len(list_num)):
#     if list_num[j] % 7 == 0:
#         list_7.append(list_num[j])
# for k in range(len(list_num)):
#     if list_num[k] % 7 == 0 and list_num[k] % 2 ==0:
#         list_14.append(list_num[k]) 
# sum_2=sum(list_2)
# sum_7=sum(list_7)
# sum_14=sum(list_14)
# print(sum_2+sum_7-sum_14)
###########################
# m = 5
# n = 4
# list_star=[[0]*n for _ in range(m)]
# for i in range(m):
#     for j in range(n):
#         if i == 0:
#             list_star[i][j] = '*'
#         elif i == m-1:
#             list_star[i][j] = '*'
#         else:
#             if j == 0 or j == n-1:
#                 list_star[i][j] = '*'
# for k in range(len(list_star)):
#     print(*list_star[k])
###################################
# a = 3
# b = 6
# c = -5
# gen=(round((-b+(b**2-7*a*c)**0.5)/2/a,4),round((-b-(b**2-7*a*c)**0.5)/2/a,4))
# print(gen)
####################
# a=str('<p>취업 준비생에게 SW 역량 향상 교육 및 다양한 취업지원 서비스를 제공하여 취업에 성공하도록 돕는 프로그램입니다.</p>')
# print(a[3:66])
############################
# str_lst = input('문자열을 입력하세요. : ')
# a = str_lst.lower().split()
# if a[0][len(a[0])-1] == a[1][0]:
#     if a[1][len(a[1])-1] == a[2][0]:
#         print('Pass')
#     else:
#         print('Fail')
# else:
#     print('Fail')
    #############
# a=50000
# b=a*0.15
# c=a+b
# print('스테이크   '+str(a)+'\n'+'+VAT     '+str(b)+'\n'+'총계₩    '+str(c))
#########################
# todo = [("Python Homework", 3), ("Assay", 4), ("Vacation", 100)]
# work=str(input())
# d_day=int(input())
# todo.append((work,d_day))
# print(todo)
#################
# orders = '아이스아메리카노,카라멜마키야또,에스프레소,아메리카노,아메리카노,아이스라떼,핫초코,아이스아메리카노,아메리카노,아이스카라멜마키야또,아이스라떼,라떼마키야또,카푸치노,라떼마키야또'
# print(len(orders.split(',')))
# a=sorted(list(set(orders.split(','))),reverse=True)
# print(a)
#####################
# orders = '아이스아메리카노,카라멜마키야또,에스프레소,아메리카노,아메리카노,아이스라떼,핫초코,아이스아메리카노,아메리카노,아이스카라멜마키야또,아이스라떼,라떼마키야또,카푸치노,라떼마키야또'
# mod_orders=orders.split(',')
# cnt=0
# for i in range(len(mod_orders)):
#     ice = mod_orders[i].count('아이스')
#     if ice>0:
#         cnt+=1
# print(cnt)

# a=list(set(orders.split(',')))
# list_1=[]

# for j in a:
#     cnt=0
#     for k in range(len(mod_orders)):
#         if j == mod_orders[k]:
#             cnt+=1
#     list_1.append((j,cnt))
    
# for k in range(len(list_1)):
#     print(*list_1[k])
    ########################
# print(dir(str))
# fruit=str(input())
# fruit_list=list(fruit.lower().split(','))
# for i in range(len(fruit_list)):
#     if str(fruit_list[i]).find('rotten') == -1:
#         pass
#     else:
#         fruit_list[i]=str(fruit_list[i]).replace('rotten','')
#         print(fruit_list[i])
# print(fruit_list)
#############################
# alp=str(input())
# if len(alp)%2 == 0:
#     print(alp[len(alp)//2-1],alp[len(alp)//2])
# else:
#     print(alp[len(alp)//2])
######################################
class Ssafy: #클래스 정의
    region = '부울경' # 클래스 변수
    name = '_' # 클래스 변수
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

person_1 = Ssafy('김싸피','울산') #인스턴스 생성
print(Ssafy.name) # _
print(Ssafy.region) # 부울경
print(person_1.name) # 김싸피
print(person_1.region) # 울산
person_1.talk() # 메서드 호출
# 김싸피 피곤해!!!
person_1.good() # 인스턴스는 클래스 메서드,인스턴스 메서드 둘 다 접근가능
# 부울경은 좋다.
Ssafy.good()
# 부울경은 좋다.
#Ssafy.talk() # 오류발생 클래스는 인스턴스 메서드 사용 불가능
print(Ssafy.check_tired(20)) # True
print(person_1.check_tired(20)) # True
