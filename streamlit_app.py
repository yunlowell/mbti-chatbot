import streamlit as st

# 🌸 큐티뽀티 스타일 적용
st.set_page_config(page_title="MBTI 심리테스트 & 내 성격과 같은 챗봇과 대화하기", page_icon="🌸")

# 💄 Custom CSS
st.markdown("""
<!-- Google Fonts 가져오기 -->
<link href="https://fonts.googleapis.com/css2?family=Gowun+Dodum&family=Jua&display=swap" rel="stylesheet">

<style>
    /* 전체 앱에 부드러운 기본 글꼴 적용 */
    .stApp {
        font-family: 'Gowun Dodum', sans-serif;
        background-color: #FFF0F5;
        color: #000000;
    }

    /* 본문 마크다운, 질문, 버튼 등 모두 기본 글꼴로 통일 */
    html, body, [class*="st-"], [data-testid="stMarkdownContainer"] {
        font-family: 'Gowun Dodum', sans-serif !important;
        color: #000000 !important;
    }

    /* 제목은 귀엽고 큰 폰트로 강조 */
    h1, h2, h3, .stTitle {
        font-family: 'Jua', sans-serif !important;
        color: #e75480 !important;
        font-weight: bold;
    }

    /* radio 버튼 스타일 개선 (작고 귀엽게) */
    div[role="radiogroup"] > label {
        background-color: #ffeef4;
        padding: 2px 5px;
        margin: 4px 0;
        border-radius: 12px;
        border: 1px solid #f5c2c7;
        cursor: pointer;
        display: block;
        font-size: 12px;
        color: #000000 !important;
    }

    div[role="radiogroup"] > label:hover {
        background-color: #ffdde7;
        border-color: #f192a1;
    }

    div[role="radiogroup"] > label[data-selected="true"] {
        background-color: #f5c2c7 !important;
        color: #000000 !important;
        border-color: #ff95b5;
        font-weight: bold;
    }

    /* 버튼 스타일 */
    div.stButton > button {
        background-color: #ffb6c1;
        color: #000000;
        border-radius: 12px;
        border: 2px solid #ff8da6;
        padding: 10px 20px;
        font-weight: bold;
        transition: all 0.2s ease-in-out;
    }

    div.stButton > button:hover {
        background-color: #ffa6b8;
        border-color: #ff6f91;
        transform: scale(1.02);
    }
    </style>
""", unsafe_allow_html=True)



# 🌷 타이틀
st.title("🌸 MBTI 심리테스트")
st.write("20개의 문항에 답하고 당신의 성격 유형을 알아보신 후 같은 mbti 챗봇과 대화해 보세요!")

# 🧠 점수 초기화
scores = {
    "E": 0, "I": 0,
    "S": 0, "N": 0,
    "T": 0, "F": 0,
    "J": 0, "P": 0
}

# 📋 문항: (질문, "그렇다" → 유형, "아니다" → 반대유형)
questions = [
    ("나는 새로운 사람을 만나는 것이 즐겁다.", "E", "I"),
    ("사람들과 오래 있으면 에너지가 떨어진다.", "I", "E"),
    ("중요한 결정을 할 때 주로 다른 사람들과 상의한다.", "E", "I"),
    ("생각을 말로 표현하는 것이 쉽다.", "E", "I"),
    ("나만의 공간이 꼭 필요하다.", "I", "E"),
    ("나는 세부 사항에 주의를 기울이는 편이다.", "S", "N"),
    ("상상력이 풍부하고 추상적인 아이디어를 좋아한다.", "N", "S"),
    ("현재에 집중하는 편이다.", "S", "N"),
    ("“왜”보다는 “어떻게”에 더 관심이 많다.", "S", "N"),
    ("직감이 잘 맞는다고 느낀다.", "N", "S"),
    ("결정을 내릴 때 감정보다 논리가 중요하다.", "T", "F"),
    ("타인의 감정을 먼저 고려한다.", "F", "T"),
    ("나는 공정함을 중요시한다.", "T", "F"),
    ("사람들 사이의 조화가 중요하다.", "F", "T"),
    ("피드백을 받을 때 감정보다 내용에 집중한다.", "T", "F"),
    ("계획을 세워두고 그에 따라 움직인다.", "J", "P"),
    ("유연하게 상황을 대처하는 편이다.", "P", "J"),
    ("정해진 일정을 좋아한다.", "J", "P"),
    ("기분에 따라 즉흥적으로 움직이는 편이다.", "P", "J"),
    ("미리 정해진 계획이 없으면 불안하다.", "J", "P"),
]

# 🧩 문항 출력 (3지선다)
for i, (q, yes_type, no_type) in enumerate(questions):
    answer = st.radio(f"{i+1}. {q}", ["그렇다", "보통이다", "아니다"], key=f"q{i}")
    if answer == "그렇다":
        scores[yes_type] += 2
    elif answer == "보통이다":
        scores[yes_type] += 1
    elif answer == "아니다":
        scores[no_type] += 2

