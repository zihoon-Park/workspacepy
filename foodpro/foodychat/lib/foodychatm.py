import streamlit as st
import os

# Streamlit 페이지 구성
st.set_page_config(page_title="FoodyChat", layout="wide")

# 스타일 적용
st.markdown(
    """
    <style>
    .menu-container {
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 40px;
        padding: 20px 0;
        z-index: 1000;
    }
    .menu-link {
        color: #FFFFFF;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.3);
        font-weight: bold;
        font-size: 1.1em;
        text-decoration: none;
        padding: 8px 15px;
        border-radius: 5px;
        transition: all 0.3s ease;
        letter-spacing: 0.5px;
    }
    .menu-link:hover {
        background-color: rgba(255, 255, 255, 0.2);
        transform: translateY(-2px);
    }
    .main-title {
        display: flex;
        align-items: center;
        gap: 8px;
        padding: 10px;
        border-radius: 8px;
        background: rgba(255, 255, 255, 0.1);
    }
    .cute-icon {
        font-size: 1.6em;
        margin-right: 5px;
        display: flex;
        align-items: center;
        gap: 2px;
    }
    .title-text {
        background: linear-gradient(135deg, #FF6B6B 0%, #4ECDC4 100%);
        -webkit-background-clip: text;
        background-clip: text;
        color: transparent;
        font-weight: bold;
        font-size: 1.3em;
        text-shadow: none;
        letter-spacing: 0.5px;
    }
    .home-button {
        background-color: rgba(255, 255, 255, 0.2);
        color: white;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.3);
        padding: 10px 20px;
        border: 2px solid white;
        border-radius: 5px;
        cursor: pointer;
        transition: all 0.3s;
        text-decoration: none;
        font-weight: bold;
    }
    .home-button:hover {
        background-color: white;
        color: #333;
    }
    .menu-title {
        font-weight: bold;
        color: #1E88E5;
        margin-bottom: 5px;
    }
    .menu-subtitle {
        color: #666;
        font-size: 0.9em;
        margin-left: 10px;
    }
    .auth-buttons {
        position: absolute;
        top: 20px;
        left: 20px;
        display: flex;
        flex-direction: column;
        gap: 5px;
        z-index: 1000;
    }
    .auth-button {
        background: transparent;
        color: white;
        padding: 4px 10px;
        border: 1px solid white;
        border-radius: 3px;
        text-decoration: none;
        font-size: 0.6em;
        font-weight: bold;
        transition: all 0.3s ease;
        text-align: center;
        width: 80px;
    }
    .auth-button:hover {
        background-color: rgba(255, 255, 255, 0.1);
        transform: translateY(-1px);
    }
    .auth-buttons-right {
        position: absolute;
        top: 20px;
        right: 20px;
        display: flex;
        flex-direction: column;
        gap: 5px;
        z-index: 1000;
    }
    .home-container {
        background-image: url('https://images.unsplash.com/photo-1504674900247-0877df9cc836?ixlib=rb-1.2.1&auto=format&fit=crop&w=1950&q=80');
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        min-height: 100vh;
        position: relative;
        margin-top: -100px;
        padding-top: 100px;
    }
    .home-overlay {
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: linear-gradient(to bottom, 
            rgba(0, 0, 0, 0.7) 0%,
            rgba(0, 0, 0, 0.5) 20%,
            rgba(0, 0, 0, 0.3) 100%);
        display: flex;
        flex-direction: column;
        justify-content: flex-start;
        align-items: center;
        color: white;
        text-align: center;
        padding: 20px;
    }
    .home-title {
        font-size: 3em;
        margin-bottom: 20px;
        text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.3);
        color: white;
    }
    .home-subtitle {
        font-size: 1.5em;
        margin-bottom: 30px;
        text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.3);
        color: white;
    }
    .home-buttons {
        display: flex;
        gap: 20px;
    }
    .upload-container {
        max-width: 400px;
        margin: 120px auto 0;
        padding: 20px;
        background-color: white;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .form-group {
        margin-bottom: 15px;
    }
    .form-group label {
        display: block;
        margin-bottom: 5px;
        color: #333;
    }
    .form-group input {
        width: 100%;
        padding: 8px;
        border: 1px solid #ddd;
        border-radius: 4px;
    }
    .submit-btn {
        background-color: #1E88E5;
        color: white;
        padding: 10px 20px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        width: 100%;
    }
    .submit-btn:hover {
        background-color: #1976D2;
    }
    .upload-area {
        border: 2px dashed #1E88E5;
        border-radius: 10px;
        padding: 20px;
        text-align: center;
        cursor: pointer;
        transition: background-color 0.3s;
    }
    .upload-area:hover {
        background-color: rgba(30, 136, 229, 0.1);
    }
    .preview-image {
        max-width: 100%;
        max-height: 300px;
        margin-top: 20px;
        border-radius: 5px;
    }
    </style>
    <div class="menu-container">
        <a href="/?page=mypage" class="menu-link">마이페이지</a>
        <a href="/?page=chatbot" class="menu-link">AI 챗봇</a>
        <a href="/?page=image_upload" class="menu-link">이미지 업로드</a>
    </div>
    """,
    unsafe_allow_html=True
)

