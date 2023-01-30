#리스트
#.append(x)
cafe = ['starbuscks','tomntoms','hollys']
cafe.append('banapresso')
print(cafe)
#.insert(i,x) list길이보다긴경우 맨뒤에 첨부
cafe = ['starbuscks','tomntoms','hollys']
cafe.insert(0,'start')#['start', 'starbuscks', 'tomntoms', 'hollys']
print(cafe)
#.extend(iterable)
cafe = ['starbuscks','tomntoms','hollys']
cafe.extend(['coffee'])#['starbuscks', 'tomntoms', 'hollys', 'coffee']
print(cafe)
cafe = ['starbuscks','tomntoms','hollys']
cafe+=['coffee']
print(cafe)
cafe = ['starbuscks','tomntoms','hollys']
cafe.extend('cup')#[]안에 안쓰면 각각첨부됨['starbuscks', 'tomntoms', 'hollys', 'c', 'u', 'p']
print(cafe)
#.remove(x)
numbers=[1,2,3,'hi']
print(numbers)
numbers.remove('hi')
print(numbers)#[1, 2, 3]
#numbers.remove('hi')#valueerror
#.pop(i) 정해진위치에있는 i값을 삭제하고 그항목을 반환
#i가지정되지 않으면 마지막 항목을 삭제하고 반환함
numbers = ['hi',1,2,3]
numbers.pop()
print(numbers)
#.clear()
numbers = ['hi',1,2,3]
numbers.clear()
print(numbers)
#.index(x)
numbers=[1,2,3,4]
print(numbers)
print(numbers.index(3))#2
print(numbers.index(100))#없는경우 valueError
#.count(x)
numbers=[1,2,3,1,1]
print(numbers.count(1))#3
print(numbers.count(100))#0
#.sort() 원본리스트를 정렬함,none반환
#sort()와sortd차이점 원본변경이 없고 리턴값이 있다?
numbers=[3,2,5,1]
result = numbers.sort()
print(numbers,result)#[1,2,3,5] none
numbers=[3,2,5,1]
result = sorted(numbers)
print(numbers,result)#[3,2,5,1] [1,2,3,5]
#.reverse() 순서를 반대로 뒤집음
numbers=[3,2,5,1]
result = numbers.reverse()
print(numbers,result)#[1,5,3,3] none
#연산자
'a' in 'apple'
'a' not in 'apple'
[0]+[0]
[0]*8

