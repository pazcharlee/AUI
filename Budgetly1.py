#!/usr/bin/env python
# coding: utf-8

import customtkinter as ctk
import tkinter.messagebox as tkmb
from datetime import datetime
import time

# Define user configurations
users = {
    "userA": {
        "password": "password",
        "security_answer": "red",
        "login_hours": (14, 23),
        "max_attempts": 2
    },
    "userB": {
        "password": "alpha",
        "security_answer": "blue",
        "login_hours": (9, 14),
        "max_attempts": 4
    },
    "userC": {
        "password": "bravo",
        "security_answer": "green",
        "login_hours": (8, 10),
        "max_attempts": 5
    }
}

class LoginApp:
    def __init__(self, root):
        self.root = root
        self.failed_attempts = {}
        self.security_triggered = {}
        self.setup_ui()

    def setup_ui(self):
        self.root.geometry("650x700")
        self.root.title("Budgetly.com")
        self.root.configure(fg_color="#0e1f26")

        frame = ctk.CTkFrame(master=self.root, fg_color="white")
        frame.pack(pady=70, padx=140, fill='both', expand=True)

        ctk.CTkLabel(master=frame, text="Budgetly", font=("Brush Script MT", 45), text_color="#06083a").pack(pady=45)
        ctk.CTkLabel(master=frame, text="Sign In", font=("Georgia", 25), text_color="#06083a").pack(pady=0)

        self.user_entry = ctk.CTkEntry(master=frame, placeholder_text="Username")
        self.user_entry.pack(pady=12)

        self.user_pass = ctk.CTkEntry(master=frame, placeholder_text="Password", show="*")
        self.user_pass.pack(pady=12)

        ctk.CTkCheckBox(master=frame, text="Remember Me", text_color="grey").pack(pady=12)

        self.sign_in_button = ctk.CTkButton(master=frame, text="Sign In", width=300, height=40, corner_radius=10, command=self.handle_login)
        self.sign_in_button.pack(pady=20)

        self.forgot_pass_button = ctk.CTkButton(master=frame, text="Forgot Password?", width=150, height=30, fg_color="white", text_color="#004481", hover_color="#eaf4fc", corner_radius=10)
        self.forgot_pass_button.pack(pady=5)

    def handle_login(self):
        self.login_attempt_time = time.time()
        print(f"Timestamp of Started Login: {self.login_attempt_time:.4f}")
        username = self.user_entry.get()
        password = self.user_pass.get()
        login_time = datetime.now()
        current_hour = login_time.hour

        if username not in self.failed_attempts:
            self.failed_attempts[username] = 0
            self.security_triggered[username] = False

        # Check credentials
        if username in users and password == users[username]["password"]:
            start_hour, end_hour = users[username]["login_hours"]
            if not (start_hour <= current_hour <= end_hour) and not self.security_triggered[username]:
                self.security_trigger_time = time.time()
                print(f"Timestamp when security question triggered due to unusual hours: {self.security_trigger_time:.4f}")
                print(f"Time taken to trigger security question: {self.security_trigger_time - self.login_attempt_time:.4f} seconds\n")

                tkmb.showwarning("Unusual Login Time", "Login Attempt Outside Usual Hours")
                self.security_triggered[username] = True
                self.current_user = username
                self.security_question()
                return
            else:
                self.open_new_window()
        else:
            self.failed_attempts[username] += 1
            tkmb.showerror("Login Failed", "Incorrect Username or Password")

            max_attempts = users.get(username, {}).get("max_attempts", 3)
            if self.failed_attempts[username] >= max_attempts and not self.security_triggered[username]:
                self.security_trigger_time = time.time()
                print(f"Timestamp when security question is triggered after {max_attempts} failed attempts: {self.security_trigger_time:.4f}")
                print(f"Time taken to trigger security question: {self.security_trigger_time - self.login_attempt_time: } seconds\n")

                tkmb.showwarning("Security Alert; Possible Breach", "Multiple Failed Login Attempts")
                self.security_triggered[username] = True
                self.current_user = username
                self.security_question()

    def open_new_window(self):
        time_login_completes = time.time()
        print(f"Time Login Completes: {time_login_completes}")
        print(f"Time Taken for Successful Login: {time_login_completes - self.login_attempt_time:.4f} seconds")
        new_window = ctk.CTkToplevel(self.root)
        new_window.geometry("400x300")
        new_window.title("Welcome to Budgetly")

        label = ctk.CTkLabel(master=new_window, text="Welcome to Budgetly!", font=("Times New Roman", 20))
        label.pack(pady=40)

        close_button = ctk.CTkButton(master=new_window, text="Close", width=200, command=new_window.destroy)
        close_button.pack(pady=20)

    def security_question(self):
        self.security_window = ctk.CTkToplevel(self.root)
        self.security_window.geometry("400x200")
        self.security_window.title("Security Question")

        question_label = ctk.CTkLabel(master=self.security_window, text="What is your favorite color?", font=("Arial", 14))
        question_label.pack(pady=20)

        self.answer_entry = ctk.CTkEntry(master=self.security_window, placeholder_text="Enter Answer")
        self.answer_entry.pack(pady=10)

        submit_button = ctk.CTkButton(master=self.security_window, text="Submit", command=self.check_answer)
        submit_button.pack(pady=10)

    def check_answer(self):
        answer = self.answer_entry.get().lower()
        expected_answer = users.get(self.current_user, {}).get("security_answer", "")

        if answer == expected_answer:
            tkmb.showinfo("Security Question Passed", "Correct answer!")
            self.security_window.destroy()
            self.open_new_window()
        else:
            tkmb.showinfo("Security Check Failed", "Incorrect Answer. Access Denied.")
            self.security_window.destroy()

if __name__ == "__main__":
    app = ctk.CTk()
    login_app = LoginApp(app)
    app.mainloop()
