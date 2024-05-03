import streamlit as st
from db_conn import select_cmd
from registration_form import check_email
import bcrypt

def check_credentials(email, password):

   if not check_email(email):
      st.warning("This email is not registered.")
      return False

   sql = f"select password from users where email = '{email}'"
   hashed_pass = select_cmd(sql)

   pass_check = bcrypt.checkpw(bytes(password, 'UTF-8'), hashed_pass)
   
   if pass_check:
      return True
   else:
      st.warning("Your password is wrong!")
      return False

with st.form("login_form"):
   email = st.text_input('Username/Email')
   password = st.text_input('Password', type='password')

   # Every form must have a submit button.
   submit = st.form_submit_button("Submit")
   if submit:
      if check_credentials(email, password):
         st.write("Go into home page")
      