import streamlit as st
import pandas as pd
from streamlit import session_state as state

document_dict = {
        "Document ID": ["-", "-", "-"],
        "Instiution ID": ["-", "-", "-"],
        "Requester Name": ["-", "-", "-"],
        "Classification_Level": ["-", "-", "-"],
        "Last_Time_Added": ["-", "-", "-"],
        "Approval": ["-", "-", "-"],
        "Expiry_Date": ["-", "-", "-"],
    }
df_document = pd.DataFrame(document_dict)

def access_page():
    st.title("Access Page")

    if state.get('access_notif_clicked', False):
        st.write("There are no immidiate access request!")

    if st.button('Go to Main Page'):
        state.page = 'main'
        state.access_notif_clicked = True
        st.rerun()
        
    st.write("Access Management System")
    st.table(df_document)


    

if __name__ == "__main__":
    access_page()
