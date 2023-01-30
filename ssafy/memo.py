list_mil=list(range(1,10001))
def self_num(n):
    while n < 10000:
        list_num=[]
        sum = 0
        len_num = 0
        for i in range(len(str(n))):
            len_num += int(str(n)[i])
            sum = n + len_num
            if sum <= 10000:
                n = sum
            else:
                pass
        list_num.append(n)
    return list_num

# self_num(1)
# self_num(3)
# self_num(5)
# self_num(7)
# self_num(9)

print(self_num(1))
