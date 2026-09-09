import streamlit as st

# CSS แต่งปุ่ม
st.markdown("""
    <style>
        div.stButton > button[kind="primary"] {
            background-color: #2563eb !important;
            color: white !important;
            border: 2px solid #1d4ed8 !important;
            border-radius: 8px !important;
            font-size: 15px !important;
            font-weight: bold !important;
            padding: 0.5rem 1.8rem !important;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1) !important;
        }
        div.stButton > button[kind="primary"]:hover {
            background-color: #1d4ed8 !important;
            border-color: #1e40af !important;
        }
    </style>
""", unsafe_allow_html=True)

left_space, content_container, right_space = st.columns([1, 4, 1])

with content_container:
    st.subheader("🖼️ อัปโหลดรูปภาพรายงานการปฏิบัติงาน")

# รายชื่อจังหวัดทั้งหมดสำหรับทำ Dropdown
all_provinces = [
    "กรุงเทพมหานคร", "เชียงใหม่", "เชียงราย", "ขอนแก่น", 
    "อุดรธานี", "นครราชสีมา", "สงขลา", "ภูเก็ต", "สุราษฎร์ธานี",
    "ชลบุรี", "ระยอง", "นนทบุรี", "ปทุมธานี", "สมุทรปราการ"
]

# ข้อมูลจำลองรายชื่อจอแยกตามภาค
screen_data = {
    "กรุงเทพฯ และปริมณฑล": ["จอแยกอโศก", "จอสยามพารากอน", "จอสีลมคอมเพล็กซ์"],
    "ภาคเหนือ": ["จอประตูท่าแพ", "จอนิมมานเหมินท์", "จอเซ็นทรัลเชียงราย"],
    "ภาคอีสาน": ["จอหน้าเซ็นทรัลขอนแก่น", "จอเมืองอุดรธานี", "จอโคราชไนท์บาซาร์"],
    "ภาคใต้": ["จอหาดใหญ่ซิตี้", "จอภูเก็ตป่าตอง", "จอเมืองสุราษฎร์"]
}

regions = list(screen_data.keys())

@st.dialog("🎉 แจ้งเตือน")
def success_dialog():
    st.success("Success! อัปโหลดรูปภาพสำเร็จ")
    st.balloons()
    if st.button("ตกลง", use_container_width=True, key="btn_dialog_ok"):
        st.rerun()

with content_container:
    # 1. Dropdown เลือกภูมิภาค (ขึ้น Select... เป็นค่าเริ่มต้น)
    st.markdown("### 1. เลือกชื่อจอ")
    selected_region = st.selectbox(
        "เลือกภูมิภาค", 
        regions, 
        index=None, 
        placeholder="Select...", 
        key="reg"
    )
    
    if selected_region:
        available_screens = screen_data[selected_region]
        selected_screen = st.selectbox(
            "เลือกชื่อจอภาพ", 
            available_screens, 
            index=None, 
            placeholder="Select...", 
            key="scr"
        )
    else:
        selected_screen = st.selectbox(
            "เลือกชื่อจอภาพ", 
            ["กรุณาเลือกภูมิภาคก่อน"], 
            index=0, 
            disabled=True, 
            key="scr_disabled"
        )
    
    # 2. Location (Dropdown จังหวัด ขึ้น Select... เป็นค่าเริ่มต้น)
    st.markdown("### 2. Location (จังหวัด)")
    selected_province = st.selectbox(
        "เลือกจังหวัดสถานที่ตั้ง", 
        all_provinces, 
        index=None, 
        placeholder="Select...", 
        key="prov"
    )
    
    # 3. ช่องอัปโหลดรูปภาพ
    st.markdown("### 3. อัปโหลดรูปภาพ")
    uploaded_files = st.file_uploader(
        "อัปโหลดรูปภาพ (เลือกได้สูงสุด 5 รูป / รองรับไฟล์ภาพกล้องความละเอียดสูง)", 
        type=["png", "jpg", "jpeg", "RAW", "cr2", "nef"], 
        accept_multiple_files=True,
        key="up_files",
        help="รองรับไฟล์ภาพขนาดใหญ่จากกล้องโปร"
    )
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # 4. ปุ่มกดส่งข้อมูล
    col1, col_btn, col3 = st.columns([1.7, 2, 1.3])
    with col_btn:
        submitted = st.button("🚀 ส่งข้อมูล / อัปโหลด", type="primary", key="submit_btn")
    
    if submitted:
        if not selected_region or not selected_province or not uploaded_files:
            st.warning("⚠️ กรุณากรอกข้อมูลและอัปโหลดรูปภาพให้ครบถ้วนก่อนกดส่งครับ")
        else:
            st.session_state.show_success_popup = True

if st.session_state.get("show_success_popup", False):
    st.session_state.show_success_popup = False
    success_dialog()
