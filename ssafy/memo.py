# list_mil=list(range(1,10001))
# def self_num(n):
#     while n < 10000:
#         list_num=[]
#         sum = 0
#         len_num = 0
#         for i in range(len(str(n))):
#             len_num += int(str(n)[i])
#             sum = n + len_num
#             if sum <= 10000:
#                 n = sum
#             else:
#                 pass
#         list_num.append(n)
#     return list_num

# # self_num(1)
# # self_num(3)
# # self_num(5)
# # self_num(7)
# # self_num(9)

# print(self_num(1))
# infos = [{'name': 'kim', 'age': 12}, {'name': 'lee', 'age': 4}]
# sum=0
# for i in range(len(infos)):
#     sum+=infos[i]['age']
# print(sum)
# ##########################
# blood_types = [ 'A','A','O', 'B', 'A', 'O', 'AB','O', 'A', 'B', 'O', 'B', 'AB']
# blood_list = ['A','B','O','AB']
# a = []
# for i in blood_list:
#     cnt=0
#     for j in range(len(blood_types)):
#         if i ==blood_types[j]:
#             cnt+=1
#         else:
#             pass
#     a.append(cnt)
# blood_dict={}
# for k in range(4):
#     blood_dict[blood_list[k]] = a[k]
# print(blood_dict)
#####################
# num=int(input())
# salt_sum=0
# water_sum=0
# for i in range(num):
#     a,b=map(int,input().split())
#     salt_sum+=a*b/100
#     water_sum+=b
# print(round(salt_sum/water_sum,2))
####################################
# year=int(input())
# if (year % 4 == 0 and year % 100 !=0) or year % 400 == 0:
#     print('윤년')
# else:
#     print('no')
###############
# s_triangle = str(input())
# a = int(s_triangle[0])
# b = int(s_triangle[1])
# c = int(s_triangle[2])
# if a == b and b == c:
#     print('정삼각형')
# elif (a==b and a+b>c) or (b==c and b+c>a) or (c==a and c+a>b):
#     print('이등변삼각형')
# elif a**2+b**2==c**2 or c**2+b**2==a**2 or a**2+c**2==b**2:
#     print('직각삼각형')
# elif c>=a+b or b>=a+c or a>=b+c:
#     print('삼각형 아님')
# else:
#     print('삼각형')
#####################################
# import calendar
# year=int(input())
# while calendar.isleap(year) :
#     print('윤년입니다. 연도를 다시 입력해주세요.')
#     year=int(input())
# else:
#     print(calendar.calendar(year))
# month=int(input())
# day=int(input())
# day_list=['월요일','화요일','수요일','목요일','금요일','토요일','일요일']
# if day_list[calendar.weekday(year,month,day)] == '월요일':
#     print(f'경고 {day_list[calendar.weekday(year,month,day)]}입니다.')
# dict_a={'년':year,'월':month,'일':day,'요일':day_list[calendar.weekday(year,month,day)]}
# print(dict_a)
######################
# def fn_d(n):
#     num=str(n)
#     sum=int(n)
#     for i in range(len(num)):
#         sum+=int(num[i])
#     return sum
# num=list(range(1,10000))
# a=[]
# for i in range(1,len(num)):
#     fn_d(i)
#     a.append(fn_d(i))
# for i in list(set(a)):
#     for j in range(len(a)):
#         if i == a[j]:
#             (i)
# print(a)
######################
# id='1234561234567'
# def de_identify(id):
#     return id[:6]+'*******'
# print(de_identify('970103-1234567'))
# print(de_identify('8611232345678'))

# t=int(input())
# for test_case in range(1, t+1):
#     num = int(input())
#     list_num = list(map(int, input().split()))
#     for i in range(num-1,0,-1):
#         for j in range(i):
#             if list_num[j]>list_num[j+1]:
#                 list_num[j],list_num[j+1]=list_num[j+1],list_num[j]
#         max_min = list_num[len(list_num) - 1] - list_num[0]
#     print(f'#{test_case} {max_min}')
#####################
# T=int(input())
# for tc in range(1,T+1):
#     n,m=map(int,input().split())
#     a=list(map(int,input().split()))
#     s=[]
#     for i in range(n-m+1):
#         sum=0
#         for j in range(m):
#             sum += a[i+j]
#         s.append(sum)
#     div=max(s)-min(s)
#     print(f'#{tc} {div}')
###################
# T = int(input())
# for tc in range(1, T + 1):
#     n=int(input())
#     h=list(map(int,input().split()))
#     list_cnt=[]
#     for i in range(n):
#         cnt = 0
#         for j in range(1, n-i):
#             if h[i]>h[j+i]:
#                  cnt += 1
#         list_cnt.append(cnt)
#     max=0
#     for j in list_cnt:
#         if j > max:
#             max=j
#     print(f'#{tc} {max}')
    ############################
