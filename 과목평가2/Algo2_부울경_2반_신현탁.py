T=int(input())

for t in range(T):#테스트케이스만큼 작업수행
    n = int(input())
    r,c=map(int,input().split())#망치의 위치(r,c)
    cnt = 0
    for i in range(n):
        a,b,k = map(int,input().split())#두더지의 위치(a,b), 머문시간k

        if abs(a-r)+abs(b-c) <= k:#망치와 두더지와의거리차가 k이하일때 점수획득
            cnt+=1
            r,c = a,b#그후 망치위치는 두더지의 위치

        else:#만약 망치와 두더지와의 거리차가 k보다 클때 k만큼이동
            if a>r:#가로로 먼저 이동
                while a!=r and k!=0:# 망치의열위치가 두더지보다 클때
                    r+=1
                    k-=1

            elif a<r:
                while a!=r and k!=0:#망치의열위치가 두더지보다 작을때
                    r-=1
                    k-=1

            if b>c:#세로로 이동
                while b!=c and k!=0:#망치의행위치가 두더지보다 클때
                    c+=1
                    k-=1

            elif b<c:
                while b!=c and k!=0:#망치의행위치가 두더지보다 작을때
                    c-=1
                    k-=1

    print(f'#{t+1} {cnt}')