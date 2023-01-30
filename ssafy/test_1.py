# dust = 28
# if dust > 150:
#     print("매우나쁨")
#     if dust > 300:
#         print("실외활동자제하세요.")
# elif dust > 80:
#     print("나쁨")
# elif dust > 30:
#     print("보통")
# else:
#     print("좋음")
# print("미세먼지 확인")
# num = 10
# # value = num if num >= 0 else -num
# # print(value)
# num = 2
# result = print('홀수') if num % 2 else print('짝수')
# a = 0
# while a < 5:
#     print('a')
#     a += 1
# else:
#     print('끝')
# chars = input()
# # for char in chars:
# #     print(char)
# #     chars = input()
# for idx in range(len(chars)):
#     print(chars[idx])
# grades = {'john' : 80, 'eric' : 90}
# grades
# members = ['민수', '영희', '철수']
# for idx, number in enumerate(members):
#     print(idx,number)
# s = input('숫자를 입력해주세요 : ')
# sum=0
# for i in range(len(s)):
#     sum+=int(s[i])
#     if i == (len(s)-1):
#         print(sum)
# list_1=list(map(int,input().split()))
# print(list_1)
# alp1,alp2,alp3='A','B','C'
# list_alp=[]
# for i in range(17):
#     if i<=6:
#         list_alp.append(alp1)
#     elif i>6 and i<=12:
#         list_alp.append(alp2)
#     elif i<17:
#         list_alp.append(alp3)
# for j in range(len(list_alp)):
#     print(list_alp[len(list_alp)-j-1],end="")
# alp1,alp2,num=map(str,input().split())
# for j in range(int(num)):
#     for i in range(ord(alp2)-ord(alp1)+1):
#         print(chr(ord(alp1)+i),end="")
#     print()
# alp,num=map(str,input().split())
# for i in range(int(num)):
#     for j in range(int(num)):
#         print(alp,end="")
# #     print()
# list_a=[[0 for _ in range(3)] for _ in range(3)]
# num1,num2,num3=map(int,input().split())
# list_a[num1][num2]=num3 
# for i in range(3):
#     print(*list_a[i])
# list_a=[[0 for _ in range(3)] for _ in range(6)]
# num1,num2=map(int,input().split())
# for i in range(6):
#     if i<3:
#         for j in range(3):
#             list_a[i][j]=num1
#     else:
#         for j in range(3):
#             list_a[i][j]=num2
# for k in range(6):
#     for l in range(3):
#         print(list_a[k][l],end="")
#     print()
# list_a=[[0 for _ in range(6)] for _ in range(3)]
# alp1,alp2=map(str,input().split())
# for i in range(3):
#     for j in range(6):
#         if j>3:
#             list_a[i][j]=alp2
#         else:
#             list_a[i][j]=alp1
# for k in range(3):
#     for l in range(6):
#         print(list_a[k][l],end="")
#     print()
# list_num=[4,3,6,1,3,1,5,3]
# num=int(input())
# for i in range(len(list_num)):
# #     if list_num[i] == num:
# # import time
# A,B,C=map(int,input().split())
# start = time.time()

# def square(num):
#     square=1
#     for i in range(B):
#         square*=A
#     return square%C
# print(square(B))
# end = time.time()
# print(f'{end-start:.5f}sec')
# def check(target_str):
#     counting_char=0
#     counting_digit=0
#     counting_sym=0
#     for char in target_str:
#         if char.isalpha() == True:
#             counting_char += 1
#         elif char.isdigit() == True:
#             counting_digit += 1
#         else:
#             counting_sym += 1
#     return counting_char,counting_digit,counting_sym
# target_str='abcdefghij1234567!@#$%^&'
# char_counting,digit_counting,symbol_counting = check(target_str)
# print(f'char : {char_counting}, digit : {digit_counting}, symbop : {symbol_counting}')
#####################################################
# inp=str(input())
# print(ord(inp))
#################################
# num1=int(input())
# num2=str(input())
# sum=0
# for i in range(num1):
#     sum+=int(num2[i])
# print(sum)
###################################
# alp=str(input())
# for i in range(97,123):
#     print(alp.find(chr(i)),end=" ")
#######################################
# num=int(input())
# def QR():
#     alp=str(input())
#     rlt=""
#     for i in range(2,len(alp)):
#         if len(alp) < 1:
#             pass
#         else:
#             rlt += alp[i]*int(alp[0])
#     return rlt
# for i in range(num):
#     print(QR())
##########################################
# alp=str(input())
# mod_alp=','.join(alp.upper())
# set_alp=set(mod_alp.split(','))
# max=0
# alp_list=list(set_alp)
# for i in range(len(alp_list)):
#     mod_alp.count(alp_list[i])
#     if mod_alp.count(alp_list[i])>max:
#         max=mod_alp.count(alp_list[i])
#         char=alp_list[i]
#     elif mod_alp.count(alp_list[i])==max:
#         char='?'
# print(char)
##########################################
# alp=str(input())
# cz_alp=['c=','c-','dz=','d-','lj','nj','s=','z=']
# counting=0
# for i in cz_alp:
#     while alp.find(i)>=0:
#         if alp.find(i) >= 0:
#             alp=alp.replace(i,' ',1)
#             counting+=1
#         else:
#             pass
# print(counting+len(alp.replace(' ','')))
#########################################        
# a,b=map(str,input().split())
# a=a[::-1]
# b=b[::-1]
# if a>b:
#     print(a)
# else:
#     print(b)
    ##################
# alp=str(input())
# counting=0
# sum=0
# for i in range(len(alp)):
#     if ord(alp[i])>=87:
#         counting = 10
#     elif ord(alp[i])>=84:
#         counting = 9
#     elif ord(alp[i])>=80:
#         counting = 8
#     elif ord(alp[i])>=77:
#         counting = 7
#     elif ord(alp[i])>=74:
#         counting = 6
#     elif ord(alp[i])>=71:
#         counting = 5
#     elif ord(alp[i])>=68:
#         counting = 4
#     elif ord(alp[i])>=65:
#         counting = 3
#     sum+=counting
# print(sum)
#####################
# a,b,c=map(int,input().split())
# x=1
# while c*x < (x//10)*1700+(a+b)*(x%10):
#     x+=1
# print(x+1)
###############################################
# sample_list=[11,22,33,44,55]
# #주어진 리스트의 3번인덱스에 있는 항목을 제거하고 변수에 할당해주세요.

# print('origianl list:', sample_list)
# elem=sample_list.pop(3)
# print('list after:',sample_list)
# print('elem: ',elem)
# #77가장뒤에추가
# sample_list.append(77)
# print('sample',sample_list)
# #할당해놓은 변수의 값을 2번인데스에 추가해보세요
# sample_list.insert(2,elem)
# print(sample_list)
# my_tuple=(11,22,33,44,55,66)
# #44와55의값을 새로운 튜플에 할당해보세요.
# new_tuple = my_tuple[3:5]
# print(new_tuple)

# scores = [('eng',88),('sci',90),('math',80)]
# def check(x):
#     return x[1]
# #정렬
# scores.sort(key=lambda x: x[1])
# print(scores)
