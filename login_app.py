import customtkinter as ctk
import tkinter.messagebox as tkmb
from datetime import datetime
import smtplib
import random
import time 
import requests


class LoginApp:
    def __init__(self, root):
        self.root = root
        self.failed_attempts = 0
        self.security_answer = "red"
        self.setup_ui()

    def setup_ui(self):
        
     # Main frame
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
                                             command=self.handle_login)
        self.sign_in_button.pack(pady=20, padx=20)

        self.forgot_pass_button = ctk.CTkButton(master=frame, text="Forgot Password?", width=150, height=30, 
                                                 fg_color="white", text_color="#004481", hover_color="#eaf4fc", 
                                                 corner_radius=10)
        self.forgot_pass_button.pack(pady=5, padx=20)


    def handle_login(self):
        username = self.user_entry.get()
        password = self.user_pass.get()
        correct_username = "user123"
        correct_password = "password"
        if username == correct_username and password == correct_password:
            self.open_new_window()
        else:
            tkmb.showinfo("Failed Login", "Incorrect credentials. Please try again.")

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
        
def start_tkinter():
    # Your original Tkinter app code goes here, but inside this function
    def handle_login(self):
        username = self.user_entry.get()
        password = self.user_pass.get()
        correct_username = "user123"
        correct_password = "password"
        if username == correct_username and password == correct_password:
            self.open_new_window()
        else:
            tkmb.showinfo("Failed Login", "Incorrect credentials. Please try again.")

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
        
    app = ctk.CTk()
    frame = ctk.CTkFrame(master=app)
    frame.pack(pady=20, padx=20)

    # Add your Tkinter widgets here, similar to how you had them in the original script
    ctk.CTkLabel(master=frame, text="Welcome to Budgetly!", font=("Arial", 16)).pack(pady=20)
    
    app.mainloop()
       
