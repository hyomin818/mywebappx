import streamlit as st

st.set_page_config(
    page_title="MBTI 여행지 추천",
    page_icon="✈️",
    layout="centered"
)

# MBTI별 여행지
travel_data = {
    "INTJ": ["🏛️", "교토, 일본", "조용히 깊게 즐기는 감성 여행",
             "계획적으로 움직이면서 역사와 전통문화를 천천히 살펴보기 좋아요.",
             ["기요미즈데라", "아라시야마", "철학의 길"], "#E8DDF8"],
    "INTP": ["🔭", "아이슬란드", "신기한 자연을 탐구하는 여행",
             "빙하, 화산, 오로라처럼 호기심을 자극하는 독특한 자연환경이 가득해요.",
             ["레이캬비크", "골든서클", "블루라군"], "#DCECFB"],
    "ENTJ": ["🌆", "뉴욕, 미국", "에너지 넘치는 도시 여행",
             "볼거리와 할 일이 많아서 계획을 세우고 알차게 여행하기 좋아요.",
             ["맨해튼", "브루클린", "센트럴파크"], "#FFE0E7"],
    "ENTP": ["🎡", "런던, 영국", "새로운 자극이 가득한 여행",
             "역사와 현대문화가 함께 있어서 매일 새로운 분위기를 즐길 수 있어요.",
             ["코벤트가든", "캠든마켓", "대영박물관"], "#FFF0CB"],
    "INFJ": ["🌿", "제주도, 대한민국", "마음을 천천히 쉬게 하는 여행",
             "바다와 숲, 조용한 공간을 오가며 여유롭게 시간을 보내기 좋아요.",
             ["사려니숲길", "애월", "오름"], "#DDF3E4"],
    "INFP": ["🌷", "프라하, 체코", "동화 속을 걷는 감성 여행",
             "예쁜 골목과 오래된 건축물, 낭만적인 분위기를 느끼기 좋아요.",
             ["카를교", "프라하성", "구시가지"], "#FADFF0"],
    "ENFJ": ["💐", "바르셀로나, 스페인", "사람과 예술을 함께 즐기는 여행",
             "활기찬 분위기와 독특한 건축, 맛있는 음식까지 함께 즐길 수 있어요.",
             ["사그라다 파밀리아", "구엘공원", "람블라스 거리"], "#FFE1D6"],
    "ENFP": ["🎨", "방콕, 태국", "즉흥적으로 즐기는 알록달록 여행",
             "먹거리와 야시장, 카페와 문화체험까지 다양한 즐거움이 있어요.",
             ["짜뚜짝시장", "아이콘시암", "왓 아룬"], "#FFF0C7"],
    "ISTJ": ["🏰", "비엔나, 오스트리아", "차분하고 깔끔한 클래식 여행",
             "관광지를 차분하게 둘러보며 클래식한 분위기를 즐기기 좋아요.",
             ["쇤브룬궁전", "벨베데레", "빈 국립오페라극장"], "#EAE2F6"],
    "ISFJ": ["🍰", "삿포로, 일본", "포근하고 편안한 힐링 여행",
             "맛있는 음식과 편안한 풍경을 부담 없이 즐기기 좋아요.",
             ["오도리공원", "오타루", "모이와산"], "#E3F1FA"],
    "ESTJ": ["🚄", "싱가포르", "깔끔하고 알찬 도시 여행",
             "관광지를 효율적으로 둘러보면서 알찬 여행을 만들기 좋아요.",
             ["마리나베이", "가든스 바이 더 베이", "센토사"], "#DDF4EC"],
    "ESFJ": ["🎀", "파리, 프랑스", "예쁘고 특별한 추억 여행",
             "맛집과 쇼핑, 사진 명소가 많아 소중한 사람들과 추억을 만들기 좋아요.",
             ["에펠탑", "몽마르트르", "튈르리정원"], "#FFE0EA"],
    "ISTP": ["🏔️", "인터라켄, 스위스", "자유롭게 떠나는 여행",
             "웅장한 자연 속에서 자유롭게 움직이며 다양한 체험을 할 수 있어요.",
             ["융프라우", "하더쿨룸", "브리엔츠호수"], "#DCEFF1"],
    "ISFP": ["🌊", "발리, 인도네시아", "예쁜 풍경 속 느긋한 여행",
             "자연과 예술, 감성적인 공간 속에서 순간의 분위기를 즐기기 좋아요.",
             ["우붓", "스미냑", "울루와뚜"], "#E6F3DD"],
    "ESTP": ["🏄", "시드니, 호주", "활동적으로 즐기는 여행",
             "도시와 해변을 함께 즐길 수 있고 야외에서 할 수 있는 것도 많아요.",
             ["본다이비치", "오페라하우스", "달링하버"], "#DDEBFF"],
    "ESFP": ["🌺", "하와이, 미국", "신나고 화려한 휴양 여행",
             "예쁜 바다와 쇼핑, 맛집, 다양한 즐거움을 함께 느낄 수 있어요.",
             ["와이키키", "다이아몬드헤드", "알라모아나"], "#FFE4D2"]
}