# grain_lst = [('고구마',3000), ('감자',2000), ('옥수수',4500),('토란',1300)]
# max=grain_lst[0][1]
# n=0
# for i in range(len(grain_lst)):
#     if grain_lst[i][1]>max:
#         max=grain_lst[i][1]
#         n=i
# print(grain_lst[n][0])
###############################
# def count_vowels(alp):
#     list_vow=['a','w','e','y','u','i','o']
#     cnt=0
#     alp=','.join(alp)
#     a=alp.split(',')
#     for i in list_vow:
#         cnt += a.count(i)
#     print(cnt)
# count_vowels('apple')
# count_vowels('bananaananananana')
############################
# from collections import Counter
# entry_record = ['이싸피', '박장고', '조실습', '이싸피', '조실습', '오디비', '임온실', '조실습', '조실습', '이싸피', '안도둑', '임온실', '최이썬', '오디비', '안도둑', '염자바', '박장고', '조실습',
#                 '최이썬', '조실습', '염자바', '박장고', '임온실', '임온실', '이싸피', '임온실', '오디비', '조실습', '염자바', '임온실', '박장고', '최이썬', '안도둑', '염자바', '임온실', '박장고', '이싸피', '안도둑',
#                 '임온실', '오디비', '최이썬', '안도둑', '이싸피', '오디비', '안도둑', '이싸피', '박장고', '박장고', '안도둑', '안도둑', '안도둑', '염자바', '최이썬', '오디비', '오디비', '최이썬', '이싸피', '임온실', '안도둑']

# exit_record = ['최이썬', '조실습', '이싸피', '안도둑', '임온실', '안도둑', '이싸피', '오디비', '염자바', '박장고', '최이썬', '이싸피', '염자바', '염자바', '박장고', '임온실', '이싸피',
#                '박장고', '안도둑', '염자바', '이싸피', '조실습', '조실습', '임온실', '박장고', '이싸피', '조실습', '박장고', '오디비', '안도둑', '조실습', '임온실', '안도둑', '안도둑', '임온실', '조실습', '최이썬', '안도둑', '임온실',
#                '염자바', '이싸피', '임온실', '안도둑', '오디비', '안도둑', '오디비', '임온실', '염자바', '임온실', '박장고', '조실습', '이싸피', '최이썬', '최이썬', '오디비', '오디비', '염자바', '오디비', '안도둑', '박장고']
# print('입장 기록 많은 Top3')
# for i in Counter(entry_record).most_common(3):
#     print(f'{i[0]} {i[1]}회')
# c1=Counter(entry_record)
# c2=Counter(exit_record)
# entry_more=c1-c2
# exit_more=c2-c1
# print(exit_more.most_common()[0][1])
# print('출입 기록이 수상한 사람')
# print(f'{entry_more.most_common()[0][0]}은 입장 기록이 {entry_more.most_common()[0][1]}회 더 많아 수상합니다.')
# print(f'{exit_more.most_common()[0][0]}은 퇴장 기록이 {exit_more.most_common()[0][1]}회 더 많아 수상합니다.')
###################
# list_a=[]
# n=0
# while True:
#     n+=1
#     alp=str(input(f'{n}. 소금물의 농도(%)와 소금물의 양(g)을 입력하시오:'))
#     if alp == 'Done':
#         break
#     else:
#         a=int(alp[0])*0.01
#         b=int(alp[3:-1])
#         list_a.append([a,b])
# water_sum=0
# salt_sum=0
# for i in range(len(list_a)):
#     salt_sum+=list_a[i][0]*list_a[i][1]
#     water_sum+=list_a[i][1]

# print(f'{salt_sum/water_sum*100}% {water_sum}g')
###############################
# for t in range(10):
#     n=int(input())
#     a=list(map(int,input().split()))
#     sum=0
#     for i in range(2,n-2):
#         if a[i]>a[i+1] and a[i]>a[i+2] and a[i]>a[i-1] and a[i]>a[i-2]:
#             b=[a[i+1],a[i+2],a[i-1],a[i-2]]
#             sum+=a[i]-max(b)
#     print(f'#{t+1} {sum}')
####################
# import random
# class ClassHelper:
#     def __init__(self,list):
#         self.list=list
#     def pick(n):
#         return random.choice(n)
#     def match_pair(self):
#         self.list
#         if len(self.list) % 2 == 1:
#             a=random.choice(self.list)
#             self.list.remove(a)
#             b=random.choice(self.list)
#             self.list.remove(b)
#             c=random.choice(self.list)
#             self.list.remove(c)
#         else:
#             a=random.choice(self.list)
#             self.list.remove(a)
#             b=random.choice(self.list)
#             self.list.remove(b)        
    
# ch = ClassHelper(['김해피', '이해킹', '조민지', '박영수', '정민수'])

