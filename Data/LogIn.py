import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import bcrypt
import subprocess

# Function to display error popup
def show_error_popup(message):
    messagebox.showerror("Error", message)

# Function to navigate to the main page
def welcome():
    window.destroy()
    subprocess.call(["python", "Data\MainPage.py"])  # Open the MainPage.py file

# Function to attempt login
def gainAccess():
    Username = username_entry.get()
    Password = password_entry.get()

    if not len(Username or Password) < 1:
        # Read user data from the signupinfo.txt file
        db = open("DataBase\signupinfo.txt", "r")
        d = []
        f = []
        for i in db:
            # Split each line into username and hashed password
            a, b = i.split(",")
            b = b.strip()
            c = a, b
            d.append(a)  # Store usernames in a list
            f.append(b)  # Store hashed passwords in a list
            data = dict(zip(d, f))  # Create a dictionary of usernames and hashed passwords
        try:
            if Username in data:
                hashed = data[Username].strip('b')
                hashed = hashed.replace("'", "")
                hashed = hashed.encode('utf-8')

                try:
                    # Check if the entered password matches the hashed password
                    if bcrypt.checkpw(Password.encode(), hashed):
                        welcome()
                    else:
                        show_error_popup("Wrong password")
                except:
                    show_error_popup("Incorrect passwords or username")
            else:
                show_error_popup("Username doesn't exist")
        except:
            show_error_popup("Password or username doesn't exist")
    else:
        show_error_popup("Please attempt login again")

# Function to navigate to the registration page
def register():
    window.destroy()
    subprocess.call(["python", "Data\SignUp.py"])

# Function to adjust spacing of UI elements
def adjust_spacing(event):
    width = window.winfo_width()
    height = window.winfo_height()
    font_size = max(int(width / 100), 30)
    spacing = max(int(width / 500), 5)
    button_width = max(int(width / 200), 20)

    # Center the frame vertically
    frame.pack_configure(pady=(height // 2 - frame.winfo_reqheight() // 2))

    # Set font and width for username and password fields
    username_entry.config(font=("Impact", font_size), width=20)
    password_entry.config(font=("Impact", font_size), width=20)

    # Adjust spacing and pack UI elements into the frame
    image_label.pack(in_=frame, pady=(10, 50))
    username_label.pack(in_=frame, pady=spacing)
    username_entry.pack(in_=frame, pady=spacing)
    password_label.pack(in_=frame, pady=spacing)
    password_entry.pack(in_=frame, pady=spacing)
    login_button.pack(in_=frame, pady=spacing)
    signup_button.pack(in_=frame, pady=spacing)

# Create the main tkinter window
window = tk.Tk()
window.title("Caloric Intake Calculator")
window.configure(bg="grey")

# Get screen dimensions for initial window size
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
initial_width = screen_width // 3 if screen_width % 3 == 0 else (screen_width // 3) - 1
initial_height = screen_height // 1 if screen_height % 1 == 0 else (screen_height // 1) - 1
window.geometry(f"{initial_width}x{initial_height}")

# Set background image
image_path = "images/background.png"
image = Image.open(image_path)
image = image.resize((initial_width, initial_height))
background_image = ImageTk.PhotoImage(image)

# Create a label for the background image
background_label = tk.Label(window, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Create a frame to hold UI elements
frame = tk.Frame(window, bg="#d0cdd1", padx=20, pady=20)

# Load and resize logo image
image = Image.open("images\scalelogo.png")
image = image.resize((500, 200))
data = image.getdata()
image_tk = ImageTk.PhotoImage(image)

# Resize button images
login_width = 200
login_height = 80
signup_width = 140
signup_height = 60

# Load and convert signup button image
imagesignup_path = "images\sign up.png"
imagesignup = Image.open(imagesignup_path)
imagesignup = imagesignup.resize((signup_width, signup_height))
imagesignup = imagesignup.convert("RGBA")
data = imagesignup.getdata()
new_data = []
for item in data:
    if item[:3] == (128, 128, 128):
        new_data.append((128, 128, 128, 0))
    else:
        new_data.append(item)
imagesignup.putdata(new_data)
photosignup = ImageTk.PhotoImage(imagesignup)

# Load and convert login button image
imagelogin_path = "images/loginbutton.png"
imagelogin = Image.open(imagelogin_path)
imagelogin = imagelogin.resize((login_width, login_height))
imagelogin = imagelogin.convert("RGBA")
data = imagelogin.getdata()
new_data = []
for item in data:
    if item[:3] == (128, 128, 128):
        new_data.append((128, 128, 128, 0))
    else:
        new_data.append(item)
imagelogin.putdata(new_data)
photologin = ImageTk.PhotoImage(imagelogin)

# Create UI elements
image_label = tk.Label(frame, image=image_tk, bg="#d0cdd1")
username_label = tk.Label(frame, text="Username:", font=("Verdana", 12), bg="#d0cdd1")
username_entry = tk.Entry(frame, font=("Impact", 12))
password_label = tk.Label(frame, text="Password:", font=("Verdana", 12), bg="#d0cdd1")
password_entry = tk.Entry(frame, show="*", font=("Impact", 12))
password_label_confirm = tk.Label(frame, text="Confirm Password:", font=("Verdana", 12), bg="#d0cdd1")
password_entry_confirm = tk.Entry(frame, show="*", font=("Impact", 12))
login_button = tk.Button(frame, image=photologin, command=gainAccess, bd=0, highlightthickness=0)
signup_button = tk.Button(frame, image=photosignup, command=register, bd=0, highlightthickness=0)

# Configure button backgrounds and bind images
signup_button.config(bg="#d0cdd1", activebackground="#d0cdd1")
signup_button.image = photosignup

login_button.config(bg="#d0cdd1", activebackground="#d0cdd1")
login_button.image = photologin

# Pack UI elements into the frame
frame.pack(pady=10)
image_label.pack(pady=(0.05,5))
username_label.pack(pady=5)
username_entry.pack(pady=5)
password_label.pack(pady=5)
password_entry.pack(pady=5)
login_button.pack(pady=10)
signup_button.pack(pady=5)

# Bind the adjust_spacing() function to the window's <Configure> event
window.bind("<Configure>", adjust_spacing)

# Start the main event loop
window.mainloop()
