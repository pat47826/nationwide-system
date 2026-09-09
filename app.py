import streamlit as st

st.set_page_config(page_title="Nationwide System", layout="wide")

# 1. กำหนดให้ "หน้าแรก" เป็น Default ทันทีเมื่อเปิดเว็บเข้ามา
if "current_page" not in st.session_state:
    st.session_state.current_page = "home"

# CSS เมนูมินิมอลตรงกลางจอ
st.markdown("""
    <style>
        [data-testid="stSidebar"] { display: none !important; }

        div[data-testid="stMainBlockContainer"] {
            padding-top: 1rem !important;
        }

        .top-nav-btn button,
        .top-nav-btn button[data-testid="baseButton-secondary"],
        div[data-testid="stColumn"] button {
            background-color: transparent !important;
            background: transparent !important;
            border: none !important;
            box-shadow: none !important;
            outline: none !important;
            color: #31333F !important;
            font-size: 16px !important;
            font-weight: 500 !important;
            padding: 4px 8px !important;
        }

        .top-nav-btn button:hover,
        div[data-testid="stColumn"] button:hover {
            color: #FF4B4B !important;
            background-color: transparent !important;
        }

        .top-nav-btn button:focus,
        div[data-testid="stColumn"] button:focus {
            color: #FF4B4B !important;
            box-shadow: none !important;
        }
    </style>
""", unsafe_allow_html=True)

# 2. แถบ Navigation ด้านบน
_, c1, c2, c3, c4, c5, _ = st.columns([2, 1.2, 1.5, 1.3, 1.2, 1.6, 2])

with c1:
    st.markdown('<div class="top-nav-btn">', unsafe_allow_html=True)
    if st.button("🏠 หน้าแรก", use_container_width=True):
        st.session_state.current_page = "home"
    st.markdown('</div>', unsafe_allow_html=True)

with c2:
    st.markdown('<div class="top-nav-btn">', unsafe_allow_html=True)
    if st.button("🖼️ อัปโหลดรูปภาพ", use_container_width=True):
        st.session_state.current_page = "image"
    st.markdown('</div>', unsafe_allow_html=True)

with c3:
    st.markdown('<div class="top-nav-btn">', unsafe_allow_html=True)
    if st.button("🛠️ การซ่อมบำรุง", use_container_width=True):
        st.session_state.current_page = "maint"
    st.markdown('</div>', unsafe_allow_html=True)

with c4:
    st.markdown('<div class="top-nav-btn">', unsafe_allow_html=True)
    if st.button("📦 คลังสินค้า", use_container_width=True):
        st.session_state.current_page = "stock"
    st.markdown('</div>', unsafe_allow_html=True)

with c5:
    st.markdown('<div class="top-nav-btn">', unsafe_allow_html=True)
    if st.button("📜 ประวัติการซ่อมแซม", use_container_width=True):
        st.session_state.current_page = "history"
    st.markdown('</div>', unsafe_allow_html=True)

# --------------------------------------------------
# 3. โหลดเนื้อหาตามหน้าที่เลือก (ดึงจากไฟล์ในโฟลเดอร์ pages/)
# --------------------------------------------------
if st.session_state.current_page == "home":
    # โหลดโค้ดจากไฟล์ pages/1_Home.py มาแสดง
    exec(open("pages/1_Home.py", encoding="utf-8").read())

elif st.session_state.current_page == "image":
    exec(open("pages/2_Image.py", encoding="utf-8").read())

elif st.session_state.current_page == "maint":
    exec(open("pages/3_Maintenance.py", encoding="utf-8").read())

elif st.session_state.current_page == "stock":
    exec(open("pages/4_Inventory.py", encoding="utf-8").read())

elif st.session_state.current_page == "history":
    exec(open("pages/5_History.py", encoding="utf-8").read())