import streamlit as st
import random

st.set_page_config(
    page_title="MBTI 여행지 추천 💕",
    page_icon="✈️",
    layout="centered"
)

# -----------------------------
# 여행지 데이터
# -----------------------------
travel_data = {
    "INTJ": {
        "emoji": "🏛️",
        "title": "교토, 일본",
        "subtitle": "조용히 깊게 즐기는 감성 여행",
        "reason": "계획적으로 움직이면서 역사, 건축, 전통문화를 천천히 살펴보기 좋아요.",
        "spots": ["기요미즈데라", "아라시야마", "철학의 길"],
        "color": "#E8DDF8"
    },
    "INTP": {
        "emoji": "🔭",
        "title": "아이슬란드",
        "subtitle": "신기한 자연을 탐구하는 여행",
        "reason": "빙하, 화산, 오로라처럼 호기심을 자극하는 독특한 자연환경이 가득해요.",
        "spots": ["레이캬비크", "골든서클", "블루라군"],
        "color": "#DCECFB"
    },
    "ENTJ": {
        "emoji": "🌆",
        "title": "뉴욕, 미국",
        "subtitle": "에너지 넘치는 도시 정복 여행",
        "reason": "볼거리와 할 일이 많아 빠르게 계획을 세우고 알차게 여행하기 좋아요.",
        "spots": ["맨해튼", "브루클린", "센트럴파크"],
        "color": "#FFE0E7"
    },
    "ENTP": {
        "emoji": "🎡",
        "title": "런던, 영국",
        "subtitle": "새로운 자극이 가득한 여행",
        "reason": "역사와 현대문화가 함께 있어 매일 다른 분위기를 즐길 수 있어요.",
        "spots": ["코벤트가든", "캠든마켓", "대영박물관"],
        "color": "#FFF0CB"
    },
    "INFJ": {
        "emoji": "🌿",
        "title": "제주도, 대한민국",
        "subtitle": "마음을 천천히 쉬게 하는 여행",
        "reason": "바다와 숲, 조용한 카페를 오가며 혼자만의 시간을 보내기 좋아요.",
        "spots": ["사려니숲길", "애월", "오름"],
        "color": "#DDF3E4"
    },
    "INFP": {
        "emoji": "🌷",
        "title": "프라하, 체코",
        "subtitle": "동화 속을 걷는 감성 여행",
        "reason": "예쁜 골목과 오래된 건축물, 낭만적인 야경이 감성적인 여행과 잘 어울려요.",
        "spots": ["카를교", "프라하성", "구시가지"],
        "color": "#FADFF0"
    },
    "ENFJ": {
        "emoji": "💐",
        "title": "바르셀로나, 스페인",
        "subtitle": "사람과 예술을 함께 즐기는 여행",
        "reason": "활기찬 분위기와 독특한 건축, 맛있는 음식까지 함께 즐길 수 있어요.",
        "spots": ["사그라다 파밀리아", "구엘공원", "람블라스 거리"],
        "color": "#FFE1D6"
    },
    "ENFP": {
        "emoji": "🎨",
        "title": "방콕, 태국",
        "subtitle": "즉흥적으로 즐기는 알록달록 여행",
        "reason": "먹거리, 야시장, 카페, 문화체험까지 선택지가 많아 지루할 틈이 없어요.",
        "spots": ["짜뚜짝시장", "아이콘시암", "왓 아룬"],
        "color": "#FFF0C7"
    },
    "ISTJ": {
        "emoji": "🏰",
        "title": "비엔나, 오스트리아",
        "subtitle": "차분하고 깔끔한 클래식 여행",
        "reason": "교통이 편리하고 볼거리가 체계적으로 모여 있어 안정적인 여행을 즐기기 좋아요.",
        "spots": ["쇤브룬궁전", "벨베데레", "빈 국립오페라극장"],
        "color": "#EAE2F6"
    },
    "ISFJ": {
        "emoji": "🍰",
        "title": "삿포로, 일본",
        "subtitle": "포근하고 편안한 힐링 여행",
        "reason": "맛있는 음식과 조용한 풍경을 부담 없이 즐기기 좋아요.",
        "spots": ["오도리공원", "오타루", "모이와산"],
        "color": "#E3F1FA"
    },
    "ESTJ": {
        "emoji": "🚄",
        "title": "싱가포르",
        "subtitle": "깔끔하고 알찬 도시 여행",
        "reason": "이동이 편리하고 관광지가 잘 정리되어 있어 짧은 일정도 효율적으로 즐길 수 있어요.",
        "spots": ["마리나베이", "가든스 바이 더 베이", "센토사"],
        "color": "#DDF4EC"
    },
    "ESFJ": {
        "emoji": "🎀",
        "title": "파리, 프랑스",
        "subtitle": "예쁘고 특별한 추억을 만드는 여행",
        "reason": "맛집, 쇼핑, 사진 명소가 많아 소중한 사람들과 추억을 남기기 좋아요.",
        "spots": ["에펠탑", "몽마르트르", "튈르리정원"],
        "color": "#FFE0EA"
    },
    "ISTP": {
        "emoji": "🏔️",
        "title": "인터라켄, 스위스",
        "subtitle": "자유롭게 떠나는 액티비티 여행",
        "reason": "웅장한 자연 속에서 원하는 만큼 자유롭게 움직이고 다양한 체험을 할 수 있어요.",
        "spots": ["융프라우", "하더쿨룸", "브리엔츠호수"],
        "color": "#DCEFF1"
    },
    "ISFP": {
        "emoji": "🌊",
        "title": "발리, 인도네시아",
        "subtitle": "예쁜 풍경 속 느긋한 여행",
        "reason": "자연과 예술, 감성적인 공간이 많아 순간의 분위기를 즐기기 좋아요.",
        "spots": ["우붓", "스미냑", "울루와뚜"],
        "color": "#E6F3DD"
    },
    "ESTP": {
        "emoji": "🏄",
        "title": "시드니, 호주",
        "subtitle": "활동적으로 즐기는 짜릿한 여행",
        "reason": "도시와 해변을 동시에 즐길 수 있고 야외 활동도 풍부해요.",
        "spots": ["본다이비치", "오페라하우스", "달링하버"],
        "color": "#DDEBFF"
    },
    "ESFP": {
        "emoji": "🌺",
        "title": "하와이, 미국",
        "subtitle": "신나고 화려한 휴양 여행",
        "reason": "예쁜 바다, 쇼핑, 맛집, 액티비티까지 밝고 즐거운 분위기를 가득 느낄 수 있어요.",
        "spots": ["와이키키", "다이아몬드헤드", "알라모아나"],
        "color": "#FFE4D2"
    }
}

