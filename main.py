import streamlit as st
from streamlit import session_state as state

def main():
    st.title("Main Page")
    
    # st.set_page_config(
    #     page_title="Main",
    #     page_icon="👋",
    # )

    st.write("# Welcome to Main User Interface! 👋")

    st.sidebar.success("Select which table you can access.")


    st.markdown(
        """
        Our app are dedicated to help fasten the registration process using blockchain powered apps
        \n
        👈 Select a page where your page has access to
    """
    )

    if state.access_notif_clicked is False:
        st.warning('you have an access request', icon="⚠️")

    if st.button('Check Access Table'):
        state.page = 'access_page'
        state.access_notif_clicked = True
        st.rerun()

    # if st.button('Go to Page 2'):
    #     state.page = 'access_page'
    #     st.experimental_rerun()
        

if __name__ == "__main__":
    main()
