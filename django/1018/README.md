- # 장고 14

  <aside> ⏰ 오늘의 일정
   ~ 13 : 30 - 점심 시간 **~ 15 : 30 - 실습 시간 ~ 16 : 00 - 쉬는 시간 ~ 17 : 50 - 실습 시간

  </aside>

  ------

  # 실습

  <aside> 📚 실습 진행 후 **가상환경 폴더를 제외한** 파일 폴더를 압축해서 실라버스에 제출해주세요. 가상환경을 포함해서 제출하면 용량 제한을 초과하니 꼭 가상환경 폴더를 제외하고 압축해서 제출해주세요.

  각 기능은 적절한 브랜치로 나눠서 개발하세요.

  DJANGO 개발은 꼭 가상 환경을 실행한 상태로 진행하세요.

  </aside>

  복습 자료

  [자료 공유](https://www.notion.so/e7ee7159a74243d8bf865f89f78e2c85)

  [GitHub - kdt-live/01-django-modelform](https://github.com/kdt-live/01-django-modelform)

  ## 목표

  게시글과 댓글이 **1 : N** 관계로 매핑 된 게시글에 댓글을 작성할 수 있는 서비스를 개발합니다.

  ## 요구사항

  ### 모델 Model

  모델은 아래 조건을 만족해야합니다.

  - 모델 이름 : Article

    모델 필드

    | 필드 이름 | 역할    | 필드 | 속성          |
    | --------- | ------- | ---- | ------------- |
    | title     | 글 제목 | Char | max_length=80 |
    | content   | 글 내용 | Text |               |

  - 모델 이름 : Comment

    모델 필드

    | 필드 이름 | 역할        | 필드       | 속성                     |
    | --------- | ----------- | ---------- | ------------------------ |
    | article   | 참조 게시글 | ForeignKey | on_delete=models.CASCADE |
    | content   | 댓글 내용   | Char       | max_length=80            |

  ### 기능 View

  **게시판 articles**

  게시글 목록 조회

  - `GET` http://127.0.0.1:8000/article**s**/

  게시글 정보 조회

  - `GET` http://127.0.0.1:8000/article**s**/[int:article_pk](int:article_pk)/
  - 해당 게시글(article_pk)에 작성된 댓글 목록 조회

  게시글 생성

  - `POST` http://127.0.0.1:8000/article**s**[/](http://127.0.0.1:8000/posts/create/)create[/](http://127.0.0.1:8000/posts/create/)

  **댓글 comments**

  게시글에 작성된 댓글 목록 조회

  - `GET` http://127.0.0.1:8000/article**s**/[int:article_pk](int:article_pk)/
  - 해당 게시글(article_pk)의 댓글 목록 조회

  댓글 생성

  - `POST` http://127.0.0.1:8000/article**s**/[int:article_pk](int:article_pk)/comments/

  댓글 삭제 **(교재 참고)**

  - `POST` http://127.0.0.1:8000/article**s**/[int:article_pk](int:article_pk)/comments/[int:comment_pk](int:comment_pk)/delete/

  ### 화면 Template

  게시글 목록 페이지

  - `GET` http://127.0.0.1:8000/article**s**/

  게시글 정보 페이지

  - `GET` http://127.0.0.1:8000/article**s**/[int:article_pk](int:article_pk)/
  - 댓글 작성 폼
  - 총 댓글 개수 출력 **(교재 참고)**
  - 댓글 목록
    - 댓글 내용
    - 댓글 삭제 버튼 **(교재 참고)**

  게시글 작성 페이지

  - `GET` http://127.0.0.1:8000/article**s**/create/
  - 게시글 작성 폼