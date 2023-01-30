#셋
#.add(elem)
a={'사과','바나나','수박'}
a.add('딸기')
print(a)#{'수박', '사과', '바나나', '딸기'} 출력시 순서상관없이 랜덤출력
#.update(*others)
a={'사과','바나나','수박'}
a.update(['딸기','바나나','참외'])
print(a)#{'수박', '딸기', '참외', '바나나', '사과'}중복 허락X
#.remove(elem)
a={'사과','바나나','수박'}
a.remove('사과')
print(a)#{'수박', '바나나'}
#a.remove('애플')#keyerror
#print(a)#keyerror
#.discard(elem) 셋에서 삭제하고 없어도 에러가 발생하지않음
a={'사과','바나나','수박'}
a.discard('사과')
print(a)
a.discard('애플')
print(a)
#.pop() 임의의 원소를 제거해 반환
a={'사과','바나나','수박'}
a.pop()
print(a)#{'사과', '바나나'}
#.clear()모두삭제
a={'사과','바나나','수박'}
a.clear()
print(a)#set()
#집합 관련 함수
# s.isdisjoint(t):셋s가셋t의 서로같은항목을 하나라도 갖고있지않은경우, True서로소
# s.issubset(t):셋s가셋t의 하위셋인경우True반환
# s.issuperset(t):셋s가 셋t의 상위 셋인경우 True반환
#딕셔너리
#.get(key[,defalut])
my_dict = {'apple':'사과','banana':'바나나'}
#my_dict['pineapple']#KeyError
my_dict = {'apple':'사과','banana':'바나나'}
print(my_dict.get('pineapple'))#none
print(my_dict.get('apple'))#사과
print(my_dict.get('pineapple',0))#0
#.pop(key[,defalut])
my_dict = {'apple':'사과','banana':'바나나'}
data = my_dict.pop('apple')
print(data,my_dict)
my_dict = {'apple':'사과','banana':'바나나'}
data = my_dict.pop('pineapple',0)
print(data,my_dict)#0 {'apple':'사과','banana':'바나나'}
#.update()
my_dict = {'apple':'사','banana':'바나나'}
data = my_dict.update(apple='사과')
print(my_dict)

