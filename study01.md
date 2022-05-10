# Streamlit Study

> 스트림릿 라이브러리 공부 -1일차



## 공부하는 이유

- 팀 프로젝트 

멀티 캠퍼스 최종 팀 프로젝트에서 웹서비스를 구현할 때의 방법으로 스트림릿을 선정하였음. 그러나 나는 스트림릿을 들어보기만 했을 뿐, 한 번도 사용해 본 경험이 없음. 따라서 사용법을 익혀야 할 필요성을 느꼈음. 



- 언젠가를 위해

스트림릿이 무엇인지, 어떤 식으로 활용되는지 눈대중으로 구글링해본 결과 시각화하는 데에 상당히 유용하게 쓸 수 있다고 판단함. 어떤 결과를 시연할 때 스트림릿을 이용하면 매우 편리할 것 같음. 그리 어렵지 않은 데다가, 무엇보다도......있어 보임^^. 아무튼 그 '언젠가'를 위해서 파이팅! ψ(｀∇´)ψ



### Streamlit API

> 공식문서에 소개된 스트림릿 API를 하나씩 살펴보자. 실습은 test.py 파일에서!

```python
# 앨리아스 약자로 "st"를 사용함!
import streamlit as st
```



1. __st.write __: 기본적으로 사용되는 명령어. 

> Write arguments to the app.
>
> - You can pass in multiple arguments, all of which will be written.

- 사용방법 : `st.write()`

- 예시:

```python
import streamlit as st

st.write("Hello, Steamlit!")
st.write('''
# Markdown
## Markdown2
''')
```



2. __st.markdown__

> Display string formatted as Markdown.

- 사용방법 : `st.markdown()`
- 마크다운 문법이 지원된다. 
