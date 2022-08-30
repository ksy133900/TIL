# HTML  

* 웹을 이루는 가장 기초적인 구성 요소로, 웹 콘텐츠의 의미와 구조를 정의할 때 사용

* 컨텐츠의 서로 다른 부분들을 씌우거나(wrap) 감싸서(enclose) 다른 형식으로 보이게하거나 특정한 방식으로 동작하도록 하는 일련의 **요소([elements](https://developer.mozilla.org/ko/docs/Glossary/Element))**로 이루어져 있다.

**요소(element)**: 요소는 여는 태그와 닫는 태그, 그리고 컨텐츠로 이루어진다.

## 속성

* 속성은 실제 컨텐츠로 표시되길 원하지 않는 추가적인 정보를 담고 있다.
* 속성이 항상 가져야 하는 것:
  1. 요소 이름 (또는 요소가 하나 이상 속성을 이미 가지고 있다면 이전 속성)과 속성 사이에 공백이 있어야 한다.
  2. 속성 이름 뒤에는 등호(=)가 와야 한다.
  3. 속성 값의 앞 뒤에 열고 닫는 인용부호(" 또는 ')가 있어야 한다.

* 어떤 요소들은 내용을 갖지 않습니다, 그리고 이것을 **빈 요소(empty elements)**라고 한다.

```html
<img src="images/firefox-icon.png" alt="My test image">
```

이 요소는 두 개의 속성을 포함하고 있으나 닫는 </img> 태그가 없습니다. 이미지 요소는 효과를 주기 위해 컨텐츠를 감싸지 않기 때문이다.

```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>My test page</title>
  </head>
  <body>
    <img src="images/firefox-icon.png" alt="My test image">
  </body>
</html>
```

- ``<html></html>`` —   이 요소는 페이지 전체의 컨텐츠를 감싸며, 루트(root) 요소라고도 합니다.
- ``<head></head>`` —   이 요소는 HTML 페이지에 포함되어 있는 모든 것들(여러분의 페이지를 조회하는 사람들에게 보여주지 않을 컨텐츠)의 컨테이너 역할을 합니다
- ``<body></body>`` —  이것은 **페이지에 방문한 모든 웹 사용자들에게 보여주길 원하는 *모든* 컨텐트를 담고 있으며,** 그것이 텍스트일 수도, 이미지, 비디오, 게임, 플레이할 수 있는 오디오 트랙이나 다른 무엇이든 될 수 있습니다.

* ``<title></title>`` — 이 요소는 **페이지의 제목을 설정하는 것으로 페이지가 로드되는 브라우저의 탭에 이 제목이 표시됩니다.** 

## [이미지](https://developer.mozilla.org/ko/docs/Learn/Getting_started_with_the_web/HTML_basics#이미지)

```html
<img src="images/firefox-icon.png" alt="My test image">
```

``alt``— 이 속성에는 다음과 같은 이유로 이미지를 볼 수 없는 사용자들을 위한 설명문(descriptive text)을 지정할 수 있습니다.

1. 무언가 잘못되어서 이미지를 표시할 수 없는 경우
2. 시각 장애자인 경우 alt 텍스트(대체 텍스트)를 읽어주는 스크린 리더라는 도구를 사용한다.

### [제목](https://developer.mozilla.org/ko/docs/Learn/Getting_started_with_the_web/HTML_basics#제목)

```html
<h1>My main title</h1>
<h2>My top level heading</h2>
<h3>My subheading</h3>
<h4>My sub-subheading</h4>
```

**제목 요소는 내용의 특정 부분이 제목 또는 내용의 하위 제목임을 구체화 할 수 있게 해준다** (h1~h6)

### [문단](https://developer.mozilla.org/ko/docs/Learn/Getting_started_with_the_web/HTML_basics#문단)

```html
<p>This is a single paragraph</p>
```

``<p>`` 요소는 문자의 문단을 포함하기 위한 것입니다; 일반적인 문자 내용을 나타낼 때 많이 사용한다.

### [목록](https://developer.mozilla.org/ko/docs/Learn/Getting_started_with_the_web/HTML_basics#목록)

```html
<p>At Mozilla, we’re a global community of technologists, thinkers, and builders working together ... </p>
```

```html
<p>At Mozilla, we’re a global community of</p>
<ul>
  <li>technologists</li>
  <li>thinkers</li>
  <li>builders</li>
</ul>
<p>working together ... </p>

<!--At Mozilla, we’re a global community of
    •technologists
    •thinkers
    •builders
working together ... -->
<oi>oi로 감싸면 말머리기호가 1..2..3 이다.</oi>
```

1. **순서 없는 목록은** 쇼핑 목록과 같이 항목의 순서에 관계가 없는 목록을 위한 것입니다. ``<ul>`` 요소로 둘러 쌓여 있습니다.
2. **순서 있는 리스트**는 조리법처럼 항목의 순서가 중요한 목록을 위한 것입니다. ``<ol>`` 요소로 둘러 쌓여 있습니다.

## [연결](https://developer.mozilla.org/ko/docs/Learn/Getting_started_with_the_web/HTML_basics#연결)

``<a>``*a* 는 "anchor" 의 약자입니다. 문장 안의 어떤 단어를 링크로 만든다. 

ex)  "Mozilla Manifesto"  선택

1. **--문자를 <a> 요소로 감싼다.**

```html
<a>Mozilla Manifesto</a>
```

2. **``<a>`` 요소에 href 속성을 줍니다**

```html
<a href="">Mozilla Manifesto</a>
```

3. **이 속성의 값에 연결하길 원하는 웹 주소를 채운다.**

```html
<a href="https://www.mozilla.org/en-US/about/manifesto/">Mozilla Manifesto</a>
```

# CSS

* HTML 문서에 있는 요소들에 선택적으로 스타일을 적용할 수 있다

- 각각의 rule set (셀렉터로 구분) 은 반드시 (`{}`) 로 감싸져야 합니다.
- 각각의 선언 안에, 각 속성을 해당 값과 구분하기 위해 콜론 (:)을 사용해야만 한다.
- 각각의 rule set 안에, 각 선언을 그 다음 선언으로부터 구분하기 위해 세미콜론 (;)을 사용해야만 한다.
  - 여러 속성 값들을 한번에 수정하기 위해서, 세미콜론으로 구분 작성.

```html
p {
  color: red;
  width: 500px;
  border: 1px solid black;
}
```

```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>My test page</title>
  </head>
    <!-- style 세미콜론 부분 작성 -->
  <style>
    h1 {
        color : red;
        font-size: 25px
            /* px 은 'pixels' 를 의미합니다: 기본 글자 크기는 현재 10 pixels 높이입니다. */
      }
      .title-brown {
        color : brown;
      }
      #title-yellow {
        color: yellow
      }
    /* style 세미콜론 부분 작성 */
    h5,h6,p {
        color : blueviolet
    }
  </style>
  <body>
      <!-- 색 red -->
    <h1>태그선택자1</h1>
    <h1>태그선택자2</h1>
    <!-- 색 brown -->
    <h3 class="title-brown">222</h3>
    <!-- 색 yellow-->
    <h3 id="title-yellow">333<h3>
    <h5>342432</h5>
    <h6>555</h6>
    <p>7777</p>
  </body>
</html>
```





* 웹 접근성 경험하고 느낀 점 작성

``흰 배경에서는 흐릿하게 보이던 글자와 사물들이 반전이나 흑백전환을 했을 때 잘 보이는 것이 신기하였고 시각 장애인분들의 인터넷환경을 체험해볼 수 있었던 좋은 기회였다고 생각합니다.``

