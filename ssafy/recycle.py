T = 10
from pprint import pprint
for t in range(T):
    n = int(input())
    abc = [list(map(str,input())) for _ in range(100)]
    mod_abc = list(map(list, zip(*abc)))
    abc_1=[]
    for x in range(100):
        abc_1.append(''.join(map(str,abc[x])))
    abc_2=[]
    for x in range(100):
        abc_2.append(''.join(map(str,mod_abc[x])))
    # 가로
    a=[]
    arc=[]
    for i in range(100):
        arc.append(abc_1[i][::-1])
    for k in range(100):
        for i in range(100):
            for j in range(i+1):
                if abc_1[k][j:100+j-i] == arc[k][j+i:j+100-i]:
                    a.append(len(abc_1[0][i:100-i]))
    # 세로
    arc = []
    for i in range(100):
        arc.append(abc_2[i][::-1])
    for k in range(100):
        for i in range(100):
            for j in range(1+i):
                if abc_2[k][j:100 + j-i] == arc[k][j + i:j + 100 - i]:
                    a.append(len(abc_2[0][i:100 - i]))

    # print(abc_2)
    # print(abc_1)
    print(max(a))