# print(ch.pick(1))
# print(ch.pick(1))
# print(ch.pick(2))
# print(ch.pick(3))
# print(ch.pick(4))

# print(ch.match_pair())
######################################
# T=int(input())
# for t in range(T):
#     num=int(input())
#     num_list=list(map(int,input()))
#     cnt=[0]*10
#     for i in num_list:
#         cnt[i]+=1
#     max_cnt=0
#     for j in range(len(cnt)):
#         if max_cnt <= cnt[j]:
#             n=j
#             max_cnt=cnt[j]
#     print(f'#{t+1} {n} {max_cnt}')
##############################
# T=int(input())
# for t in range(1,T+1):
#     k,n,m=map(int,input().split())
#     num_list=list(map(int,input().split()))
#     cnt=[0]*(n+3)
#     for i in num_list:
#         cnt[i]+=1
#     num=0
#     cnt=''.join(str(_) for _ in cnt)
#     print(cnt)
#     print(cnt[1:4])
#     i=1
#     while i<n:
#         if cnt[i:i+k+1] == '000':
#             num=0
#             continue
#         elif cnt[i+1:i+k+1] == '1':
#             num+=1
#             i = i+1
#             continue
#         elif cnt[i+2:i+k+1] == '1':
#             i = i+2
#             num+=1
#             continue
        
#         print(num)
# T=int(input())
# for t in range(1,T+1):
#     k,n,m=map(int,input().split())
#     num_list=list(map(int,input().split()))
#     cnt=[0]*(n+1)
#     for x in num_list:
#         cnt[x]+=1
#     num=0
#     i=0
#     while True:
#         a=[]
#         if i+k>=n:
#             print(f'#{t} {num}')
#             break
#         for j in range(1,k+1):
#             if cnt[i+j]==1:
#                 a.append(i+j)
#         if len(a)==0:
#             num=0
#             print(f'#{t} {num}')
#             break
#         else:
#             num+=1
#             i=max(a)
##########################
# for i in range(10):
#     num=int(input())
#     num_list=list(map(int,input().split()))
#     cnt=[0]*(max(num_list)+1)
#     for j in num_list:
#         cnt[j]+=1
#     n=0
#     k=1
#     m1=1
#     while n<=num:
#         if cnt[k]>0:
#             cnt[k]-=1
#             cnt[k+1]+=1
#             n+=1
#         else:
#             k+=1
#             m1+=1
#     m2=max(num_list)
#     l=1
#     m=0
#     x=len(cnt)
#     while m<=num:
#         if cnt[x-l]>0:
#             cnt[x-l]-=1
#             cnt[x-l-1]+=1
#             m+=1
#         else:
#             l+=1
#             m2-=1
#     print(f'#{i+1} {m2-m1}')
# for i in range(10):
#     num=int(input())
#     num_list=list(map(int,input().split()))
#     cnt=[0]*(max(num_list)+1)
#     for j in num_list:
#         cnt[j]+=1
#     n=0
#     k=1
#     m1=1
#     x=len(cnt)
#     m2=max(num_list)
#     l=1
#     m=0
#     while n<num and m<num:
#         if cnt[k]>0:
#             cnt[k]-=1
#             cnt[k+1]+=1
#             n+=1
#         else:
#             k+=1
#             m1+=1
        
#         if cnt[x-l]>0:
#             cnt[x-l]-=1
#             cnt[x-l-1]+=1
#             m+=1
#         else:
#             l+=1
#             m2-=1
#         if m1-m2==0 or m1-m2==1:
#             break
#     print(f'#{i+1} {m2-m1}')
# class Doggy:
#     num_of_dogs = 0
#     birth_of_dogs=0
#     def __init__(self,name,spiece):
#         self.name = name
#         self.spiece = spiece
#         Doggy.num_of_dogs += 1
#         Doggy.birth_of_dogs += 1

#     def bark(self):
#         print('왈왈')

#     @classmethod
#     def get_status(cls):
#         print(f'num_of_dogs:{cls.num_of_dogs} birth_of_dogs:{cls.birth_of_dogs}')
#     def kill(self):
#         print('강아지가 죽었습니다.')
#         Doggy.num_of_dogs-=1

# d1=Doggy('바둑이','똥개')
# d2=Doggy('바둑이','똥개')
# d1.bark()
# d1.kill()
# d1.get_status()
###########################
# participants =  [3, 7, 100, 21, 13, 6, 5, 7, 5, 6, 3, 13, 21]
# cnt=[0]*(max(participants)+1)
# for i in participants:
#     cnt[i]+=1
# for j in range(len(cnt)):
#     if cnt[j]==1:
#         print(j)
#################
# class PublicTransport:
#     cnt=0
#     def __init__(self,name,fare):
#         self.name=name
#         self.fare=fare
        
