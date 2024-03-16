import streamlit as st
import snowflake.connector
from snowflake.connector import Error
import time

st.set_page_config(page_title='Login/Signup', initial_sidebar_state="collapsed", layout="wide", menu_items="None")
# Connect to Snowflake
def connect_to_snowflake():
    try:
        conn = snowflake.connector.connect(
            user='HIMANSHU',
            password='pygsim-3fyvqo-nabweB',
            account='pz16085.us-east-2.aws',
            warehouse='COMPUTE_WH',
            database='RESUMES',
            schema='PUBLIC'
        )
        return conn
    except Error as e:
        st.error(f"Error connecting to Snowflake: {e}")

# Function to check if email exists in Snowflake

# Function to create account in Snowflake
def create_account(first_name, last_name, email, password):
    conn = connect_to_snowflake()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO USERS (first_name, last_name, email, password) VALUES (%s, %s, %s, %s)",
                           (first_name, last_name, email, password))
            conn.commit()
            st.success("Account created successfully!")
        except Error as e:
            st.error(f"Error creating account in Snowflake: {e}")
        finally:
            cursor.close()
            conn.close()

# Streamlit app
def signup():
    tab1, tab2, tab3, tab4, tab5, tab6, tab7= st.tabs(["Signup","  ","  "," | ","  ","  ","Login"])
    with tab1:
        c1,c2 = st.columns([3,4])
        with c1:
            st.title("Sign Up")
            def check_email(email):
                conn = connect_to_snowflake()
                if conn:
                    try:
                        cursor = conn.cursor()
                        cursor.execute("SELECT * FROM USERS WHERE email = %s", (email,))
                        rows = cursor.fetchall()
                        if rows:
                            return True  # Email exists
                        else:
                            return False  # Email doesn't exist
                    except Error as e:
                        st.error(f"Invalid Email address{e}")
                    finally:
                        cursor.close()
                        conn.close()
            # User input fields
            first_name = st.text_input("First Name")
            last_name = st.text_input("Last Name")
            email = st.text_input("Email")
            password = st.text_input("Create new password", type="password")
            confirm_password = st.text_input("Confirm new password", type="password")

            if first_name and last_name and email and password and confirm_password:
                if st.button("Sign Up"):
                    if password != confirm_password:
                        st.error("Passwords do not match!")
                    else:
                        email_exists = check_email(email)
                        if email_exists:
                            st.error("Email already exists! Please use a different email.")
                        else:
                            create_account(first_name, last_name, email, password)
                            time.sleep(3)
                            st.switch_page("pages/Check your resume score.py")   

    with tab7:
        c1,c2 = st.columns([3,4])
        with c1:
            def check_email(email):
                conn=connect_to_snowflake()
                cursor = conn.cursor()
                query = f"SELECT COUNT(*) FROM USERS WHERE email = '{email}'"
                cursor.execute(query)
                result = cursor.fetchone()[0]
                cursor.close()
                conn.close()
                return result > 0
            def verify_password(email, password):
                conn=connect_to_snowflake()
                cursor = conn.cursor()
                query = f"SELECT password FROM users WHERE email = '{email}'"
                cursor.execute(query)
                stored_password = cursor.fetchone()[0]
                cursor.close()
                conn.close()
                return password == stored_password
            def get_first_name(email):
                conn = connect_to_snowflake()
                cursor = conn.cursor()
                query = f"SELECT first_name FROM USERS WHERE email = '{email}'"
                cursor.execute(query)
                first_name = cursor.fetchone()[0]
                cursor.close()
                conn.close()
                return first_name
            
            def login():
                st.title("Login")
    
                # User input fields
                email = st.text_input("Email-Id")
                password = st.text_input("Password", type="password")
    
                if st.button("Login"):
                    email_exists = check_email(email)
                    if not email_exists:
                        st.error("Email not found! Please register.")
                    else:
                        password_match = verify_password(email, password)
                        if not password_match:
                            st.error("Incorrect password! Please try again.")
                        else:
                            first_name = get_first_name(email)
                            st.success(f"Login successful! Welcome back, {first_name}")
                            time.sleep(3)
                            st.switch_page("pages/Check your resume score.py")    
    
            if __name__ == "__main__":
                login()
#_----------------------------------------

if __name__ == "__main__":
    signup()

# st.page_link("pages/Login", label="Log-In")