# 사이드바 제목
st.sidebar.markdown(
    """
    <div class="main-title">
        <span class="cute-icon">🍱</span>
        <span class="title-text">FoodyChat</span>
    </div>
    """,
    unsafe_allow_html=True
)

# 사이드바 메뉴
st.sidebar.markdown("""
    <div class="menu-group">
        <div class="menu-title">마이페이지</div>
        <div class="menu-subtitle">회원 정보 관리</div>
    </div>
    <div class="menu-group">
        <div class="menu-title">AI 챗봇</div>
        <div class="menu-subtitle">음식 관련 대화</div>
    </div>
    <div class="menu-group">
        <div class="menu-title">이미지 업로드</div>
        <div class="menu-subtitle">음식 이미지 분석</div>
    </div>
""", unsafe_allow_html=True)

# 선택한 메뉴를 세션 상태에 저장
def navigate_to(page):
    st.session_state["page"] = page

# 현재 페이지 확인 및 기본값 설정
page = st.session_state.get("page", "home")

# 각 페이지 구성
def home_page():
    st.markdown("""
        <div class="home-container">
            <div class="auth-buttons">
                <a href="/?page=login" class="auth-button">로그인</a>
            </div>
            <div class="auth-buttons-right">
                <a href="/?page=signup" class="auth-button">회원가입</a>
            </div>
            <div class="home-overlay">
                <h1 class="home-title">FoodyChat</h1>
                <p class="home-subtitle">AI와 함께하는 맛있는 대화</p>
                <div class="home-buttons">
                    <a href="/?page=chatbot" class="home-button">챗봇 시작하기</a>
                    <a href="/?page=image_upload" class="home-button">이미지 업로드</a>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

def login_page():
    st.markdown('<div class="upload-container">', unsafe_allow_html=True)
    st.markdown('<h2 style="text-align: center; margin-bottom: 20px;">로그인</h2>', unsafe_allow_html=True)
    
    with st.form("login_form"):
        st.markdown('<div class="form-group">', unsafe_allow_html=True)
        username = st.text_input("아이디")
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="form-group">', unsafe_allow_html=True)
        password = st.text_input("비밀번호", type="password")
        st.markdown('</div>', unsafe_allow_html=True)
        
        submit = st.form_submit_button("로그인", key="login_submit")
        if submit:
            # 로그인 처리 로직 추가
            pass
    
    st.markdown('</div>', unsafe_allow_html=True)

def signup_page():
    st.markdown('<div class="upload-container">', unsafe_allow_html=True)
    st.markdown('<h2 style="text-align: center; margin-bottom: 20px;">회원가입</h2>', unsafe_allow_html=True)
    
    with st.form("signup_form"):
        st.markdown('<div class="form-group">', unsafe_allow_html=True)
        username = st.text_input("아이디")
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="form-group">', unsafe_allow_html=True)
        password = st.text_input("비밀번호", type="password")
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="form-group">', unsafe_allow_html=True)
        password_confirm = st.text_input("비밀번호 확인", type="password")
        st.markdown('</div>', unsafe_allow_html=True)
        
        submit = st.form_submit_button("회원가입", key="signup_submit")
        if submit:
            # 회원가입 처리 로직 추가
            pass
    
    st.markdown('</div>', unsafe_allow_html=True)

def mypage():
    st.header("마이페이지")
    st.write("회원 정보를 확인하고 수정할 수 있는 페이지입니다.")

def chatbot_page():
    st.header("AI 챗봇")
    st.write("여기는 AI 챗봇 페이지입니다.")
    st.text_area("메시지 입력")
    st.button("전송")

def image_upload_page():
    st.markdown('<div class="upload-container">', unsafe_allow_html=True)
    st.markdown('<h2 style="text-align: center; margin-bottom: 20px;">이미지 업로드</h2>', unsafe_allow_html=True)
    
    # 파일 업로더
    uploaded_file = st.file_uploader("이미지를 선택하세요", type=['png', 'jpg', 'jpeg'])
    
    if uploaded_file is not None:
        # 이미지 미리보기
        st.image(uploaded_file, caption='업로드된 이미지', use_column_width=True)
        
        # 이미지 분석 버튼
        if st.button("이미지 분석하기"):
            # 이미지 분석 로직 추가
            st.success("이미지가 성공적으로 업로드되었습니다!")
    
    st.markdown('</div>', unsafe_allow_html=True)

# 페이지 렌더링
if page == "home":
    home_page()
elif page == "login":
    login_page()
elif page == "signup":
    signup_page()
elif page == "mypage":
    mypage()
elif page == "chatbot":
    chatbot_page()
elif page == "image_upload":
    image_upload_page()