#     def get_in():
#         PublicTransport.cnt+=1
#     def get_off():
#         PublicTransport.cnt-=1
    
#     def profit():
#         return PublicTransport.cnt*PublicTransport.fare
# class Bus(PublicTransport):
#     limit=0
#     def __init__(self, name, fare):
#         super().__init__(name, fare)
#     def get_in():
#         if PublicTransport.cnt>Bus.limit:
#             print('더이상 탑승할 수 없습니다.')
###########################
# T=int(input())
# for t in range(T):
#     num=int(input())
#     a=0
#     b=0
#     c=0
#     d=0
#     e=0
#     while True:
#         if num%2 == 0:
#             a+=1
#             num=num/2
#         else:
#             break
#     while True:
#         if num%3==0:
#             b+=1
#             num=num/3
#         else:
#             break
#     while True:
#         if num%5==0:
#             c+=1
#             num=num/5
#         else:
#             break
#     while True:
#         if num%7==0:
#             d+=1
#             num=num/7
#         else:
#             break
#     while True:
#         if num%11==0:
#             e+=1
#             num=num/11
#         else:
#             break
#     print(f'#{t+1} {a} {b} {c} {d} {e}')
############################
# T=int(input())
# for t in range(T):
#     num=int(input())
#     list_num=list(map(int,input()))
#     b=[]
#     n=0
#     cnt=0
#     while n<num:
#         if list_num[n] == 1:
#             cnt+=1
#             if n == num-1:
#                 b.append(cnt)
#         else:
#             b.append(cnt)
#             cnt=0
#         n+=1
#     print(f'#{t+1} {max(b)}')
##################################
# T=int(input())
# for t in range(T):
#     num=int(input())
#     list_num=list(map(int,input().split()))
#     n=0
#     cnt=1
#     b=[]
#     while n<num-1:
#         if list_num[n]<list_num[n+1]:
#             cnt+=1
#             if n==num-2:
#                 b.append(cnt)
#         else:
#             b.append(cnt)
#             cnt=1
#         n+=1
#     if max(b) == 1:
#         print(f'#{t+1} 1')
#     else:
#         print(f'#{t+1} {max(b)}')
#######################################
# T=int(input())
# for t in range(T):
#     num=int(input())
#     cnt=[0]*1001
#     for i in range(num):
#         a=list(map(int,input().split()))
#         if a[0]==1:
#             for j in range(a[1],a[2]+1):
#                 cnt[j]+=1
#         elif a[0]==2:
#             if a[1]%2 == 0:
#                 for k in list(range(a[1],a[2]+1)):
#                     if k%2 == 0:
#                         cnt[k]+=1
#             else:
#                 for l in list(range(a[1],a[2]+1)):
#                     if l%2 == 1:
#                         cnt[l]+=1
#         elif a[0]==3:
#             if a[1]%2 == 0:
#                 for k in list(range(a[1],a[2]+1)):
#                     if k%4 == 0:
#                         cnt[k]+=1
#             else:
#                 for l in list(range(a[1],a[2]+1)):
#                     if l%3 == 0 and l%10 != 0:
#                         cnt[l]+=1 
#     print(f'#{t+1} {max(cnt)}')
#########################################
# import random
# class ClassHelper:
#     def __init__(self,list):
#         self.list=list
#     def pick(self, n):
#         return random.sample(self.list,n)
#     def match_pair(self):
#         self.list
#         b=[]
#         a=[]
#         while len(self.list)>0:
#             if len(self.list) % 2 == 1:
#                 a=random.sample(self.list,3)
#                 b.append(a)
#                 self.list.remove(a[0])
#                 self.list.remove(a[1])
#                 self.list.remove(a[2])
#             else:
#                 a=random.sample(self.list,2)
#                 b.append(a)
#                 self.list.remove(a[0])
#                 self.list.remove(a[1])
#         return b

# ch = ClassHelper(['김해피', '이해킹', '조민지', '박영수', '정민수'])

# print(ch.pick(1))
# print(ch.pick(1))
# print(ch.pick(2))
# print(ch.pick(3))
# print(ch.pick(4))
# print(ch.match_pair())
##############################
# def collatz(n):
#     cnt=0
#     while n!=1:
#         if n%2 == 0:
#             n=n/2
#         elif n%2 == 1:
#             n=n*3+1
#         cnt+=1
#     if cnt >= 500:
#         print(-1)
#     else:
#         print(cnt)
# collatz(6) #=> 8
# collatz(16) #=> 4
# collatz(27) #=> 111
# collatz(626331)
#################
# num=int(input())
# cnt=1
# sum=1
# n=0
# while num>sum:
#     n+=6
#     sum+=n
#     cnt+=1
# print(cnt)
##################
# def hanoi(n,a,b,c):
#     if n == 1:
#         print(a,"->",b)
#     else:
#         hanoi(n-1,a,c,b)
#         print(a,"->",b)
#         hanoi(n-1,c,b,a)    
# hanoi(3, 'A', 'C', 'B')
##########################
# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
        
