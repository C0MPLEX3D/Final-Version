"""
This script provides a graphical user interface (GUI) for user registration and login.
"""
import tkinter as tk
from tkinter import messagebox
import subprocess
import re
from PIL import Image, ImageTk
import bcrypt


def register():
    """
    Register a new user by validating input, 
    checking password complexity, hashing the password,
    and writing to the database.
    """
    # Get user input from entry fields
    username = username_entry.get()
    password1 = password_entry.get()
    password2 = password_entry_confirm.get()

    # Validate user input
    if len(username) < 1:
        messagebox.showerror("Error", "Please provide a username")
        return

    if len(password1) < 1:
        messagebox.showerror("Error", "Please provide a password")
        return

    if password1 != password2:
        messagebox.showerror("Error", "Passwords do not match")
        return

    # Read existing usernames from a file
    database_file = open("DataBase/signupinfo.txt", "r", encoding="utf-8")
    d = []
    for i in database_file:
        a, b = i.split(",")
        b = b.strip()
        d.append(a)

    # Validate password complexity
    if 4 <= len(password1) <= 10:
        if re.match("^[A-Za-z0-9]*$", username):
            # Allow only letters and numbers in the username
            if username in d:
                messagebox.showerror("Error", "Username exists")
                return
            else:
                # Check password complexity using regular expressions
                if not re.search(r'[A-Z]', password1):
                    messagebox.showerror("Error", "Password must contain at least one uppercase letter and at least one number")
                    return
                if not re.search(r'[a-z]', password1):
                    messagebox.showerror("Error","Password must contain at least one lowercase letter")
                    return
                if not re.search(r'[0-9]', password1):
                    messagebox.showerror("Error","Password must contain at least one number")
                    return

                # Hash the password using bcrypt
                password1 = password1.encode('utf-8')
                hashed_password = bcrypt.hashpw(password1, bcrypt.gensalt())

                # Write the new user to the database file
                db = open("DataBase/signupinfo.txt", "a")
                db.write(username + "," + str(hashed_password) + "\n")

        else:
            messagebox.showerror("Error", "Username must not include special characters")
            return
    else:
        messagebox.showerror("Error", "Password must be between 4 and 10 characters")
        return

    # Display a success message
    create_account_message = f"Username: {username}\nPassword: {password1}"
    messagebox.showinfo("Account Created", create_account_message)

# Function to handle login
def login():
    """
    Handle user login by checking credentials and opening the login window.
    """
    # Close the current window and open a new one for login
    window.destroy()
    subprocess.call(["python","Data\login.py"])

def adjust_spacing(event):
    """
    Adjust the spacing and layout of GUI elements based on window size.
    """
    # Calculate dimensions and adjust elements accordingly
    width = window.winfo_width()
    height = window.winfo_height()
    font_size = max(int(width / 100), 30)
    spacing = max(int(width / 800), 5)

    frame.pack_configure(pady=(height // 2 - frame.winfo_reqheight() // 2))

    username_entry.config(font=("Impact", font_size))
    password_entry.config(font=("Impact", font_size))
    password_entry_confirm.config(font=("Impact", font_size))

    image_label.pack(in_=frame)
    username_label.pack(in_=frame, pady=spacing)
    username_entry.pack(in_=frame, pady=spacing)
    password_label.pack(in_=frame, pady=spacing)
    password_entry.pack(in_=frame, pady=spacing)
    password_label_confirm.pack(in_=frame, pady=spacing)
    password_entry_confirm.pack(in_=frame, pady=spacing)
    signup_button.pack(in_=frame, pady=spacing)
    login_button.pack(in_=frame, pady=spacing)

window = tk.Tk()
window.title("Caloric Intake Calculator")
window.configure(bg="#5c5c5c")

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
initial_width = screen_width // 3 if screen_width % 3 == 0 else (screen_width // 3) - 1
initial_height = screen_height // 1 if screen_height % 1 == 0 else (screen_height // 1) - 1
window.geometry(f"{initial_width}x{initial_height}")

IMAGE_PATH = "images/background.png"
image = Image.open(IMAGE_PATH)
image = image.resize((initial_width, initial_height))
background_image = ImageTk.PhotoImage(image)

background_label = tk.Label(window, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

frame = tk.Frame(window, bg="#d0cdd1", padx=20, pady=20)

image = Image.open("images\scalelogo.png")
image = image.resize((500, 200))
image_tk = ImageTk.PhotoImage(image)


# Resize the login button image
LOGIN_WIDTH = 140
LOGIN_HEIGHT = 60

SIGNUP_WIDTH = 200
SIGNUP_HEIGHT = 80

IMAGESIGNUP_PATH = "images\sign up.png"
imagesignup = Image.open(IMAGESIGNUP_PATH)
imagesignup = imagesignup.resize((SIGNUP_WIDTH, SIGNUP_HEIGHT))


# Convert the image background to transparent
imagesignup = imagesignup.convert("RGBA")
data = imagesignup.getdata()
new_data = []
for item in data:

    if item[:3] == (128, 128, 128):
        new_data.append((128, 128, 128, 0))  # Make the background transparent
    else:
        new_data.append(item)

imagesignup.putdata(new_data)

# Convert the resized image to a Tkinter-compatible format
photosignup = ImageTk.PhotoImage(imagesignup)

# Read the login button image
IMAGELOGIN_PATH = "images/loginbutton.png"
imagelogin = Image.open(IMAGELOGIN_PATH)
imagelogin = imagelogin.resize((LOGIN_WIDTH, LOGIN_HEIGHT))

# Convert the image background to transparent
imagelogin = imagelogin.convert("RGBA")
data = imagelogin.getdata()
new_data = []
for item in data:
    if item[:3] == (128, 128, 128):
        new_data.append((128, 128, 128, 0))  # Make the background transparent
    else:
        new_data.append(item)
imagelogin.putdata(new_data)


# Convert the resized image to a Tkinter-compatible format
photologin = ImageTk.PhotoImage(imagelogin)

image_label = tk.Label(frame, image=image_tk, bg="#d0cdd1")
username_label = tk.Label(frame, text="Username:",
                          font=("Verdana", 12), bg="#d0cdd1")
username_entry = tk.Entry(frame, font=("Impact", 12))
password_label = tk.Label(frame, text="Password:",
                          font=("Verdana", 12), bg="#d0cdd1")
password_entry = tk.Entry(frame, show="*", font=("Impact", 12))
password_label_confirm = tk.Label(frame, text="Confirm Password:",
                                  font=("Verdana", 12), bg="#d0cdd1")
password_entry_confirm = tk.Entry(frame, show="*", font=("Impact", 12))
login_button = tk.Button(frame, image=photologin, command=login, bd=0,)
signup_button = tk.Button(frame, image=photosignup, command=register, bd=0,)

signup_button.config(bg="#d0cdd1", activebackground="#d0cdd1")
signup_button.image = photosignup

login_button.config(bg="#d0cdd1", activebackground="#d0cdd1")
login_button.image = photologin

frame.pack(pady=10)
image_label.pack(pady=(0.05, 5))
username_label.pack(pady=5)
username_entry.pack(pady=5)
password_label.pack(pady=5)
password_entry.pack(pady=5)
password_label_confirm.pack(pady=5)
password_entry_confirm.pack(pady=5)
signup_button.pack(pady=10)
login_button.pack(pady=1)

window.bind("<Configure>", adjust_spacing)

window.mainloop()
