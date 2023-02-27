# import sys
# input=sys.stdin.readline
# n=int(input)
# a=[]
# for i in range(n):
#     word=str(input())
#     if len(word)>=6:
#         a.append(word[5:])
#     elif word == 'top':
#         if len(a) == 0:
#             print(-1)
#         else:
#             print(a[-1])
#     elif word == 'size':
#         print(len(a))
#     elif word == 'empty':
#         if len(a) == 0:
#             print(1)
#         else:
#             print(0)
#     elif word == 'pop':
#         if len(a) == 0:
#             print(-1)
#         else:
#             print(a.pop())
#################
from pprint import pprint

lst=[[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5]]

lst_t=list(map(list,zip(*lst)))

pprint(lst)
print()
pprint(lst_t)