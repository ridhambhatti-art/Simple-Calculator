import streamlit as st


st.title("...Calculatore...")
a = st.text_input("No1: ")
b = st.text_input("No2: ")

symbol = st.selectbox("Chose Operation: ", ('+' , '-' , '*' , '/'))
st.write("You selected: ", symbol)

if (st.button("Clickme")):
    if symbol == "+":
        st.write("Addition: ", float(a) + float(b))
    elif symbol == "-":
        st.write("Substraction: ", float(a) - float(b))
    elif symbol == "*":
        st.write("Multiplication: ", float(a) * float(b))
    elif symbol == "/":
        st.write("Division: ", float(a) / float(b))
    else:
        st.warning("Enter valid Operation")



