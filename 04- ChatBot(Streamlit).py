import streamlit as st

# Title
st.title("Customer Support Chatbot")

# User Input
user_input = st.text_input("Enter your message")

# Rule-Based Responses
if user_input:

    msg = user_input.lower()

    if "hi" in msg or "hello" in msg:
        st.success("Bot: Hello! How can I help you?")

    elif "order" in msg:
        st.success("Bot: Please provide your Order ID.")

    elif "return" in msg:
        st.success("Bot: Products can be returned within 7 days.")

    elif "refund" in msg:
        st.success("Bot: Refund will be processed soon.")

    elif "contact" in msg:
        st.success("Bot: Contact support@gmail.com")

    elif "bye" in msg:
        st.success("Bot: Thank you for visiting!")
        st.stop()

    else:
        st.error("Bot: Sorry, I did not understand.")