import streamlit as st
import os
import base64
from PIL import Image
import io

# 페이지 설정
st.set_page_config(
    page_title="FoodyChat",
    page_icon="🍱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS 스타일
st.markdown("""
<style>
    /* 전체 스타일 */
    .stApp {
        background-color: #f5f5f5;
    }
    
    /* 홈 컨테이너 */
    .home-container {
        position: relative;
        width: 100%;
        height: 100vh;
        background-image: url('https://images.unsplash.com/photo-1504674900247-0877df9cc836?ixlib=rb-1.2.1&auto=format&fit=crop&w=1950&q=80');
        background-size: cover;
        background-position: center;
        overflow: hidden;
        margin-top: -10mm;
    }
    
    /* 홈 오버레이 */
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
        margin-top: -15mm;
    }
    
    /* 한옥문 문고리 스타일의 원형 버튼 */
    .hanok-door-container {
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        width: 30mm;
        height: 30mm;
        border-radius: 50%;
        overflow: hidden;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3),
                    inset 0 0 10px rgba(255, 255, 255, 0.5),
                    0 0 15px rgba(255, 255, 255, 0.3);
        z-index: 1000;
        background-image: url('https://images.unsplash.com/photo-1584559582128-97f5f1722ecc?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=80');
        background-size: cover;
        background-position: center;
        filter: brightness(1.3) saturate(1.2);
        border: 3px solid rgba(255, 255, 255, 0.8);
        cursor: pointer;
        display: block !important;
    }
    
    .hanok-door-half {
        position: absolute;
        width: 50%;
        height: 100%;
        display: flex;
        justify-content: center;
        align-items: center;
        text-decoration: none;
        font-weight: bold;
        font-size: 1em;
        color: #4CAF50;
        transition: all 0.3s ease;
        background-color: rgba(0, 0, 0, 0.4);
    }
    
    .hanok-door-half:hover {
        background-color: rgba(0, 0, 0, 0.6);
    }
    
    .hanok-door-login {
        left: 0;
        border-radius: 15mm 0 0 15mm;
        border-right: 1px solid rgba(255, 255, 255, 0.5);
    }
    
    .hanok-door-signup {
        right: 0;
        border-radius: 0 15mm 15mm 0;
        border-left: 1px solid rgba(255, 255, 255, 0.5);
    }
    
    .hanok-door-text {
        text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.5);
        z-index: 2;
        writing-mode: vertical-lr;
        text-orientation: upright;
        letter-spacing: 3px;
        padding: 5px 0;
        text-decoration: none;
        color: #4CAF50;
        font-size: 1.2em;
    }
    
    /* 기존 plate-container 스타일은 유지하되 숨김 처리 */
    .plate-container {
        display: none !important;
    }
    
    /* 홈 타이틀 */
    .home-title {
        font-size: 3em;
        margin-bottom: 10px;
        background: linear-gradient(135deg, #FF6B6B 0%, #4ECDC4 100%);
        -webkit-background-clip: text;
        background-clip: text;
        color: transparent;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
        margin-top: 15mm !important;
    }
    
    /* 홈 서브타이틀 */
    .home-subtitle {
        font-size: 1.5em;
        margin-bottom: 30px;
        color: white;
        margin-top: 0mm !important;
    }
    
    /* 홈 버튼 */
    .home-buttons {
        display: flex;
        gap: 20px;
        margin-top: 15px !important;
    }
    
    .home-button {
        padding: 12px 25px;
        background-color: rgba(255, 255, 255, 0.2);
        color: white;
        border-radius: 5px;
        text-decoration: none;
        transition: all 0.3s ease;
        font-size: 1.1em;
        border: 1px solid rgba(255, 255, 255, 0.3);
    }
    
    .home-button:hover {
        background-color: rgba(255, 255, 255, 0.3);
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
    }
    
    /* 라디오 버튼 완전히 숨김 처리 */
    div[data-testid="stRadio"] {
        display: none !important;
        visibility: hidden !important;
        opacity: 0 !important;
        height: 0 !important;
        width: 0 !important;
        position: absolute !important;
        pointer-events: none !important;
    }
    
    /* 인증 버튼 스타일 제거 */
    .auth-buttons, .auth-buttons-right, .auth-button {
        display: none !important;
    }
    
    /* 사이드바 스타일 */
    .sidebar-content {
        padding: 30px;
        color: white;
        background-image: url('https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80');
        background-size: cover;
        background-position: center;
        min-height: 100vh;
        position: relative;
    }
    
    .sidebar-content::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: rgba(0, 0, 0, 0.7);
        z-index: 1;
    }
    
    .sidebar-title {
        font-size: 2em;
        font-weight: bold;
        margin-bottom: 15px;
        color: #FFD700;
        text-align: center;
        padding-bottom: 15px;
        border-bottom: 2px solid #FFD700;
        position: relative;
        z-index: 2;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
    }
    
    .sidebar-subtitle {
        font-size: 1em;
        color: rgba(255, 255, 255, 0.9);
        text-align: center;
        margin-bottom: 30px;
        position: relative;
        z-index: 2;
        font-style: italic;
    }
    
    .sidebar-menu {
        margin-top: 30px;
        position: relative;
        z-index: 2;
    }
    
    .sidebar-menu-item {
        display: block;
        padding: 15px 0;
        color: #FFFFFF;
        text-decoration: none;
        font-size: 1.2em;
        font-weight: 700;
        transition: all 0.3s ease;
        border-bottom: 1px solid rgba(255, 255, 255, 0.2);
        text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.8);
    }
    
    .sidebar-menu-item:hover {
        color: #FFD700;
        transform: translateX(5px);
        background-color: rgba(0, 0, 0, 0.5);
        padding-left: 15px;
    }
    
    .sidebar-menu-icon {
        margin-right: 15px;
        font-size: 1.3em;
    }
    
    /* 사이드바 이미지 아래 부분 제거 */
    .sidebar-content::after {
        display: none;
    }
</style>
""", unsafe_allow_html=True)

# 페이지 함수
def home_page():
    st.markdown("""
    <div class="home-container">
        <div class="hanok-door-container">
            <a href="javascript:void(0)" onclick="window.parent.document.querySelector('button[data-testid=\'stSidebar\']').click(); window.parent.document.querySelector('div[data-testid=\'stRadio\'] label:nth-child(2)').click();" class="hanok-door-half hanok-door-login">
                <span class="hanok-door-text">로그인</span>
            </a>
            <a href="javascript:void(0)" onclick="window.parent.document.querySelector('button[data-testid=\'stSidebar\']').click(); window.parent.document.querySelector('div[data-testid=\'stRadio\'] label:nth-child(3)').click();" class="hanok-door-half hanok-door-signup">
                <span class="hanok-door-text">회원가입</span>
            </a>
        </div>
        <div class="home-overlay">
            <h1 class="home-title">FoodyChat</h1>
            <p class="home-subtitle">AI와 함께하는 맛있는 대화</p>
            <div class="home-buttons">
                <a href="javascript:void(0)" onclick="window.parent.document.querySelector('button[data-testid=\'stSidebar\']').click(); window.parent.document.querySelector('div[data-testid=\'stRadio\'] label:nth-child(5)').click();" class="home-button">챗봇 시작하기</a>
                <a href="javascript:void(0)" onclick="window.parent.document.querySelector('button[data-testid=\'stSidebar\']').click(); window.parent.document.querySelector('div[data-testid=\'stRadio\'] label:nth-child(6)').click();" class="home-button">이미지 업로드</a>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

def login_page():
    st.title("로그인")
    st.write("로그인 페이지입니다.")

def signup_page():
    st.title("회원가입")
    st.write("회원가입 페이지입니다.")

def mypage():
    st.title("마이페이지")
    st.write("마이페이지입니다.")

def chatbot():
    st.title("챗봇")
    st.write("챗봇 페이지입니다.")

def image_upload():
    st.title("이미지 업로드")
    st.write("이미지 업로드 페이지입니다.")

# 메인 앱
def main():
    # 사이드바
    with st.sidebar:
        st.markdown("""
        <div class="sidebar-content">
            <h2 class="sidebar-title">푸디챗 Menu</h2>
            <p class="sidebar-subtitle">AI와 함께하는 맛있는 대화</p>
            <div class="sidebar-menu">
                <a href="javascript:void(0)" onclick="window.parent.document.querySelector('button[data-testid=\'stSidebar\']').click(); window.parent.document.querySelector('div[data-testid=\'stRadio\'] label:nth-child(1)').click();" class="sidebar-menu-item"><span class="sidebar-menu-icon">🏠</span>홈</a>
                <a href="javascript:void(0)" onclick="window.parent.document.querySelector('button[data-testid=\'stSidebar\']').click(); window.parent.document.querySelector('div[data-testid=\'stRadio\'] label:nth-child(2)').click();" class="sidebar-menu-item"><span class="sidebar-menu-icon">🔑</span>로그인</a>
                <a href="javascript:void(0)" onclick="window.parent.document.querySelector('button[data-testid=\'stSidebar\']').click(); window.parent.document.querySelector('div[data-testid=\'stRadio\'] label:nth-child(3)').click();" class="sidebar-menu-item"><span class="sidebar-menu-icon">📝</span>회원가입</a>
                <a href="javascript:void(0)" onclick="window.parent.document.querySelector('button[data-testid=\'stSidebar\']').click(); window.parent.document.querySelector('div[data-testid=\'stRadio\'] label:nth-child(4)').click();" class="sidebar-menu-item"><span class="sidebar-menu-icon">👤</span>마이페이지</a>
                <a href="javascript:void(0)" onclick="window.parent.document.querySelector('button[data-testid=\'stSidebar\']').click(); window.parent.document.querySelector('div[data-testid=\'stRadio\'] label:nth-child(5)').click();" class="sidebar-menu-item"><span class="sidebar-menu-icon">💬</span>챗봇</a>
                <a href="javascript:void(0)" onclick="window.parent.document.querySelector('button[data-testid=\'stSidebar\']').click(); window.parent.document.querySelector('div[data-testid=\'stRadio\'] label:nth-child(6)').click();" class="sidebar-menu-item"><span class="sidebar-menu-icon">📸</span>이미지 업로드</a>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # 페이지 선택 (숨김 처리)
        page = st.radio("페이지 선택", ["홈", "로그인", "회원가입", "마이페이지", "챗봇", "이미지 업로드"], label_visibility="collapsed")
    
    # 페이지 라우팅
    if page == "홈":
        home_page()
    elif page == "로그인":
        login_page()
    elif page == "회원가입":
        signup_page()
    elif page == "마이페이지":
        mypage()
    elif page == "챗봇":
        chatbot()
    elif page == "이미지 업로드":
        image_upload()

if __name__ == "__main__":
    main()