#     @classmethod
#     def get_age(cls,name, year):
#         cls.name=name
#         cls.year = year
#         age = 2023 - cls.year
#         return Person(name,age)
        

#     def check_age(self):
#         if self.age>=18:
#             return True
#         else:
#             return False
# person1 = Person('Mark', 20)
# person2 = Person.get_age('Rohan', 1992)
# print(person1.name, person1.age) 
# print(person2.name, person2.age)
# print(person1.check_age())
# print(person2.check_age())
#########################
# class Point:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
# class Rectangle:
#     def __init__(self,p1,p2):
#         self.p1=p1
#         self.p2=p2
#     def get_area(self):
#         wid=self.p1.y-self.p2.y
#         hei=self.p2.x-self.p1.x
#         return wid*hei

#     def get_perimeter(self):
#         wid=self.p1.y-self.p2.y
#         hei=self.p2.x-self.p1.x
#         return 2*wid+2*hei

#     def is_square(self):
#         wid=self.p1.y-self.p2.y
#         hei=self.p2.x-self.p1.x
#         if wid == hei:
#             return True
#         else:
#             return False
# p1 = Point(1, 3)122
# p2 = Point(3, 1)
# r1 = Rectangle(p1, p2)
# print(r1.get_area())
# print(r1.get_perimeter())
# print(r1.is_square())

# p3 = Point(3, 7)
# p4 = Point(6, 4)
# r2 = Rectangle(p3, p4)
# print(r2.get_area())
# print(r2.get_perimeter())
# print(r2.is_square())
##################
# list_num=list(map(int,input()))
# cnt=[0]*(max(list_num)+1)
# a=[0]*(len(list_num))
# for i in list_num:
#     cnt[i]+=1
# for j in range(1,len(cnt)):
#     cnt[j] = cnt[j-1]+cnt[j]
# for k in list_num:
#     a[-(cnt[k])]=k
#     cnt[k]-=1
# for l in range(len(a)):
#     print(a[l],end='')
###########################
# num=int(input())
# a=[]
# b=[]
# num_list=[]
# for x in range(num):
#     num_list.append(int(input()))
# for i in num_list:
#     if i>=0:
#         a.append(i)
#     else:
#         b.append(abs(i))

