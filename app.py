import streamlit as st

st.title("Ôn Tập Tiếng Anh")

# Danh sách từ vựng
words = [
    {"word": "Vocabulary", "meaning": "Từ vựng"},
    {"word": "Pronunciation", "meaning": "Phát âm"}
]

# Tạo trạng thái để nhớ việc lật thẻ
if 'flipped' not in st.session_state:
    st.session_state.flipped = False

def flip_card():
    st.session_state.flipped = not st.session_state.flipped

# Hiển thị thẻ đầu tiên
current_word = words[0]

# Giao diện thẻ
st.markdown("---")
if st.session_state.flipped:
    st.markdown(f"<h2 style='text-align: center; color: blue;'>{current_word['meaning']}</h2>", unsafe_allow_html=True)
else:
    st.markdown(f"<h2 style='text-align: center;'>{current_word['word']}</h2>", unsafe_allow_html=True)
st.markdown("---")

# Nút bấm lật thẻ
st.button("Lật thẻ", on_click=flip_card, use_container_width=True)
