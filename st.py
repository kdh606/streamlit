import streamlit as st  # streamlit 라이브러리 임포트

# 타이틀 텍스트 출력
st.title('첫번째 웹 어플 만들기 👋🎥')

# 텍스트 출력
st.write('# 1. Markdown 텍스트 작성하기')

# Markdown 문법으로 작성된 문장 출력
st.markdown(
'''
# 마크다운 헤더1
- 마크다운 목록1. **굵게** 표시
- 마크다운 목록2. *기울임* 표시
    - 마크다운 목록2-1
    - 마크다운 목록2-2

## 마크다운 헤더2
- [네이버](https://naver.com)
- [구글](https://google.com)

### 마크다운 헤더3
일반 텍스트
'''
)