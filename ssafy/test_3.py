a,b=map(int,input().split())
people=list(range(1,a+1))
c=b-1
list_1=[]
# for i in range(a):
#     list_1.append(people.pop(c))
#     if c+b>len(people):
#         c=c+b-len(people)-1
#         if c>=len(people):
#             c=c-len(people)
#             if b>=len(people):
#                 b=b-len(people)
#             else:
#                 pass
#         else:
#             if b>=len(people):
#                 b=b-len(people)
#             else:
#                 pass
#     else:
#         c=c+b-1
for i in range(a):
    list_1.append(people.pop(c))
    if b>=len(people):
        b=b-len(people)
        while len(people)<=1:
            if c+b>len(people):
                c=c+b-len(people)-1
                if c>=len(people):
                   c=c-len(people)
s=""
for j in range(len(list_1)):
    s+=str(list_1[j])
print("<"+str((', '.join(s)))+">")