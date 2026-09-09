import streamlit as st

# แบ่งเป็น 2 คอลัมน์ (ฝั่งซ้ายใหญ่กว่าสำหรับรูป/แบนเนอร์, ฝั่งขวาเป็นกล่องข่าวสาร)
col_left, col_right = st.columns([2.2, 1], gap="large")

with col_left:
    st.subheader("🏢 Nationwide System")
    
    # แสดงรูปตึก Plan B Media (เปลี่ยน path เป็นรูปของคุณ เช่น 'planb_building.jpg' หรือ URL)
    # หากยังไม่มีไฟล์รูป ระบบจะใช้ รูปตัวอย่าง (Placeholder) ไปก่อนได้ครับ
    image_path = "https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?q=80&w=1200" # รูปตึกตัวอย่าง
    
    st.image(
        image_path, 
        caption="Plan B Media Headquarters", 
        use_container_width=True
    )
    
    st.markdown("""
    ### ยินดีต้อนรับสู่ระบบบริหารจัดการ Nationwide
    ระบบกลางสำหรับจัดการรูปภาพ การซ่อมบำรุง คลังสินค้า และติดตามประวัติการซ่อมแซม 
    เลือกเมนูการใช้งานได้จากแถบเมนูด้านบน
    """)

with col_right:
    st.subheader("📢 ข่าวสาร & ประกาศ")
    
    # กล่องข่าวสารข่าวที่ 1
    with st.container(border=True):
        st.markdown("**📌 อัปเดตรบบประจำเดือน**")
        st.caption("🗓️ 9 กันยายน 2026")
        st.write("ระบบเปิดใช้งานแถบเมนูด้านบนรูปแบบใหม่ เพิ่มความสะดวกในการสลับหน้าทำงาน")
        st.markdown("[🔗 อ่านรายละเอียดเพิ่มเติม](https://www.planbmedia.co.th)")

    # กล่องข่าวสารข่าวที่ 2
    with st.container(border=True):
        st.markdown("**🛠️ แจ้งปิดปรับปรุงระบบคลังสินค้าชั่วคราว**")
        st.caption("🗓️ 5 กันยายน 2026")
        st.write("จะมีการปิดปรับปรุงฐานข้อมูลคลังสินค้าในวันเสาร์นี้ เวลา 22:00 - 00:00 น.")

    # กล่องข่าวสารข่าวที่ 3
    with st.container(border=True):
        st.markdown("**📸 แนวทางการอัปโหลดรูปภาพงานซ่อม**")
        st.caption("🗓️ 1 กันยายน 2026")
        st.write("รบกวนเจ้าหน้าที่ควรอัปโหลดรูปภาพความละเอียดไม่เกิน 5MB ต่อไฟล์เพื่อความรวดเร็ว")