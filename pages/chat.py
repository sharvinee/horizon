import streamlit as st
from api_calls import get_api_response

st.set_page_config(page_title="Horizon Internal Medicine Clinic", page_icon="⚕", layout = "centered")

def main():
    if not st.experimental_user.is_logged_in:
        st.switch_page(page="pages/login.py")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    if st.sidebar.button(label="Back to Home Page"):
        st.session_state.session_id = None
        st.session_state.messages = []
        st.switch_page(page="pages/home.py")

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Enter your message"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.spinner("Generating response..."):
            response = get_api_response(prompt, st.session_state.session_id)
            
            # check if response was received from API
            if response:
                st.session_state.session_id = response.get('session_id')
                st.session_state.messages.append({"role": "assistant", "content": response['answer']})  # append assistant's response to session state
                
                with st.chat_message("assistant"):  #display AI assistant's response in chat interface
                    st.markdown(response['answer'])
                    
            else:  # display error message if API response fails
                st.error("Failed to get a response from the API. Please try again.")

if __name__ == "__main__":
    main()