cute_messages = [
    "오늘은 어디로 떠나볼까요? ✈️💕",
    "당신의 MBTI에 꼭 맞는 여행지를 찾아드릴게요 🌷",
    "여행 가방 챙길 준비 완료! 🧳✨",
    "귀여운 여행 운세가 도착했어요 💌"
]

# -----------------------------
# CSS
# -----------------------------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(180deg, #fff8fc 0%, #fffdf8 50%, #f8fbff 100%);
}

.block-container {
    max-width: 780px;
    padding-top: 2rem;
    padding-bottom: 4rem;
}

.hero {
    text-align: center;
    padding: 28px 18px 18px 18px;
}

.hero h1 {
    font-size: 2.65rem;
    margin-bottom: 8px;
    color: #ff6fa9;
    letter-spacing: -1px;
}

.hero p {
    font-size: 1.03rem;
    color: #806979;
    margin-top: 0;
}

.cute-box {
    background: rgba(255,255,255,0.82);
    border: 2px solid #ffd6e7;
    border-radius: 28px;
    padding: 22px;
    box-shadow: 0 10px 30px rgba(255, 143, 184, 0.12);
    margin-bottom: 18px;
}

.result-card {
    border-radius: 30px;
    padding: 28px;
    text-align: center;
    box-shadow: 0 12px 35px rgba(106, 86, 120, 0.12);
    margin-top: 18px;
    border: 3px solid rgba(255,255,255,0.9);
}

.result-emoji {
    font-size: 4rem;
    margin-bottom: 8px;
}

.result-title {
    font-size: 2rem;
    font-weight: 800;
    color: #574451;
    margin-bottom: 6px;
}

.result-subtitle {
    font-size: 1.08rem;
    font-weight: 700;
    color: #8c6578;
    margin-bottom: 18px;
}

