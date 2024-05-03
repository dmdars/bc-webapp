import streamlit as st
import bcrypt
import re
from db_conn import select_cmd, insert_cmd
import pycountry

class User:
    def __init__(self, first_name, last_name, email, password, id_number, gender, birthdate, birthplace, nationality, address, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.id_number = id_number
        self.gender = gender
        self.birthdate = birthdate
        self.birthplace = birthplace
        self.nationality = nationality
        self.address = address
        self.phone_number = phone_number


    def add_user(self):
        salt = bcrypt.gensalt()
        hashed_pass = bcrypt.hashpw(bytes(self.password, 'UTF-8'), salt)
        sql = f"insert into users(first_name, last_name, email, password, id_number, gender, birthdate, birthplace, nationality, address, phone_number) 
        values('{self.first_name}','{self.last_name}','{self.email}','{str(hashed_pass, 'UTF-8')}', '{self.id_number}', '{self.gender}', '{self.birthdate}', '{self.birthplace}', '{self.nationality}', '{self.address}', '{self.phone_number}')"
        return insert_cmd(sql)

    def check_email(self):
        sql = f"select email from users where email='{self.email}';"
        row = select_cmd(sql)
        if row:
            return True
        else:
            return False

    def check_form(self, password2):
        regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')

        name_check = False
        if not regex.search(self.first_name) == None:
            st.warning("Your first name has special characters are not allowed!")
        elif not regex.search(self.last_name) == None:
            st.warning("Your last name has special characters are not allowed!")
        else:
            name_check = True

        email_check = False
        if self.check_email():
            st.warning("The email is already registered.")
        else:
            email_check = True

        pass_check = False
        if self.password != password2:
            st.warning("Password does not match.")
        elif len(self.password) < 6 and len(self.password) > 16:
            st.warning("Password should be between 6 to 15 characters.")
        else:
            pass_check = True
        
        return name_check and email_check and pass_check

if __name__ == '__main__':
    countries = []
    for country in list(pycountry.countries):
        countries.append(country.name)

    with st.form(key="signup", clear_on_submit=True):
        st.header("Sign Up")
        first_name = st.text_input("First Name")
        last_name = st.text_input("Last Name")
        email = st.text_input("Email")
        password1 = st.text_input("Password", type='password')
        password2 = st.text_input("Confirm Password", type='password')
        id_number = st.text_input("ID Number")
        gender = st.radio("Gender", ["M", "F"], horizontal=True)
        birthdate = st.date_input("Birthdate")
        birthplace = st.text_input("Birthplace")
        nationality = st.selectbox("Nationality", countries)
        address = st.text_input("Address")
        phone_number = st.text_input("Phone Number")

        user = User(first_name, last_name, email, password1, id_number, gender, birthdate, birthplace, nationality, address, phone_number)

        submit = st.form_submit_button("Submit")
        if submit:
            if user.check_form(password2):
                user.add_user()
                st.write("Your data has been registered!")

    