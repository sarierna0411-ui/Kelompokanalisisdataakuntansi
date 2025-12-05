import streamlit as st

st.title("Aplikasi Pertama Erna di Streamlit")
st.write("Halo! Ini aplikasi sederhana dari Erna Sari.")

name = st.text_input("Masukkan nama kamu")
if name:
    st.success(f"Halo {name}, selamat datang di aplikasi Streamlit!")