.reason {
    background: rgba(255,255,255,0.72);
    border-radius: 20px;
    padding: 17px;
    color: #604f59;
    line-height: 1.75;
    margin: 15px 0;
}

.spot-chip {
    display: inline-block;
    background: white;
    padding: 8px 13px;
    margin: 4px;
    border-radius: 999px;
    font-size: 0.92rem;
    color: #715b68;
    box-shadow: 0 4px 12px rgba(80,60,70,0.07);
}

.small-title {
    font-size: 0.95rem;
    font-weight: 800;
    color: #8f6b7c;
    margin-top: 18px;
    margin-bottom: 7px;
}

.footer {
    text-align:center;
    color:#b093a2;
    font-size:0.85rem;
    margin-top:35px;
}

div[data-baseweb="select"] > div {
    border-radius: 18px !important;
    border-color: #ffc8dc !important;
}

.stButton > button {
    width: 100%;
    border: none;
    border-radius: 999px;
    padding: 0.75rem 1rem;
    font-weight: 800;
    font-size: 1rem;
    background: linear-gradient(90deg, #ff8fbd, #ffb09d);
    color: white;
    box-shadow: 0 8px 18px rgba(255, 126, 171, 0.24);
}

.stButton > button:hover {
    transform: translateY(-1px);
    border: none;
    color: white;
}

div[data-testid="stMetric"] {
    background: white;
    border-radius: 18px;
    padding: 12px;
    border: 1px solid #ffe0ec;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# 화면
# -----------------------------
st.markdown("""
<div class="hero">
    <div style="font-size:3.7rem;">🧳🌸✈️</div>
    <h1>MBTI 여행지 추천</h1>
    <p>내 성격에 찰떡인 여행지는 어디일까? 💗</p>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="cute-box">', unsafe_allow_html=True)
st.markdown("### 💌 나의 MBTI를 골라주세요")

mbti = st.selectbox(
    "MBTI 선택",
    ["선택해주세요 💕"] + list(travel_data.keys()),
    label_visibility="collapsed"
)

col1, col2 = st.columns(2)
with col1:
    mood = st.selectbox(
        "여행 분위기",
        ["아무거나 좋아요", "🌿 힐링", "🎨 감성", "🎡 신나는 여행", "🏛️ 문화·도시"]
    )
with col2:
    companion = st.selectbox(
        "누구와 가나요?",
        ["상관없어요", "🧸 혼자", "👭 친구", "👨‍👩‍👧 가족"]
    )

recommend = st.button("💖 나에게 어울리는 여행지 보기")
st.markdown('</div>', unsafe_allow_html=True)

if recommend:
    if mbti == "선택해주세요 💕":
        st.warning("MBTI를 먼저 선택해 주세요! 🌷")
    else:
        item = travel_data[mbti]

        st.balloons()

        st.markdown(
            f"""
            <div class="result-card" style="background:{item['color']};">
                <div class="result-emoji">{item['emoji']}</div>
                <div style="font-size:0.95rem; color:#9a7a89; font-weight:700;">
                    {mbti}에게 추천하는 여행지
                </div>
                <div class="result-title">{item['title']}</div>
                <div class="result-subtitle">{item['subtitle']}</div>

                <div class="reason">
                    💕 <b>추천 이유</b><br>
                    {item['reason']}
                </div>

                <div class="small-title">📍 꼭 가볼 곳</div>
                <div>
                    {''.join([f'<span class="spot-chip">{spot}</span>' for spot in item['spots']])}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.write("")
        st.success(random.choice(cute_messages))

        c1, c2, c3 = st.columns(3)
        with c1:
            st.metric("MBTI", mbti)
        with c2:
            st.metric("분위기", mood.replace("🌿 ", "").replace("🎨 ", "").replace("🎡 ", "").replace("🏛️ ", ""))
        with c3:
            st.metric("동행", companion.replace("🧸 ", "").replace("👭 ", "").replace("👨‍👩‍👧 ", ""))

        st.caption("※ 추천 결과는 재미로 즐겨주세요. 여행 전에는 실제 날씨, 안전 정보, 운영시간 등을 확인해 주세요.")

st.markdown("""
<div class="footer">
    Made with 💗 and Streamlit · 오늘도 귀여운 여행 되세요! 🌷
</div>
""", unsafe_allow_html=True)
