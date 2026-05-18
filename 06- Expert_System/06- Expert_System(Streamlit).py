import streamlit as st

# App Title
st.title("Help Desk Expert System")

# User Input
problem = st.text_input("Enter your problem")

# Expert System Rules
if problem:

    p = problem.lower()

    if "password" in p:
        st.write("Solution: Reset password using Forgot Password option.")

    elif "internet" in p or "network" in p:
        st.write("Solution: Restart router and check network connection.")

    elif "printer" in p:
        st.write("Solution: Check printer connection and paper.")

    elif "virus" in p:
        st.write("Solution: Run antivirus scan.")

    elif "software" in p:
        st.write("Solution: Reinstall the software.")

    elif "bye" in p:
        st.write("Thank you for using the Expert System.")

    else:
        st.write("Solution not available.")