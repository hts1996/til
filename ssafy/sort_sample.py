a=[55,7,78,12,42]
b=[1,8,4,6,5,2,4,9,6]
c=[5,7,5,5,1,6,8,7,4,23,6,7,1,2,5,74,4,5,9]
#내가만든거
def bubble_sort(list):
    for i in range(len(list)-1):# 5번이 아니라 4번 5번이어도 결과는 나옴
        for j in range(len(list)-1-i):
            if list[j]>list[j+1]:
                list[j+1], list[j]=list[j], list[j+1]
            else:
                pass
    print(*list)
bubble_sort(b)
#교육예제
# n=int(input())# 5일때
# arr = list(map(int,input().split()))
# for i in range(n-1,0,-1):#4 3 2 1 총4번
#     for j in range(i):# 4 3 2 1
#         if arr[j]>arr[j+1]:
#             arr[j],arr[j+1] = arr[j+1],arr[j]
# print(*arr)
