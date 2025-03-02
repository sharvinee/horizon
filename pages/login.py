import streamlit as st
st.set_page_config(page_title="Horizon Internal Medicine Clinic", page_icon="⚕", layout = "centered")

def main():
    st.title(body="This is the login page.")

    if st.experimental_user.is_logged_in:
        st.switch_page(page="pages/home.py")

    if st.button(label="Login"):
        if not st.experimental_user.is_logged_in:
            st.login()

if __name__ == "__main__":
    main()