# ✅ 결과 보기 버튼
if st.button("결과 보기"):
    mbti = ""
    mbti += "E" if scores["E"] >= scores["I"] else "I"
    mbti += "S" if scores["S"] >= scores["N"] else "N"
    mbti += "T" if scores["T"] >= scores["F"] else "F"
    mbti += "J" if scores["J"] >= scores["P"] else "P"
    st.session_state["mbti"] = mbti
    st.session_state["show_result"] = True

# ✅ 결과 보기 이후 화면 출력
if st.session_state.get("show_result"):
    mbti = st.session_state["mbti"]

    # 상담하러 가기 버튼 중앙 정렬
    button_col1, button_col2, button_col3 = st.columns([1, 2, 1])
    with button_col2:
        if st.button("🗨️ MBTI 친구에게 상담하러 가기"):
            st.switch_page("pages/chatbot.py")


    # 🧸 캐릭터 이미지
    images = {
        "ISTJ": "images/istj.png",
        "ISFJ": "images/isfj.png",
        "INFJ": "images/infj.png",
        "INTJ": "images/intj.png",
        "ISTP": "images/istp.png",
        "ISFP": "images/isfp.png",
        "INFP": "images/infp.png",
        "INTP": "images/intp.png",
        "ESTP": "images/estp.png",
        "ESFP": "images/esfp.png",
        "ENFP": "images/enfp.png",
        "ENTP": "images/entp.png",
        "ESTJ": "images/estj.png",
        "ESFJ": "images/esfj.png",
        "ENFJ": "images/enfj.png",
        "ENTJ": "images/entj.png"
    }

    # 📝 설명
    descriptions = {
        "ISTJ": "🔹 <strong>ISTJ - 현실주의적인 관리자</strong> 🔹<br>신중하고 책임감이 강하며 계획적인 성향입니다.<br>규칙과 원칙을 중시하고 일에 있어 실수를 잘 하지 않습니다.<br>관계에서는 예의와 신뢰를 중요하게 생각하며 감정보다 사실을 우선합니다.<br>조용한 리더십과 실천력으로 조직에서 신뢰받는 타입입니다.",

        "ISFJ": "🔹 <strong>ISFJ - 헌신적인 수호자</strong> 🔹<br>따뜻하고 책임감이 강하며 조용한 성향입니다.<br>타인을 배려하고 돕는 것을 좋아하며 충성심이 높습니다.<br>전통과 안정감을 중시하고 변화보다는 익숙함을 선호합니다.<br>묵묵히 맡은 일을 해내는 성실한 사람입니다.",

        "INFJ": "🔹 <strong>INFJ - 통찰력 있는 조언자</strong> 🔹<br>깊은 내면과 통찰력을 가진 조용한 이상주의자입니다.<br>자신만의 가치관이 뚜렷하며 타인의 감정을 잘 공감합니다.<br>의미 있는 관계와 일을 추구하며 혼자 있는 시간도 중요하게 생각합니다.<br>계획적이고 체계적으로 비전을 실행하는 힘이 있습니다.",

        "INTJ": "🔹 <strong>INTJ - 전략적인 설계자</strong> 🔹<br>독립적이고 분석적이며 미래를 체계적으로 설계하는 성향입니다.<br>감정보다는 논리와 효율을 중시하고 집중력이 매우 뛰어납니다.<br>다소 냉철하게 보일 수 있으나, 내면에는 강한 목표 의식이 있습니다.<br>혼자 일할 때 효율이 높고 리더로서도 강한 면모를 보입니다.",

        "ENFP": "🔹 <strong>ENFP - 열정적인 활동가</strong> 🔹<br>에너지 넘치고 창의적이며 사람들과 어울리는 것을 좋아합니다.<br>즉흥적이지만 진심 어린 관심과 공감 능력이 뛰어난 성격입니다.<br>틀에 얽매이는 걸 싫어하고 자유롭고 다채로운 환경에서 잘 빛납니다.<br>열정적이고 낙천적인 분위기로 주변을 활기차게 만듭니다.",

        "ENTP": "🔹 <strong>ENTP - 창의적인 발명가</strong> 🔹<br>도전 정신이 강하고 아이디어가 풍부한 성격입니다.<br>새로운 것을 시도하는 것을 즐기며 즉흥적인 상황에도 강합니다.<br>말재주가 뛰어나고 사람들과의 토론을 즐깁니다.<br>틀에 얽매이지 않고 자유로운 환경에서 잠재력을 발휘합니다.",

        "ESTP": "🔹 <strong>ESTP - 활기찬 해결사</strong> 🔹<br>즉흥적이고 현실적인 성향으로, 활동적이고 유쾌합니다.<br>문제를 빠르게 인식하고 실전에서 해결하는 데 능합니다.<br>직관적으로 판단하고 눈앞의 상황에 집중합니다.<br>사교적이고 에너지가 넘쳐 그룹에서 중심 역할을 합니다.",

        "ESFP": "🔹 <strong>ESFP - 자유로운 연예인</strong> 🔹<br>사람들과 어울리는 것을 좋아하고 분위기 메이커 역할을 자주 합니다.<br>지금 이 순간을 즐기며 감각적인 경험을 선호합니다.<br>즉흥적으로 움직이고 새로운 자극을 좋아합니다.<br>공감 능력과 친화력이 높아 주변에 활기를 줍니다.",

        "ENFJ": "🔹 <strong>ENFJ - 따뜻한 리더</strong> 🔹<br>타인을 이끄는 능력이 탁월하며 공감과 소통에 강점이 있습니다.<br>사람들에게 동기를 부여하고 조화를 중시합니다.<br>주변 사람들을 세심히 챙기며 조직의 분위기를 부드럽게 만듭니다.<br>가슴 따뜻한 리더 타입으로 존경을 받는 경우가 많습니다.",

        "ENTJ": "🔹 <strong>ENTJ - 당당한 지휘관</strong> 🔹<br>목표 지향적이고 추진력이 강하며 논리적인 사고를 합니다.<br>체계적이고 효율적인 시스템을 구축하는 데 능합니다.<br>리더십이 뛰어나고 어려운 상황에서도 냉정하게 판단합니다.<br>도전과 경쟁을 즐기며 성공을 위해 끊임없이 나아갑니다.",

        "INFP": "🔹 <strong>INFP - 이상적인 중재자</strong> 🔹<br>자신만의 가치와 철학을 지닌 감성적인 성향입니다.<br>다정하고 사려 깊으며 깊은 내면의 감정을 중시합니다.<br>사람들의 진심을 잘 알아채며, 조용하지만 따뜻한 존재입니다.<br>현실보다 이상을 추구하며 자기 성찰을 즐깁니다.",

        "ISFP": "🔹 <strong>ISFP - 온화한 예술가</strong> 🔹<br>부드럽고 감성적이며, 자유로운 분위기를 좋아합니다.<br>자신만의 스타일이 뚜렷하고 조용히 행동으로 표현합니다.<br>갈등을 싫어하고 평화로운 관계를 선호합니다.<br>섬세한 감각으로 예술적 재능을 가진 경우가 많습니다.",

        "ISTP": "🔹 <strong>ISTP - 분석적인 장인</strong> 🔹<br>조용하고 실용적인 성향으로 관찰력이 뛰어납니다.<br>실제 문제 해결에 능하고 분석적 사고를 즐깁니다.<br>자유로운 방식으로 일하기를 선호하고 간섭을 싫어합니다.<br>효율성과 논리를 중시하며 행동은 신속하고 정확합니다.",

        "INTP": "🔹 <strong>INTP - 논리적인 사색가</strong> 🔹<br>지적 호기심이 많고 이론적 사고를 좋아하는 성향입니다.<br>새로운 개념을 탐구하며 창의적인 해결책을 고민합니다.<br>감정보다 진실과 논리에 집중합니다.<br>혼자 깊이 생각할 시간을 중요하게 여깁니다.",

        "ESFJ": "🔹 <strong>ESFJ - 따뜻한 외교관</strong> 🔹<br>사람을 좋아하고 주변을 잘 챙기는 배려심 깊은 성격입니다.<br>친절하고 예의 바르며, 조화로운 관계를 중요하게 여깁니다.<br>책임감이 강하고 조직 내에서 중심 역할을 잘 수행합니다.<br>정서적으로 안정된 분위기를 추구합니다.",

        "ESTJ": "🔹 <strong>ESTJ - 엄격한 관리자</strong> 🔹<br>현실적이고 체계적이며 강한 실행력을 지닌 성격입니다.<br>규칙과 질서를 중시하고 계획에 따라 행동하는 것을 선호합니다.<br>조직을 정비하고 효율을 추구하는 데 탁월합니다.<br>리더로서 명확한 방향과 기준을 제시합니다."
    }


    # 🖼 캐릭터 이미지 중앙 정렬
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image(images.get(mbti), width=250)

    # 💬 말풍선 스타일 결과 카드
    st.markdown(f"""
    <div style="
        background-color: #fff0f5;
        padding: 20px;
        border-radius: 20px;
        border: 2px solid #ffc0cb;
        margin: 20px;
        font-size: 18px;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
        text-align: center;
        ">
        <h3 style="text-align: center;">✨ 당신의 MBTI는 <span style='color:#e75480'>{mbti}</span>입니다!</h3>
        <p>{descriptions.get(mbti)}</p>
    </div>
    """, unsafe_allow_html=True)

