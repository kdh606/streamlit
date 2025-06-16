import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import altair as alt
import plotly.express as px

st.set_page_config(page_title="배달의민족 조사", page_icon="🍽️", layout="centered")

# 제목
st.title("배달의민족에 대한 간단한 조사")

# 부제
st.subheader("평소에 자주 애용하는 배달의민족에 대해 조사해보았다.")

# 이미지
st.image("data:image/jpeg;base64,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" \
, caption="배달의민족 로고")

# 기본 텍스트
st.write("배달의민족은 대한민국 대표 배달 앱 중 하나로, 사용자가 스마트폰을 통해 음식 배달을 간편하게 요청할 수 있도록 도와주는 서비스이다.")

# 구분선
st.divider()

# 주요 기능 정리
st.header("앱의 주요 특징")

st.markdown("""
- 다양한 음식점 입점
- 실시간 배달 추적 가능
- 리뷰 및 별점 기반의 신뢰성 확보
- 쿠폰 및 할인 혜택 제공
""")

# 라텍스 수식 예시
st.subheader("배달 요금 산정 공식 (예시)")
st.latex(r"\text{총 요금} = \text{메뉴 가격} + \text{배달료} + (\text{거리} \times 0.5)")

# 코드 예시
st.subheader("예시 코드 (단순 시뮬레이션)")
st.code("""
def calculate_delivery_price(price, distance):
    return price + 3000 + (distance * 500)
""", language="python")

# st.echo 사용 (코드+실행 동시 출력)
with st.echo():
    def review_summary():
        st.write("사용자 리뷰는 전반적으로 긍정적이었다.")
    review_summary()

# 알림 메시지 종류
st.subheader("리뷰 요약")
st.success("배달 속도에 대한 만족도가 높았음.")
st.info("앱 사용 편의성에 대한 긍정적인 평가 다수.")
st.warning("일부 지역은 입점 가게 수가 부족함.")
st.error("간혹 배달 오류 발생 사례 존재.")

# 차트용 데이터
df = pd.DataFrame({
    '요일': ['월', '화', '수', '목', '금', '토', '일'],
    '주문 수': [12, 15, 14, 20, 30, 45, 40]
})
요일_순서 = ['월', '화', '수', '목', '금', '토', '일']
df['요일'] = pd.Categorical(df['요일'], categories=요일_순서, ordered=True)

st.subheader("요일별 평균 주문 수")
st.line_chart(df.set_index('요일'))
st.area_chart(df.set_index('요일'))
st.bar_chart(df.set_index('요일'))

# 산점도용 데이터
np.random.seed(42)
scatter_df = pd.DataFrame({
    '배달 시간': np.random.normal(30, 5, 50),
    '리뷰 수': np.random.randint(10, 100, 50)
})
st.subheader("배달 시간과 리뷰 수 관계 (샘플 데이터)")
st.scatter_chart(scatter_df)

# 지도 시각화
st.subheader("주문 발생 지역 예시 (서울 시청 중심)")
map_data = pd.DataFrame({
    'lat': [37.5665 + np.random.normal(0, 0.01) for _ in range(20)],
    'lon': [126.9780 + np.random.normal(0, 0.01) for _ in range(20)],
})
st.map(map_data)

# Matplotlib 차트
st.subheader("주간 주문 변화 (Matplotlib)")
fig, ax = plt.subplots()
ax.plot(df['요일'], df['주문 수'], marker='o')
ax.set_title("주간 주문 변화")
ax.set_ylabel("주문 수")
st.pyplot(fig)

# Altair 차트
st.subheader("Altair 차트")
alt_chart = alt.Chart(df).mark_bar().encode(
    x='요일',
    y='주문 수',
    tooltip=['요일', '주문 수']
).interactive()
st.altair_chart(alt_chart, use_container_width=True)

# Plotly 차트
st.subheader("Plotly 차트")
fig2 = px.pie(df, names='요일', values='주문 수', title='요일별 주문 비율')
st.plotly_chart(fig2)

# 비디오 (광고 영상)
st.subheader("광고 영상")
st.video("https://youtu.be/36JvP5pw3po?si=rLb0w_1JGlSERhNY")

# 캡션
st.divider()
st.caption("이 조사는 2025년 기준으로 작성되었으며, 일부 데이터는 임의 생성되었음.")