# avg=(sum(a+b)/len(a+b))
# cnt_p=[0]*(max(a)+1)
# cnt_m=[0]*(max(b)+1)
# for j in a:
#     cnt_p[j]+=1
# for k in b:
#     cnt_m[k]+=1
# for j in range(1,len(cnt_m)):
#     cnt_m[j] = cnt_m[j-1]+cnt_m[j]
# for k in b:
#     cnt_m[-(cnt_m[k])]=k
#     cnt_m[k]-=1
# print(cnt_m)
# print(cnt_m+cnt_p)
###################
# T=int(input())
# cnt=[[[0] for _ in range(101)] for _ in range(101)]
# for t in range(T):
#     a,b=map(int,input().split())
#     for i in range(10):
#         for j in range(10):
#             cnt[101-b-i][a+j]=1
# sum=0
# for k in range(len(cnt)):
#     sum+=cnt[k].count(1)
# print(sum)
####################
# import sys
# T,n=map(int,sys.stdin.readline().split())
# num_list=list(map(int,sys.stdin.readline().split()))
# i=0
# a=[]
# for i in range(T-2):
#     a.append(sum(num_list[i:i+3]))
#     print(num_list[i:i+3])
#     i+=1
# print(a)
################
# import sys
# T,n=map(int,sys.stdin.readline().split())
# num_list=list(map(int,sys.stdin.readline().split()))
# a=[]
# for i in range(T):
#     for j in range(i+1,T):
#         for k in range(j+1,T):
#             sum=num_list[i]+num_list[j]+num_list[k]
#             a.append(sum)
# min=abs(n-a[0])
# for l in a:
#     if abs(n-l)<min and l<=n:
#         min=abs(n-l)
#         cnt=l
# print(cnt)
####################
# n=int(input())
# kg_list=(list(map(int,input().split())) for _ in range(n))
# for i in range(n-1):
#     kg_list[i][0]>
# arr=[3,6,7,1,5,4]
# n=len(arr)
# for i in range(1<<n):
# 	for j in range(n):
# 		if i&(1<<j):
# 			print(arr[j],end=", ")
# 	print()
# print()
########################
# T=int(input())
# for t in range(T):
#     a=[[0 for _ in range(10)] for _ in range(10)]
#     num=int(input())
#     list_a=[list(map(int,input().split())) for _ in range(num)]
#     for i in range(num):
#         for j in range(list_a[i][0],list_a[i][2]+1):
#             for k in range(list_a[i][1],list_a[i][3]+1):
#                 if a[k][j]!=0 and a[k][j] !=list_a[i][4] and a[k][j]<5:
#                     a[k][j]+=list_a[i][4]
#                 elif a[k][j] == 0 or a[k][j] ==list_a[i][4]:
#                     a[k][j]=list_a[i][4]
#     cnt=0
#     for p in range(10):
#         for o in range(10):
#             if a[p][o]>=3:
#                 cnt+=1
#     print(f'#{t+1} {cnt}')
##############################
# T=int(input())
# for t in range(T):
#     n=int(input())
#     a=list(map(int,input().split()))
#     for i in range(n-1):
#         for j in range(n-1-i):
#             if a[j]>a[j+1]:
#                 a[j],a[j+1]=a[j+1],a[j]
#     print(f'#{t+1} ',end='')
#     print(*a)
####################################
# T=10
# for t in range(T):
#     num=int(input())
#     list_num=[list(map(int,input().split())) for _ in range(num)]
#     sum=0
#     for i in range(num):
#         for j in range(num):
#             a=list_num[i][j]
#             for ni,nj in [[1,0],[-1,0],[0,1],[0,-1]]:
#                 if 0<=i+ni<num and 0<=j+nj<num:
#                     sum+=abs(a-list_num[i+ni][j+nj])
#     print(f'#{t+1} {sum}')
#####################################
# T=10
# for t in range(T):
#     n=int(input())
#     num_list=[list(map(int,input().split())) for _ in range(100)]
#     max=0
#     for i in range(100):
#         c=0
#         d=0
#         for j in range(100):
#             c+=num_list[i][j]
#             d+=num_list[j][i]
#         if c>max:
#             max=c
#         if d>max:
#             max=d
#     a=0
#     for p in range(100):
#         a+=num_list[p][p]
#     if a>max:
#         max=a
#     b=0
#     for o in range(100):
#         b+=num_list[o][99-o]
#     if b>max:
#         max=b
#     print(f'#{n} {max}')
#######################################
# a,b=map(int,input().split())
# alp_list=[list(map(str,input())) for _ in range(a)]
# count=[]
# c_alp_list=alp_list[::]
# print(c_alp_list)
# for k in range(a-7):
#     for l in range(b-7):
#         cnt=0
#         for i in range(8):
#             for j in range(8):
#                 for ni,nj in [[1,0],[-1,0],[0,1],[0,-1]]:
#                     if 0+k<=i+ni+k<a+k and 0+l<=j+nj+l<b+l:
#                         if c_alp_list[i+k][j+l] != c_alp_list[i+ni+k][j+nj+l]:
#                             pass
#                         else:
#                             cnt+=1
#                             if c_alp_list[i+k][j+l] == 'B':
#                                 c_alp_list[i+ni+k][j+nj+l]='W'
#                             else:
#                                 c_alp_list[i+ni+k][j+nj+l]='B'
#         count.append(cnt)
# print(min(count))
################################
# n=int(input())
# list_num=[list(map(int,input().split())) for _ in range(n)]
# for i in range(n-1,0,-1):
#     for j in range(n-1):
#         if list_num[j][0]>list_num[j+1][0]:
#             list_num[j],list_num[j+1]=list_num[j+1],list_num[j]
#         elif list_num[j][0]== list_num[j+1][0]:
#             if list_num[j][1]>list_num[j+1][1]:
#                 list_num[j],list_num[j+1]=list_num[j+1],list_num[j]
# for k in range(n):
#     print(*list_num[k])
###################################
# import sys
# n,k=map(int,sys.stdin.readline().split())
# a=[]
# for i in range(n):
#     a.append(int(sys.stdin.readline()))
# i=1
# cnt=0
# while True:
#     if k>=a[-i]:
#         k-=a[-i]
#         cnt+=1
#         if k==0:
#             break
#     else:
#         i+=1
# print(cnt)

