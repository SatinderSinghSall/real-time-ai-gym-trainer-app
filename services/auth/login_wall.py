import streamlit as st

from services.persistence.exercise_repository import get_or_create_user


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
            st.toast("Error: Fill in all the fields.", icon="❌")

            return False

        user = get_or_create_user(username=username)

        st.session_state["user_id"] = user["id"]
        st.session_state["username"] = user["username"]
        st.toast("Logged-in Successful!", icon="😍")

        st.rerun()

    return False

