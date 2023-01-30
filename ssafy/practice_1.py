#.find(x) 첫번쨰위치를반환 없으면 -1반환 오류X
print('apple'.find('p'))#1
print('apple'.find('k'))#-1
#.index(x) x의 첫번째 위치를 반환 없으면 오류발생
print('apple'.index('p'))#1
print('apple'.index('k'))#오류발생
#문자열관련검증메서드사용예시
print('abc'.isalpha())#True
print('ㄱㄴㄷ'.isalpha())#True
print('Ab'.isupper())#False
print('ab'.islower())#True
print('Title Title!'.istitle())#True(둘다대문자로 시작하지않을경우 False)
print('123'.isnumeric())#True
#.replace(old,new[,count])
print('coone'.replace('o','a'))#caane
print('wooooowoo'.replace('o','!',2))#w!!ooowoo
#.strip([chars])
print('    와우!\n'.strip())#'와우!'
print('    와우!\n'.lstrip())#'와우!'
print('    와우!\n'.rstrip())#'    와우!'
print('안녕하세요????'.rstrip('?'))# '안녕하세요'(입력문자가 없는곳까지진행)
#.split(sep=none,maxsplit=-1) 선행후행공백은 빈문자열에 포함시키지않음
print('a,b,c'.split(','))#['a','b','c']
print('a b c'.split())# ['a','b','c']
#'separator'.join([iterable])
print('!'.join('ssafy'))#'s!s!a!f!y'
print(' '.join(['3','5']))# '3 5'
#문자열 변경예시
msg='hI! Everyone, I\'m ssafy'
print(msg.capitalize())#Hi! everyone, i'm ssafy(첫번쨰만 대문자나머지소문자)
print(msg.swapcase())# Hi! eVERYONE, i'M SSAFY(대문자소문자서로변환)