# 화면 디자인
st.markdown("""
<style>
.stApp {
    background: linear-gradient(180deg, #fff7fb 0%, #fffdf8 100%);
}
.block-container {
    max-width: 760px;
    padding-top: 35px;
}
.title {
    text-align: center;
    color: #ff78ad;
    font-size: 42px;
    font-weight: 800;
    margin-bottom: 5px;
}
.subtitle {
    text-align: center;
    color: #8c7180;
    font-size: 17px;
    margin-bottom: 28px;
}
.box {
    background: white;
    border: 2px solid #ffd9e8;
    border-radius: 25px;
    padding: 24px;
    box-shadow: 0 8px 25px rgba(255, 140, 180, 0.12);
}
.result {
    border-radius: 28px;
    padding: 30px 22px;
    margin-top: 25px;
    text-align: center;
    border: 3px solid white;
    box-shadow: 0 10px 30px rgba(80, 60, 80, 0.12);
}
.reason {
    background: rgba(255,255,255,0.75);
    border-radius: 18px;
    padding: 16px;
    margin: 18px 0;
    color: #5f5058;
    line-height: 1.7;
}
.spot {
    display: inline-block;
    background: white;
    border-radius: 30px;
    padding: 8px 14px;
    margin: 4px;
    color: #735d69;
}
.footer {
    text-align: center;
    color: #b69aa9;
    margin-top: 35px;
}
.stButton > button {
    width: 100%;
    border-radius: 30px;
    border: 0;
    background: #ff91bb;
    color: white;
    font-weight: 800;
    font-size: 16px;
    padding: 10px;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">🧳🌸 MBTI 여행지 추천 ✈️</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">내 성격에 찰떡인 여행지는 어디일까? 💕</div>',
    unsafe_allow_html=True
)

st.markdown('<div class="box">', unsafe_allow_html=True)
st.markdown("### 💌 나의 MBTI를 골라주세요")

mbti = st.selectbox(
    "MBTI",
    ["선택해주세요 💕"] + list(travel_data.keys()),
    label_visibility="collapsed"
)

mood = st.selectbox(
    "여행 분위기",
    ["아무거나 좋아요", "🌿 힐링", "🎨 감성", "🎡 신나는 여행", "🏛️ 문화·도시"]
)

companion = st.selectbox(
    "누구와 가나요?",
    ["상관없어요", "🧸 혼자", "👭 친구", "👨‍👩‍👧 가족"]
)

show_result = st.button("💖 나에게 어울리는 여행지 보기")
st.markdown('</div>', unsafe_allow_html=True)

if show_result:
    if mbti == "선택해주세요 💕":
        st.warning("MBTI를 먼저 골라주세요! 🌷")
    else:
        emoji, place, subtitle, reason, spots, bg = travel_data[mbti]

        spot_html = ""
        for spot in spots:
            spot_html += '<span class="spot">' + spot + '</span>'

        # HTML 안쪽에 공백을 넣으면 일부 Streamlit 환경에서
        # 내부 내용이 코드처럼 보일 수 있어서 한 줄 구조로 만들어 줍니다.
        result_html = (
            '<div class="result" style="background:' + bg + ';">'
            '<div style="font-size:60px;">' + emoji + '</div>'
            '<div style="color:#9a7a8b; font-weight:700;">'
            + mbti + '에게 추천하는 여행지</div>'
            '<div style="font-size:32px; font-weight:800; color:#574651; margin:6px 0;">'
            + place + '</div>'
            '<div style="font-size:17px; font-weight:700; color:#8b6878;">'
            + subtitle + '</div>'
            '<div class="reason">'
            '💕 <b>추천 이유</b><br>'
            + reason +
            '</div>'
            '<div style="color:#8f6b7c; font-weight:800; margin-bottom:8px;">'
            '📍 꼭 가볼 곳</div>'
            '<div>' + spot_html + '</div>'
            '</div>'
        )

        st.markdown(result_html, unsafe_allow_html=True)

        st.success("오늘은 여기로 떠나볼까요? 🧳💕")
        st.caption(
            "※ MBTI 추천은 재미로 즐겨주세요! 실제 여행 전에는 날씨와 운영시간 등을 확인해 주세요."
        )

st.markdown(
    '<div class="footer">Made with 💗 · 오늘도 귀여운 여행 되세요! 🌷</div>',
    unsafe_allow_html=True
)
