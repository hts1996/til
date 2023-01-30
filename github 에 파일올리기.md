github 에 파일올리기

cmd입력

git init:최초한번만

.git 지우면 링크사라짐

git status:뭘해야할지모를떄

git add 파일명

git config--global user.email"이메일"

git config--global user.name"이름"

git commit

i누르고 쪽지남기기first commit그후ESC 후:wq

git push

git주소입력

git remote add <name> <url>

git push --set-upstream origin master

git push

add : working directory 에 있는걸 staging area 에 올리기

commit : staging area 에 쪽지를 남겨두는것

push :staging area 에 있는것을 repository에 올리기

원본과동일한파일 commit불가능

---



```
echo "# test" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/hts1996/test.git
git push -u origin main

```

커밋메시지

제목만적을때 

git commit -m ""

git push

git add로 여러개 올린후 한번에 커밋가능

git add .

git add -A



branch:방나누기/버전구분,여러가지버전가능

여러가지버전의장점:버그발생시 빠른 복구가능

```
git branch -M main
```

master공용방

git branch:현재위치

git branch <name> 생성

git checkout <name>로 이동

최초로 가져오는방법

cmd

git clone 우클릭

주소로 복제한것 (권한x)

포크:원본의 모제품을 다시복제한것 push가능,모제품으로 push

PR:모제품 원본으로 변경요청

이어가져오는방법





PR시 충돌시 리졸브로해결

ls/al



cli 로도 branch생성가능

git branch 

git checkout -b 파일명

git remote add origin5 내주소

git push origin5 prac

