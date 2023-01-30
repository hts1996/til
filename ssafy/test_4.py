# a,b=map(int,input().split())
# list_a=[list(map(int,input().split())) for _ in range(a)]
# list_b=[list(map(int,input().split())) for _ in range(a)]
# list_c=[[0]*b for _ in range(a)]
# for i in range(b):
#     for j in range(a):
#         list_c[i][j]=list_a[i][j]+list_b[i][j]
# for k in range(a):
#     print(*list_c[k])
#########################################################
# list_num=[list(map(int,input().split())) for _ in range(9)]
# max=0
# for i in range(9):
#     for j in range(8):
#         if list_num[i][j+1] > max:
#             max=list_num[i][j+1]
#             num=[]
#             num.append((i+1,j+2))
#         elif list_num[i][j+1] == max:
#             max=max
#             num.append((i+1,j+2))
#     if max == 0:
#         print(max)
#         print('0 0')
# print(max)
# print(*num[0])
#####################################
#재귀
# num=int(input())
# def bu(a,b):
#     if a == 0:
#         return b
#     elif b==1:
#         return 1
#     else:
#         return bu(a,b-1)+bu(a-1,b) 
# for i in range(num):
#     x=int(input())
#     y=int(input())
#     print(bu(x,y))
####################################
# num=int(input())
# def fac(num):
#     if num==1:
#         fac(num) == 1
#     else:
#         return num*fac(num-1)
####################################
num=int(input())
list_1=[]
for i in range(num):
    list_1.append(int(input()))
mod_list=sorted(list_1)
for j in range(len(mod_list)):
    print(mod_list[j],end="\n")