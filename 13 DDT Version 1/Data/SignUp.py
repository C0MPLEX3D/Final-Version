import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import bcrypt
import subprocess

def register():
    Username = username_entry.get()
    Password1 = password_entry.get()
    Password2 = password_entry_confirm.get()

    db = open("DataBase/signupinfo.txt", "r")
    d = []
    for i in db:
        a, b = i.split(",")
        b = b.strip()
        c = a, b
        d.append(a)

    if not len(Password1) <= 4:
        if not Username == "":
            if len(Username) < 1:
                print("Please provide a username")
                return
            elif Username in d:
                print("Username exists")
                return
            else:
                if Password1 == Password2:
                    Password1 = Password1.encode('utf-8')
                    hashed_password = bcrypt.hashpw(Password1, bcrypt.gensalt())

                    db = open("DataBase/signupinfo.txt", "a")
                    db.write(Username + ", " + str(hashed_password) + "\n")
                    print("User created successfully!")
                    print("Please login to proceed:")
                else:
                    print("Passwords do not match")
                    return
    else:
        print("Password too short")
        return

    create_account_message = f"Username: {Username}\nPassword: {Password1}"
    messagebox.showinfo("Account Created", create_account_message)

def login():
    def check_login():
        username = username_entry.get()
        password = password_entry.get()
    window.destroy() #destroys current window
    subprocess.call(["python", "Data\Login.py"])

def adjust_spacing(event):
    width = window.winfo_width()
    height = window.winfo_height()
    font_size = max(int(width / 100), 30)
    spacing = max(int(width / 800), 5)
    button_width = max(int(width / 100), 20)

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

image_path = "images/background.png"
image = Image.open(image_path)
image = image.resize((initial_width, initial_height))
background_image = ImageTk.PhotoImage(image)

background_label = tk.Label(window, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

frame = tk.Frame(window, bg="#d0cdd1", padx=20, pady=20)

image = Image.open("images\scalelogo.png")
image = image.resize((500, 200))
image_tk = ImageTk.PhotoImage(image)


# Resize the login button image
login_width = 140  # Specify your desired width
login_height = 60  # Specify your desired height

signup_width = 200
signup_height = 80

imagesignup_path = "images\sign up.png"
imagesignup = Image.open(imagesignup_path)
imagesignup = imagesignup.resize((signup_width, signup_height))


# Convert the image background to transparent
imagesignup = imagesignup.convert("RGBA")
data = imagesignup.getdata()
new_data = []
for item in data:
    if item[:3] == (128, 128, 128):  # Change the RGB values to match the background color you want to make transparent
        new_data.append((128, 128, 128, 0))  # Make the background transparent
    else:
        new_data.append(item)
imagesignup.putdata(new_data)


# Convert the resized image to a Tkinter-compatible format
photosignup = ImageTk.PhotoImage(imagesignup)

# Read the login button image
imagelogin_path = "images/loginbutton.png"  # Replace with the actual image path
imagelogin = Image.open(imagelogin_path)
imagelogin = imagelogin.resize((login_width, login_height))

# Convert the image background to transparent
imagelogin = imagelogin.convert("RGBA")
data = imagelogin.getdata()
new_data = []
for item in data:
    if item[:3] == (128, 128, 128):  # Change the RGB values to match the background color you want to make transparent
        new_data.append((128, 128, 128, 0))  # Make the background transparent
    else:
        new_data.append(item)
imagelogin.putdata(new_data)


# Convert the resized image to a Tkinter-compatible format
photologin = ImageTk.PhotoImage(imagelogin)

image_label = tk.Label(frame, image=image_tk, bg="#d0cdd1")
username_label = tk.Label(frame, text="Username:", font=("Verdana", 12), bg="#d0cdd1")
username_entry = tk.Entry(frame, font=("Impact", 12))
password_label = tk.Label(frame, text="Password:", font=("Verdana", 12), bg="#d0cdd1")
password_entry = tk.Entry(frame, show="*", font=("Impact", 12))
password_label_confirm = tk.Label(frame, text="Confirm Password:", font=("Verdana", 12), bg="#d0cdd1")
password_entry_confirm = tk.Entry(frame, show="*", font=("Impact", 12))
login_button = tk.Button(frame, image=photologin, command=login, bd=0, highlightthickness=0)
signup_button = tk.Button(frame, image=photosignup, command=register, bd=0, highlightthickness=0)

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
