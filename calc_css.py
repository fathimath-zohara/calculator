import streamlit as st
st.set_page_config(
    page_title = "Calculator",
    page_icon = "🔢",
    layout = "centered"
)

st.markdown("""
<style>
.stApp{backgorund:linear-gradient(135deg,#420909,#423f09,#1a1801);}
.main-title{text-align:center;font-size:48px;font-weight:bold;
    color:white;background:linear-gradient(90deg,#0f4214,#e9f5bf);
    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;
    margin-bottom:10px;}
.subtitle{text-align:center;color:#96949c;font-size:18px;margin-bottom:30px;}
.stButton>button{width:100%,height:55px;background:linear-gradient(90deg,#abad58,#3c3d1b);
    color:black;border:none;border-radius:12px;font-size:20px;font-weight:bold;}
.stButton>button:hover{background:linear-gradient(90deg,#cf9ef7,#f0edf2);
    transform:scale(1.02);}
.result{padding:20px;border-radius:15px;background:#94f29d;color:#191c19;
    text-align:center;font-size:28px,font-weight:bold;border:2px solid #15591c;}

</style
""",unsafe_allow_html=True)

# ---------- Header ----------
st.markdown("<h1 class='main-title'>🧮 Trendy Calculator</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Simple • Fast • Beautiful</p>", unsafe_allow_html=True)

# ---------- Inputs ----------
col1, col2 = st.columns(2)

with col1:
    num1 = st.number_input("🔢 First Number", value=0.0)

with col2:
    num2 = st.number_input("🔢 Second Number", value=0.0)

operation = st.selectbox(
    "✨ Select Operation",
    ["➕ Add", "➖ Subtract", "✖ Multiply", "➗ Divide"]
)

# ---------- Calculate ----------
if st.button("🚀 Calculate"):

    if operation == "➕ Add":
        ans = num1 + num2

    elif operation == "➖ Subtract":
        ans = num1 - num2

    elif operation == "✖ Multiply":
        ans = num1 * num2

    elif operation == "➗ Divide":
        if num2 == 0:
            st.error("❌ Cannot divide by zero.")
            st.stop()
        ans = num1 / num2

    st.markdown(
        f"<div class='result'>🎯 Result: {ans}</div>",
        unsafe_allow_html=True
    )

st.markdown("---")
st.caption("Made with ❤️ using Streamlit")
