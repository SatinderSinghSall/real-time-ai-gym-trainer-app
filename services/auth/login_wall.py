import time
import streamlit as st


def render_login_wall():
    if st.session_state.get("user_id") is not None:
        return True

    st.title("🏋️ AI Real-Time GYM Coach")
    st.markdown("### Welcome, please enter a unique username.")

    with st.form("login_form", clear_on_submit=False):
        username = st.text_input("Name (Unique Name):", placeholder="Please Enter a Unique Name... e.g. Satinder Singh Sall")
        submit_button = st.form_submit_button("Start Session!", width="stretch")

    if submit_button:
        if not username:
            st.error("Name can not be empty. Try again!", icon="❌")
            st.toast("Error: Fill in all the fields.", icon="😍")
            time.sleep(3)

            return False

        st.toast("Logged-in Successful!", icon="😍")
        time.sleep(3)
        st.session_state["username"] = username
        st.session_state["user_id"] = '001'
        st.rerun()

    return False