# n=int(input())
# list_n=list(map(int,input().split()))
# m=int(input())
# list_m=list(map(int,input().split()))
# sorted(list_n)
# b=[]
# for i in list_m:
#     a=list_n[::]
#     if i>list_n[len(list_n)//2]:
#         a=a[len(list_n)//2:]
#     else:
#         a=a[:len(list_n)//2]
#         if i == list_n[len(list_n)//2]:
#             b.append(1)
#         else:
#             b.append(0)
# print(b)
##############################
# while True:
#     a,b=map(int,input().split())
#     if a == 0 and b==0:
#         break
#     else:
#         if a%b!=0 and b%a == 0:
#             print('factor')
#         elif a%b ==0:
#             print('multiple')
#         else:
#             print('neither')
# ##########################
# x,y,w,h=map(int,input().split())
# a=[abs(x-0),abs(w-x),abs(y-0),abs(y-h)]
# print(min(a))
########################
# x=[]
# y=[]
# for i in range(3):
#     a,b=map(int,input().split())
#     if x.count(a) == 1:
#         x.remove(a)
#     else:
#         x.append(a)
#     if y.count(b) == 1:
#         y.remove(b)
#     else:
#         y.append(b)
# print(*x, *y)
#########################
# num_list=list(range(1,10000))
# i=0
# while True:
#     a=list(map(int,str(num_list[i])))
#     b=int(num_list[i])+sum(a)
#     num_list.remove(b)
#     i+=1
#     if a==9999:
#         break
# print(num_list)
##########################
# T=int(input())
# for t in range(T):
#     n,m=map(int,input().split())
#     list_num=[list(map(int,input().split())) for _ in range(n)]
#     a=[]
#     for i in range(n-1):
#         for j in range(n-1):
#             cnt=0
#             for p in range(m):
#                 for o in range(m):
#                     if 0<=i+p<n and 0<= j+o<n:
#                         cnt+=list_num[i+p][j+o]
#             a.append(cnt)
#     print(f'#{t+1} {max(a)}')
###################################
# T=int(input())
# for t in range(T):
#     n,m=map(int,input().split())
#     num_list=[list(map(int,input().split())) for _ in range(n)]
#     a=[]
#     for i in range(n-1):
#         for j in range(m-1):
#             cnt=0
#             for ni,nj in [[0,1],[0,-1],[1,0],[-1,0],[0,0]]:
#                 if 0<=i+ni<n and 0<=j+nj<m:
#                     cnt+=num_list[i+ni][j+nj]
#             a.append(cnt)
#     print(f'#{t+1} {max(a)}')
###################################
# n=int(input())
# a=[]
# for i in range(1667):
#     for j in range(1001):
#         if 3*i+5*j!=n:
#             pass
#         elif 3*i+5*j>n:
#             break
#         else:
#             a.append(i+j)
# if len(a) == 0:
#     a.append(-1)
# print(min(a))
########################
# n=int(input())
# num_list=list(map(int,input().split()))
# b=list(set(num_list))
# a=[]
# for i in range(n):
#     cnt=0
#     for j in range(len(b)):
#         if num_list[i]>b[j]:
#             cnt+=1
#     a.append(cnt)
# print(*a)
##########################
# T=int(input())
# for t in range(T):
#     n=int(input())
#     num_list=list(map(int,input().split()))
#     a=num_list[::]
#     for j in range(n):
#         for k in range(n-j):
#             if a[j]<a[j+k]:
#                 a[j],a[j+k] = a[j+k],a[j]
#     b=[0 for _ in range(10)]
#     for i in range(0,10,2):
#         b[i]=a[(i//2)]
#         b[i+1]=a[-1-(i//2)]
#     print(f'#{t+1} ',end='')
#     print(*b)
    ################
# T=int(input())
# for t in range(T):
#     p,pa,pb=map(int,input().split())
#     r=p
#     l=1
#     cnt_a=0
#     c=int((l+r)/2)
#     while c!=pa:
#         c=int((l+r)/2)
#         if pa<c:
#             r=c
#         elif pa>c:
#             l=c
#         cnt_a+=1
#     cnt_b=0
#     r=p
#     l=1
#     while c!=pb:
#         c=int((l+r)/2)
#         if pb<c:
#             r=c
#         elif pb>c:
#             l=c
#         cnt_b+=1
#     if cnt_a>cnt_b:
#         print(f'#{t+1} B')
#     elif cnt_a<cnt_b:
#         print(f'#{t+1} A')
#     elif cnt_a == cnt_b:
#         print(f'#{t+1} 0')
#######################
# ###########
# T=int(input())
# for t in range(T):
#     n=int(input())
#     list_num=[list(map(int,input().split())) for _ in range(n)]
#     a90=[[0]*n for _ in range(n)]
#     a180=[[0]*n for _ in range(n)]
#     a270=[[0]*n for _ in range(n)]
#     b90=[]
#     b180=[]
#     b270=[]
#     x=len(list_num)-1
#     for i in range(n):
#         for j in range(n):
#             a90[j][x-i] = list_num[i][j]
#             a180[x-i][x-j] = list_num[i][j]
#             a270[x-j][i] = list_num[i][j]
#     print(f'#{t+1}')
#     for k in range(n):
#         b90.append(''.join(map(str,a90[k])))
#         b180.append(''.join(map(str,a180[k])))
#         b270.append(''.join(map(str,a270[k])))
#     for p in range(n):
#         print(b90[p], b180[p], b270[p])
##########################
# T=int(input())
# for t in range(T):
#     n=int(input())
#     a=[[0]*n for _ in range(n)]
#     N=1
#     for i in range(n):
#         for j in range(n):
#             a[i][j]=N
#             N+=1
#             if j == n-1:
#                 i,j=j,i
#     print(a)
#############################
# import sys
# n,m=map(int,sys.stdin.readline().split())
# num_list=[list(map(int,input().split())) for _ in range(n)]
# sum_list=[[0]*(n+2) for _ in range(n+2)]
# for i in range(n):
#     for j in range(n):
#         if i == 0 and j == 0:
#             sum_list[i+1][j+1] = num_list[i][j]
#         elif i ==0 and j>0:
#             sum_list[i+1][j+1] = num_list[i][j]+sum_list[i+1][j]
#         elif j == 0 and i>0:
#             sum_list[i+1][j+1] = num_list[i][j]+sum_list[i][j+1]
#         else:
#             sum_list[i+1][j+1] = num_list[i][j]+sum_list[i+1][j]+sum_list[i][j+1]-sum_list[i][j]
# for k in range(m):
#     x1,y1,x2,y2 = map(int,sys.stdin.readline().split())
#     x=x2-x1
#     y=y2-y1
#     ans=sum_list[x2][y2]-sum_list[x2-x-1][y2]-sum_list[x2][y2-y-1]+sum_list[x2-x-1][y2-y-1]
#     print(ans)
########################
# n=int(input())
# start=0
# end=0
# cnt=0
# data=list(range(1,n+1))
# sum_data=0
# for start in range(n):
#     while sum_data<data[end] and end<n:
#         sum_data+=data[end]
#         end+=1
#     if sum_data == n:
#         cnt+=1
#     sum_data-=data[start]

