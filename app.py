import streamlit as st
st.set_page_config(
    page_title="Multiplication App",
    page_icon="👋",
)

st.title('Multiplication')
st.text('This is a web app to multiply two numbers')
placeholder_c = st.empty()
placeholder_s = st.empty()
num1 = placeholder_c.number_input('Enter number 1')
num2 = placeholder_s.number_input('Enter number 2: ')
ans = num1*num2
st.subheader(f'Your answer is {ans}.')