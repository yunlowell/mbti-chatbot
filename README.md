# MBTI 테스트 및 상담 챗봇

이 프로젝트는 사용자가 **MBTI 테스트**를 완료한 후, 그 결과에 맞는 **챗봇 상담**을 제공합니다.  
사용자는 결과를 확인한 뒤, "상담하러 가기" 버튼을 클릭하여 자신의 MBTI 유형에 맞는 캐릭터와 대화할 수 있습니다.

## 🚀 기능

- **MBTI 테스트**: 사용자가 여러 문항에 응답하여 자신의 MBTI 유형을 확인합니다.
- **결과 확인**: 결과 화면에서 자신이 어떤 MBTI 유형인지를 보여줍니다.
- **챗봇 상담**: 자신의 MBTI 유형에 맞는 캐릭터와 대화하며, 그 유형에 맞는 조언과 정보를 제공합니다.
- **유형별 이미지 및 설명**: 각 MBTI 유형에 맞는 캐릭터 이미지와 설명이 제공됩니다.

## 📦 요구 사항

- Python 3.x
- Streamlit
- OpenAI API (챗봇 기능 사용을 위한 API 키 필요)

## 🛠 설치 및 실행

### 1. 의존성 설치

```bash
pip install -r requirements.txt
```

`requirements.txt` 파일을 통해 필요한 라이브러리들을 한 번에 설치할 수 있습니다. 주요 라이브러리는 다음과 같습니다:

- `streamlit`
- `openai`
- `pandas`

### 2. Streamlit 실행

앱을 실행하려면 다음 명령어를 사용합니다:

```bash
streamlit run app.py
```

### 3. OpenAI API 키 설정

OpenAI API를 사용하려면, `st.secrets`를 통해 API 키를 입력해야 합니다.  
API 키는 `secrets.toml` 파일에 저장합니다.

#### `secrets.toml` 예시:

```toml
API_KEY = "your-openai-api-key"
```

`secrets.toml` 파일은 앱 디렉토리 내 `.streamlit` 폴더에 위치해야 합니다.

## 📋 파일 구조

```
project/
├── app.py                # MBTI 테스트와 결과 화면
├── pages/
│   └── chatbot.py        # 챗봇 상담 페이지
├── images/               # 각 MBTI 유형별 캐릭터 이미지
│   └── istj.png          # 예시 이미지 파일
│   └── isfj.png          # 예시 이미지 파일
│   └── ...
├── .streamlit/
│   └── secrets.toml      # OpenAI API 키
├── requirements.txt      # 의존성 리스트
└── README.md             # 프로젝트 설명서
```

## 🧩 사용 방법

1. **MBTI 테스트 진행**
   - 사용자는 여러 문항에 대해 "그렇다", "아니다"로 응답합니다.
   - 각 응답은 `scores` 딕셔너리에 저장되고, 테스트 완료 후 MBTI 유형이 계산됩니다.

2. **결과 확인**
   - 테스트 결과 화면에서 자신이 어떤 MBTI 유형인지 확인할 수 있습니다.
   - 각 유형에 맞는 **이미지**와 **설명**이 표시됩니다.

3. **상담하기**
   - "상담하러 가기" 버튼을 클릭하면, 사용자는 자신과 같은 MBTI 유형의 **챗봇과 대화**를 시작할 수 있습니다.
   - 챗봇은 사용자의 유형에 맞는 **말투**와 **조언**을 제공합니다.

## 🔧 코드 설명

### 1. **MBTI 테스트**

`app.py`에서 사용자가 입력한 답변을 기반으로 **MBTI 유형**을 계산합니다.

```python
mbti = ""
mbti += "E" if scores["E"] >= scores["I"] else "I"
mbti += "S" if scores["S"] >= scores["N"] else "N"
mbti += "T" if scores["T"] >= scores["F"] else "F"
mbti += "J" if scores["J"] >= scores["P"] else "P"
st.session_state["mbti"] = mbti
```

### 2. **챗봇 대화**

사용자가 MBTI 결과를 확인한 후, 그에 맞는 **챗봇**과 대화할 수 있습니다.  
이 부분은 OpenAI의 GPT 모델을 사용하여 MBTI 유형에 맞는 대화를 제공합니다.

```python
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",  # 또는 gpt-4
    messages=st.session_state.chat_history,
    temperature=0.7
)
```

### 3. **페이지 전환**

Streamlit의 **`st.switch_page()`** 함수를 사용하여 결과 화면에서 챗봇 페이지로 이동할 수 있습니다:

```python
if st.button("🗨️ MBTI 캐릭터와 상담하러 가기"):
    st.switch_page("pages/chatbot.py")
```

## 🔒 보안

- **API 키**는 `secrets.toml` 파일을 통해 안전하게 관리됩니다.
- 사용자와의 대화 히스토리는 **세션 상태**를 사용하여 관리됩니다. (`st.session_state`)

## 🌐 링크

- **[OpenAI API 문서](https://beta.openai.com/docs/)**
- **[Streamlit 공식 사이트](https://streamlit.io/docs)**
