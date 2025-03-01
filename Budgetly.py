#!/usr/bin/env python
# coding: utf-8

# In[ ]:
import customtkinter as ctk
import tkinter.messagebox as tkmb
from datetime import datetime
import smtplib
import random
import time 
import requests

# Handle login function
def handle_login(username, password):
    correct_username = "user123"
    correct_password = "password"
    login_time = datetime.now()

    # Define usual login hours
    usual_login_start = login_time.replace(hour=13, minute=0, second=0)
    usual_login_end = login_time.replace(hour=14, minute=0, second=0)

    # Validate username and password
    if username == correct_username and password == correct_password:
        if login_time < usual_login_start or login_time > usual_login_end:
            tkmb.showwarning("Unusual Login Time", "Login Attempt Outside Usual Hours")
            return "security_question"  # Trigger security question
        else:
            return "success"  # Successful login
    else:
        return "failed"  # Incorrect login details

# Security question function
def security_question(security_answer="red"):
    answer = input("What is your favorite color? ").lower()
    if answer == security_answer:
        tkmb.showinfo("Security Question Passed", "Correct answer!")
        return True
    else:
        tkmb.showinfo("Security Check Failed", "Incorrect Answer. Access Denied.")
        return False

# LoginApp Class
class LoginApp:
    def __init__(self, root):
        self.root = root
        self.failed_attempts = 0
        self.security_answer = "red"  # Example security answer
        self.setup_ui()

    def setup_ui(self):
        # Main frame setup
        self.root.geometry("650x700")
        self.root.title("Budgetly.com")
        self.root.configure(fg_color="#0e1f26")

        frame = ctk.CTkFrame(master=self.root, fg_color="white")
        frame.pack(pady=70, padx=140, fill='both', expand=True)

        # Labels
        ctk.CTkLabel(master=frame, text="Budgetly", font=("Brush Script MT", 45), text_color="#06083a").pack(pady=45, padx=20)
        ctk.CTkLabel(master=frame, text="Sign In", font=("Georgia", 25), text_color="#06083a").pack(pady=0, padx=20)

        # Username and Password Entry
        self.user_entry = ctk.CTkEntry(master=frame, placeholder_text="Username")
        self.user_entry.pack(pady=12, padx=10)

        self.user_pass = ctk.CTkEntry(master=frame, placeholder_text="Password", show="*")
        self.user_pass.pack(pady=12, padx=10)

        # Remember Me Checkbox
        ctk.CTkCheckBox(master=frame, text="Remember Me", text_color="grey").pack(pady=12, padx=10)

        # Buttons
        self.sign_in_button = ctk.CTkButton(master=frame, text="Sign In", width=300, height=40, corner_radius=10, 
                                             command=self.handle_login)  # Bind the handle_login method here
        self.sign_in_button.pack(pady=20, padx=20)

        self.forgot_pass_button = ctk.CTkButton(master=frame, text="Forgot Password?", width=150, height=30, 
                                                 fg_color="white", text_color="#004481", hover_color="#eaf4fc", 
                                                 corner_radius=10)
        self.forgot_pass_button.pack(pady=5, padx=20)

    def handle_login(self):
        username = self.user_entry.get()  # Get username from the input field
        password = self.user_pass.get()  # Get password from the input field

        login_result = handle_login(username, password)  # Call the handle_login function

        # Process login result
        if login_result == "security_question":
            self.security_question()  # Trigger security question if login is outside usual hours
        elif login_result == "success":
            self.open_new_window()  # Open new window after successful login
        else:
            self.failed_attempts += 1
            tkmb.showerror("Login Failed", "Incorrect Username or Password")
            if self.failed_attempts == 3:
                tkmb.showwarning("Security Alert; Possible Breach", "Multiple Failed Login Attempts")
                self.security_question()

    def open_new_window(self):
        # Create a new window after successful login
        new_window = ctk.CTkToplevel(self.root)  # Create a new top-level window
        new_window.geometry("400x300")
        new_window.title("Welcome to Budgetly")

        # Add a label to the new window
        label = ctk.CTkLabel(master=new_window, text="Welcome to Budgetly!", font=("Times New Roman", 20))
        label.pack(pady=40)

        # Add a button to close the new window
        close_button = ctk.CTkButton(master=new_window, text="Close", width=200, command=new_window.destroy)
        close_button.pack(pady=20)

    def security_question(self):
        # Ask a security question if login attempt is made outside usual hours
        self.security_window = ctk.CTkToplevel(self.root)
        self.security_window.geometry("400x200")
        self.security_window.title("Security Question")

        # Add a label for the security question
        question_label = ctk.CTkLabel(master=self.security_window, text="What is your favorite color?", font=("Arial", 14))
        question_label.pack(pady=20)

        # Create an entry box for the user to input the answer
        self.answer_entry = ctk.CTkEntry(master=self.security_window, placeholder_text="Enter Answer")
        self.answer_entry.pack(pady=10)

        # Button to check the answer
        submit_button = ctk.CTkButton(master=self.security_window, text="Submit", command=self.check_answer)
        submit_button.pack(pady=10)

    def check_answer(self):
        # Check the user's answer to the security question
        answer = self.answer_entry.get().lower()
        if answer == self.security_answer:
            tkmb.showinfo("Security Question Passed", "Correct answer!")
            self.security_window.destroy()  # Close the security question window
            self.open_new_window()  # Open the new window after passing the security check
        else:
            tkmb.showinfo("Security Check Failed", "Incorrect Answer. Access Denied.")
            self.security_window.destroy()  # Close the security question window

# Run the application
if __name__ == "__main__":
    app = ctk.CTk()
    login_app = LoginApp(app)  # Create an instance of LoginApp
    app.mainloop()
