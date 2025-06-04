import sys
print(sys.version)
print(sys.executable)

import streamlit as st
from few_shot import FewShotPosts
from post_generator import generate_post

# Daftar opsi untuk panjang postingan
length_options = ["Short", "Medium", "Long"]
language_options = ["Indonesia", "English"]

def main():
    # Judul dan deskripsi aplikasi
    st.markdown(
        "<h1 style='text-align: center; color: #4A90E2;'>🤖 LinkedIn Post Generator</h1>",
        unsafe_allow_html=True
    )
    st.markdown(
        "<p style='text-align: center; color: gray;'>Create engaging LinkedIn posts with AI assistance</p>",
        unsafe_allow_html=True
    )
    st.markdown("---")

    # Layout dropdown: topik, panjang, bahasa
    col1, col2, col3 = st.columns(3)

    fs = FewShotPosts()
    tags = fs.get_tags()

    with col1:
        st.selectbox("📌 Choose a Topic", options=tags, key="selected_tag")
    with col2:
        st.selectbox("✍️ Post Length", options=length_options, key="selected_length")
    with col3:
        st.selectbox("🌐 Language", options=language_options, key="selected_language")

    st.markdown("<br>", unsafe_allow_html=True)

    # Tombol Generate
    if st.button("🚀 Generate Post"):
        selected_tag = st.session_state.selected_tag
        selected_length = st.session_state.selected_length
        selected_language = st.session_state.selected_language

        post = generate_post(selected_length, selected_language, selected_tag)

        # Tampilan hasil dengan warna teks yang cukup terang
        st.markdown("### ✨ Generated Post")
        st.markdown(
            f"""
            <div style='
                background-color: #f0f2f6;
                color: #000000;
                padding: 20px;
                border-radius: 12px;
                font-size: 16px;
                line-height: 1.6;
            '>{post}</div>
            """,
            unsafe_allow_html=True
        )

if __name__ == "__main__":
    main()