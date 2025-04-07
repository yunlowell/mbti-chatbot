import streamlit as st
import openai

client = openai.OpenAI(api_key=st.secrets["API_KEY"])

st.title("💬 MBTI 친구 챗봇")

# 1. 세션에서 MBTI 가져오기
mbti = st.session_state.get("mbti", None)

if not mbti:
    st.warning("먼저 MBTI 테스트를 완료해 주세요.")
    st.stop()

# 2. 말투 정의
mbti_personalities = {
    "ISTJ": "신중하고 딱딱한 말투. 감정보다는 사실 중심으로 말함.",
    "ISFJ": "조용하고 따뜻한 말투. 배려와 공감을 담아 말함.",
    "INFJ": "차분하고 사려 깊은 말투. 내면을 꿰뚫는 듯한 느낌.",
    "INTJ": "논리적이고 단호한 말투. 효율과 분석 중심.",
    
    "ISTP": "간결하고 직설적인 말투. 쓸데없는 말은 하지 않음.",
    "ISFP": "말수가 적고 조용한 말투. 부드럽고 감성적.",
    "INFP": "따뜻하고 감성적인 말투. 이상과 감정을 중요시함.",
    "INTP": "논리적이고 탐구적인 말투. 호기심 많고 분석적.",
    
    "ESTP": "직설적이고 유쾌한 말투. 반응이 빠르고 행동 중심.",
    "ESFP": "명랑하고 감정 표현이 풍부한 말투. 말에 활기가 있음.",
    "ENFP": "말이 많고 에너지 넘치는 말투. 호기심 많고 상냥함.",
    "ENTP": "재치 있고 도전적인 말투. 농담과 비유를 잘 씀.",
    
    "ESTJ": "단정하고 논리적인 말투. 명확하고 정리된 느낌.",
    "ESFJ": "다정하고 따뜻한 말투. 상대방을 잘 배려함.",
    "ENFJ": "설득력 있고 친절한 말투. 공감 능력이 뛰어남.",
    "ENTJ": "자신감 있고 리더십 있는 말투. 단호하고 체계적."
}

bot_style = mbti_personalities.get(mbti, "친절하고 중립적인 말투")

# 3. 대화 세션
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        {"role": "system", "content": f"당신은 {mbti} 유형의 챗봇입니다. 말투는 다음과 같습니다: {bot_style}"},
        {"role": "assistant", "content": f"안녕! 나는 너와 같은 {mbti}야. 뭐든 편하게 말 걸어줘! 너의 입장에서 이야기를 들어줄게."}
    ]

# 4. 대화 UI
for msg in st.session_state.chat_history:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

user_input = st.chat_input("무엇이든 말해보세요!")
if user_input:
    st.chat_message("user").markdown(user_input)
    st.session_state.chat_history.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=st.session_state.chat_history,
        temperature=0.7
    )
    bot_reply = response.choices[0].message.content
    st.chat_message("assistant").markdown(bot_reply)
    st.session_state.chat_history.append({"role": "assistant", "content": bot_reply})
