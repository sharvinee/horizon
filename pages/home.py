import streamlit as st
import uuid

st.set_page_config(page_title="Horizon Internal Medicine Clinic", page_icon="⚕", layout = "centered")

def main():
    if not st.experimental_user.is_logged_in:
        st.switch_page(page="pages/login.py")

    if "session_id" not in st.session_state:
        st.session_state.session_id = str(uuid.uuid4())
    elif st.session_state.session_id is None:
        st.session_state.session_id = str(uuid.uuid4())

    with st.sidebar:
        if st.button(label="Logout"):
            st.logout()
    
    # Custom CSS to align the title
    st.markdown(
        """
        <style>
        .title {
            text-align: center;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown('<h1 class="title">🩺 Horizon Internal Medicine Clinic AI Assistant</h1>', unsafe_allow_html=True)
    st.markdown('<h5 class="title">"Access All the Clinic Information You Need - No Wait, No Hassle"</h5>', unsafe_allow_html=True)

    if st.button("Go to Chat Page"):
        st.switch_page(page="pages/chat.py")


if __name__ == "__main__":
   main()