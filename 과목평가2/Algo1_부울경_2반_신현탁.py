T=int(input())

for t in range(T):# 테스트케이스만큰 작업수행
    n,m = map(int,input().split())
    # 빈 배열생성(nxn)
    dohwaji = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(m):
        y1,x1,x,y = map(int,input().split())#행,열,너비,높이
        for j in range(x):#너비만큼
            for k in range(y):#높이만큼
                if 0<=y1+k<n and 0<=x1+j<n:#배열안범위일때만 작업수행
                    dohwaji[y1+k][x1+j] = 1

    sum=0
    for o in range(n):# 행갯수만큼 작업수행
        sum+=dohwaji[o].count(1)# 각 행에 1의 갯수를 구한뒤 합친다.

    print(f'#{t+1} {sum}')
