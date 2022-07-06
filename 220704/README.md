# 7/5 - 마크다운

### (제목) ###의 갯수로 h1~h6까지 표현 가능

# MARKDOWN

## 마크다운 2

### 마크다운 3

#### 마크다운 4

##### 마크다운 5

###### 마크다운 6



### Inline Code Block (`<<로 앞뒤 감싸기)

`print`는 파이썬에서 출력하는 함수이다.



# 표 (ctrl + t)

|      |      |
| ---- | ---- |
|      |      |

**야** : `**`  굵게 (Ctrl+b)

~~야~~: `~~` 취소선

*야*:`*` 기울임



# 코드블럭



​	```로 생성한다. Ctrl + shift +k 로도 가능

```
```뒤에 프로그래밍 언어를 적을 수 있음
```

```python
python
```

```java
java
```

```html
html
```

​	등등..

# 마크다운 수평선

3개 이상의 asterisks (***), dashes (---), or underscores (___)

***

---

___

# 마크다운 인용문

\>를 통해 인용문을 작성

> 안녕하세요



## 말머리

*,+,- 입력 후 TAB 키 누르면 말머리 기호 생성 (각 생성되는 기호가 다르다.)

* + - 



# 이미지 삽입

```
![Alt text](/path/to/img.jpg)
![Alt text](/path/to/img.jpg "Optional title")
```

![도라에몽](https://i.pinimg.com/736x/55/7d/38/557d38dc2749c7aa8e0dba5b8f4415b0.jpg)



# 7/6 GIT/GITHUB

### :exclamation:명령어

:star:git init : 로컬 저장소 생성
:star:git add 파일명 : 특정 파일 폴더의 변경사항 추가
:star:git commit -m '커밋메시지' : 커밋 시 메시지 출력
:star:git status : 1통,2통 상태확인

:star: git push <원격저장소이름> <브랜치이름> : 원격 저장소로 로컬 저장소 변경 사항(커밋)을 올림(push)

 git log : 현재 저장소에 기록된 커밋 조회

 git log -1 : 가장 최근에 한 커밋 조회

 git status : 파일의 상태를 알 수 있음

 git rm <파일명> : 해당 파일 삭제

 git config --list : 아이디 확인

 git remote -v : 원격 저장소 정보 확인

 git remote add origin https://github.com/github username/저장소이름.git  : 로컬 저장소 경로 설정(1회만)

 git clone <url>원격 저장소 복제