# print(cnt)
##################
# T=int(input())
# for t in range(T):
#     n,m=map(int,input().split())
#     alp_list=[str(input()) for _ in range(n)]
#     for i in range(n):
#         cnt_1 = 0
#         cnt_2 = 0
#         a=[]
#         for j in range(m//2):
#             if alp_list[i][j] == alp_list[i][-j-1]:
#                 cnt_1+=1
#         if cnt_1>=m//2:
#             print(f'#{t+1} {alp_list[i]}')
#         for k in range(m // 2):
#             if alp_list[k][i] == alp_list[-1-k][i]:
#                 cnt_2 += 1
#                 a.insert(k,alp_list[k][i])
#                 a.insert(k+1, alp_list[k][i])
#                 b=''.join(map(str,a))

#         if cnt_2 >= m // 2:
#             print(f'#{t + 1} {b}')
######################
# T=int(input())
# for t in range(T):
#     a,b=map(int,input().split())
#     num_list=[list(map(int,input().split())) for _ in range(a)]
#     #가로
#     for i in range(a):
#         cnt=0
#         x=0
#         while num_list[i][x]>0:
#             x+=1
#             cnt+=1
#         x+=1

    #세로
############################
# n=int(input())
# m=int(input())
# a=list(map(int,input().split()))
# end = 0
# cnt=0
# sum=0
# for start in a:
#     while sum<m and end<n:
#         sum+=a[end]
#         end+=1
#         if sum == m:
#             cnt+=1
#     sum-=start
# print(cnt)
###########################
# import math
# while True:
#     list_num=list(map(int,input().split()))
#     c=max(list_num)
#     list_num.remove(c)
#     a,b=list_num[0],list_num[1]

#     if a==b==c==0:
#         break
#     else:
#         if c**2==(a**2)+(b**2):
#             print('right')
#         else:
#             print('wrong')
#################################
# T=10
# for t in range(T):
#     str2=str(input())
#     str1=str(input())
#     m=len(str2)
#     n=len(str1)
#     def BF(a,b):
#         i=0
#         j=0
#         cnt=0
#         while True:
#             if b[i]!=a[j]:
#                 i = i-j
#                 j=-1
#             i+=1
#             j+=1
#             if j == m:
#                 cnt+=1
#                 j=0
#             if i == n:
#                 return cnt
#     ans=BF(str2,str1)
#     print(f'#{t+1} {ans}')
#######################
# graph = {
#     'A': ['B'],
#     'B': ['A','C','G'],
#     'C': ['B','D','F'],
#     'D': ['C','E'],
#     'E': ['D'],
#     'F': ['C'],
#     'G': ['B']
# }
# def bfs(graph, start_node):

#     visit = list()
#     queue = list()
#     queue.append(start_node)
#     while queue:
#         node = queue.pop(0)
#         if node not in visit:
#             visit.append(node)
#             queue.extend(graph[node])

#     return visit
# def dfs(graph, start_node):

#     visit = list()
#     stack = list()
#     stack.append(start_node)
#     while stack:
#         node = stack.pop()
#         if node not in visit:
#             visit.append(node)
#             stack.extend(graph[node])
#     return visit
# print(bfs(graph,'D'))
# print(dfs(graph,'D'))