import streamlit as st
import pandas as pd
from PIL import Image

# -------------------------------------------------------------
# 0. 페이지 기본 설정 및 스타일 정의
# -------------------------------------------------------------
st.set_page_config(
    page_title="경주 옥산서원 현장 탐구 도감",
    page_icon="🏯",
    layout="wide"
)

# Custom CSS
st.markdown("""
    <style>
    .main-title { font-size: 2.3rem; font-weight: bold; color: #1B4F72; }
    .sub-title { font-size: 1.15rem; color: #5D6D7E; margin-bottom: 20px; }
    .card { background-color: #F2F4F4; padding: 22px; border-radius: 12px; margin-bottom: 20px; border-left: 6px solid #2E86C1; }
    .highlight { font-weight: bold; color: #B9770E; }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">🏯 경주 옥산서원(玉山書院) 현장 탐구 도감</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">조선시대 사액서원과 성리학의 명소, 회재 이언적 선생의 학학 세계를 탐구해보세요!</div>', unsafe_allow_html=True)
st.divider()

# -------------------------------------------------------------
# 사이드바 메뉴 (옥산서원 단독 주제 구성)
# -------------------------------------------------------------
st.sidebar.title("🏯 옥산서원 탐구 메뉴")
menu = st.sidebar.radio(
    "탐구할 항목을 선택하세요:",
    [
        "1. 📖 옥산서원 개요 & 교육사적 의의",
        "2. 🏛️ 주요 공간 및 문화재 가이드",
        "3. 🎯 옥산서원 현장 탐구 퀴즈",
        "4. 💬 AI 회재 이언적 선생과의 대담",
        "5. 📸 옥산서원 답사 인증 & 소감 제출"
    ]
)

# -------------------------------------------------------------
# 1. 옥산서원 개요 & 교육사적 의의
# -------------------------------------------------------------
if menu == "1. 📖 옥산서원 개요 & 교육사적 의의":
    st.header("📖 옥산서원의 개요 및 교육사적 의의")
    
    st.markdown("""
    <div class="card">
    <h3>🏛️ 옥산서원(玉山書院)이란?</h3>
    <p>옥산서원은 조선 후기 <b>동방 5현(東方五賢)</b>으로 추앙받는 대유학자 <b>회재 이언적(李彥迪, 1491~1553)</b> 선생의 학덕을 기리기 위해 1572년에 창건된 대표적인 사액서원입니다.</p>
    <p>2019년 유네스코 세계문화유산인 <b>'한국의 서원'</b>으로 등재되었으며, 조선 시대 강학(講學)과 존현(尊賢)의 기능을 수행하며 선비들의 학문 전통을 이끌어온 지방 사학 교육의 핵심 현장입니다.</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("💡 교육사적 의의")
        st.markdown("""
        * **성리학적 강학 체계의 실천**: 성학을 익히고 학문을 탐구하던 지방 사학 기관의 대표적 모델입니다.
        * **동방 5현 추모 (존현 기능)**: 조선 중기 성리학 발전에 기여한 이언적 선생의 덕행을 계승하는 중심 역할을 하였습니다.
        * **자연과 학문의 일치**: 서원 앞 계곡과 자연을 학문修養(수양)의 장으로 통합한 조선 선비 문화의 공간성을 보여줍니다.
        """)
        
    with col2:
        st.subheader("📜 회재 이언적 선생 (1491~1553)")
        st.markdown("""
        * **조선 성리학의 개척자**: 퇴계 이황 선생 등 후대 성리학자들에게 큰 영향을 미친 사상가입니다.
        * **주요 사상**: 이기론(理氣論) 연구에 선구적 역할을 하였으며, 배움과 삶에서의 '경(敬)'과 '인(仁)'의 실천을 강조했습니다.
        * **배향**: 김굉필, 정여창, 조광조, 이황과 함께 문묘에 배향된 동방 5현에 속합니다.
        """)

# -------------------------------------------------------------
# 2. 주요 공간 및 문화재 가이드
# -------------------------------------------------------------
elif menu == "2. 🏛️ 주요 공간 및 문화재 가이드":
    st.header("🏛️ 옥산서원의 주요 공간 및 보물 가이드")
    st.write("옥산서원 현장을 직접 둘러보며 각 공간이 지닌 교육적 의미를 살펴보세요.")
    
    c1, c2 = st.columns(2)
    
    with c1:
        st.markdown("""
        <div class="card">
        <h4>1. 구인당 (求仁堂) - 강학 공간</h4>
        <p>서원의 핵심 건물로, 원생들이 모여 성리학적 진리와 학문을 토론하고 강의를 듣던 강당입니다. '인(仁)을 구한다'는 뜻을 지니고 있습니다.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="card">
        <h4>2. 독락당 (獨樂堂) - 회재 선생의 사랑채</h4>
        <p>회재 이언적 선생이 관직에서 물러난 뒤 홀로 자연을 벗 삼아 정진하고 학문의 즐거움을 누리던 공간입니다.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="card">
        <h4>3. 세심대 (洗心臺) - 수양의 계곡 바위</h4>
        <p>옥산서원 입구 계곡에 위치한 너럭바위로, '마음을 깨끗이 씻고 학문과 자연을 대한다'는 성리학적 수양의 가치를 담고 있습니다.</p>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div class="card">
        <h4>4. 암각서 (岩刻書)</h4>
        <p>세심대 주변과 서원 안팎의 바위에 새겨진 글씨들로, 조선 선비들의 학문적 기개와 자연관을 보여줍니다.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="card">
        <h4>5. 한호(한석봉)의 현판</h4>
        <p>조선 최고의 명필 한석봉이 직접 쓴 '옥산서원' 현판과 퇴계 이황 선생의 글씨 등 보물급 서예 유산을 간직하고 있습니다.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="card">
        <h4>6. 정혜사지 십삼층석탑 & 고문서</h4>
        <p>서원 인근의 정혜사지 십삼층석탑(국보)과 회재 선생의 친필 원고 및 다양한 고문서가 소장되어 있습니다.</p>
        </div>
        """, unsafe_allow_html=True)

# -------------------------------------------------------------
# 3. 옥산서원 현장 탐구 퀴즈
# -------------------------------------------------------------
elif menu == "3. 🎯 옥산서원 현장 탐구 퀴즈":
    st.header("🎯 옥산서원 현장 탐구 퀴즈")
    st.write("옥산서원 현장을 살펴보고 아래 질문들의 정답을 맞춰보세요!")
    
    # Q1
    st.subheader("Q1. 옥산서원에 배향된 조선시대 대표 유학자는 누구일까요?")
    q1 = st.radio("선택하세요:", ["1) 퇴계 이황", "2) 율곡 이이", "3) 회재 이언적", "4) 다산 정약용"], key="q1")
    if st.button("Q1 정답 확인"):
        if "3)" in q1:
            st.success("정답입니다! 옥산서원은 회재 이언적(李彥迪) 선생의 학덕을 기리기 위해 설립된 사액서원입니다.")
        else:
            st.error("오답입니다. 다시 생각해보세요!")
            
    st.divider()
    
    # Q2
    st.subheader("Q2. 옥산서원에서 원생들이 모여 학문을 배우고 토론하던 대표적인 강학(講學) 공간의 이름은?")
    q2 = st.selectbox("선택하세요:", ["선택하세요", "독락당", "구인당", "관가정", "경주향교"], key="q2")
    if q2 == "구인당":
        st.success("정답입니다! '구인당(求仁堂)'은 '인(仁)을 구한다'는 뜻의 강학 공간입니다.")
    elif q2 != "선택하세요":
        st.error("오답입니다. 서원 중앙의 강당 이름을 떠올려보세요.")

    st.divider()

    # Q3
    st.subheader("Q3. 옥산서원 입구 계곡 바위에 새겨진 '세심대(洗心臺)'의 한자적 뜻은 무엇일까요?")
    q3_input = st.text_input("의미를 간단히 적어보세요 (키워드 예시: 마음, 씻다)")
    if st.button("Q3 정답 확인"):
        if "마음" in q3_input and "씻" in q3_input:
            st.success("정답입니다! 세심대는 '마음을 깨끗이 씻고 학문과 자연을 대한다'는 뜻을 담고 있습니다.")
        else:
            st.info("💡 힌트: '마음을 씻는다'는 의미가 들어가야 합니다.")

# -------------------------------------------------------------
# 4. AI 회재 이언적 선생과의 대담
# -------------------------------------------------------------
elif menu == "4. 💬 AI 회재 이언적 선생과의 대담":
    st.header("💬 AI 회재 이언적 선생과의 학문 대담")
    st.write("조선 시대 성리학의 대가 회재 이언적 선생에게 옥산서원과 학문관에 대한 질문을 건네보세요.")
    
    user_input = st.text_input("선생님께 드릴 질문을 입력하세요 (예: 세심대와 독락당에서 강조하고자 하신 공부의 자세는 무엇입니까?)")
    
    if st.button("질문 보내기"):
        if user_input:
            st.chat_message("user").write(user_input)
            with st.chat_message("assistant"):
                st.write(f"**[회재 이언적]**: 반갑네, 유생. 자네가 물은 '{user_input}'에 대해 말해주겠네.")
                st.write("""
                학문이란 단순히 글을 외우는 것이 아니라, **거경궁리(居敬窮理)**하여 자신의 마음을 바르게 씻고(세심), 
                구인당에서 학반들과 함께 인(仁)을 구하며 삶에서 실천하는 데 있다네. 
                독락당에서 홀로 자연의 이치를 관조하듯, 이곳 옥산서원에서 참된 배움의 가치를 온전히 깨닫기를 바라네.
                """)
        else:
            st.warning("질문을 입력해주세요.")

# -------------------------------------------------------------
# 5. 📸 옥산서원 답사 인증 & 소감 제출
# -------------------------------------------------------------
elif menu == "5. 📸 옥산서원 답사 인증 & 소감 제출":
    st.header("📸 옥산서원 현장 인증샷 및 탐구 소감 제출")
    st.write("옥산서원 현장에서 직접 촬영한 사진과 탐구한 내용을 기록하세요.")
    
    with st.form("oksan_form"):
        student_id = st.text_input("학번 / 성명")
        location_type = st.selectbox("촬영 장소 / 관찰 공간", ["구인당", "독락당", "세심대 및 계곡", "한석봉 현판 / 암각서", "기타 서원 전경"])
        
        uploaded_file = st.file_uploader("옥산서원 현장 사진 업로드", type=['png', 'jpg', 'jpeg'])
        reflection = st.text_area("옥산서원을 답사하며 느낀 점이나 배운 점을 작성하세요.")
        
        submitted = st.form_submit_button("답사 기록 제출하기")
        
        if submitted:
            if student_id and reflection:
                st.success(f"🎉 {student_id}님의 옥산서원 답사 기록이 성공적으로 제출되었습니다!")
                if uploaded_file is not None:
                    image = Image.open(uploaded_file)
                    st.image(image, caption=f"{student_id}님의 {location_type} 인증샷", use_column_width=True)
                st.info(f"**작성한 소감**: {reflection}")
            else:
                st.warning("학번/성명과 소감 내용을 모두 작성해주셔야 제출됩니다.")
