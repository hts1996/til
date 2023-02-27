# a=[55,7,78,12,42]
# b=[1,8,4,6,5,2,4,9,6]
# c=[5,7,5,5,1,6,8,7,4,23,6,7,1,2,5,74,4,5,9]
#bubble
# #내가만든거
# def bubble_sort(list):
#     for i in range(len(list)-1):# 5번이 아니라 4번 5번이어도 결과는 나옴
#         for j in range(len(list)-1-i):
#             if list[j]>list[j+1]:
#                 list[j+1], list[j] = list[j], list[j+1]
#             else:
#                 pass
#     print(*list)
# bubble_sort(b)
# #교육예제
# n=int(input())# 5일때
# arr = list(map(int,input().split()))
# for i in range(n-1,0,-1):#4 3 2 1 총4번
#     for j in range(i):# 4 3 2 1
#         if arr[j]>arr[j+1]:
#             arr[j],arr[j+1] = arr[j+1],arr[j]
# print(*arr)
#max
# #내가만든거
# ans=list(map(int,input().split()))
# max=ans[0]
# for i in range(len(ans)):
# 	if max<ans[i]:
# 		max=ans[i]
# print(max)
# #예제
# T=int(input())
# for tc in range(1,T+1):
#     n=int(input())
#     arr = list(map(int,input().split()))
#     max=arr[0] # 첫원소를 최대로 가정
#     for i in range(1,n): #나머지원소비교
#         if max<arr[i]:
#             max=arr[i]
#     print(f'#{tc} {max}')
#내가한거
#counintg
# a=[1,4,2,5,6,7,6,7,8,1,9,2,2,6,6,4,3,2]
# cnt=[0]*(max(a)+1)
# for i in a:
#     cnt[i]+=1
# print(cnt)
# #누적합
# for j in range(1,len(cnt)):
#     cnt[j]=cnt[j-1]+cnt[j]
# print(cnt)
# b=[0]*len(a)
# #자리배치
# for k in a:
#     b[cnt[k]-1]=k
#     cnt[k]-=1
# print(b)
# 내림차순
# counintg
# a=[1,6,5,5,2,3,4]
# cnt=[0]*(max(a)+1)
# for i in a:
#     cnt[i]+=1
# print(cnt)
# #누적합
# for j in range(1,len(cnt)):
#     cnt[j]=cnt[j-1]+cnt[j]
# print(cnt)
# b=[0]*(len(a))
# #자리배치
# for k in a:
#     b[-(cnt[k])]=k
#     cnt[k]-=1
# print(b)
#예제
# #a[]--입력배열(0to k)
# c=[0]*k+1
#babygin
# num=456789
# c=[0]*12
# for i in range(6):
#     c[num%10]+=1
#     num//=10
# print(c)