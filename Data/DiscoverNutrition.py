# Import necessary libraries and modules
import requests
import tkinter as tk
from tkinter import messagebox
import json
from PIL import Image, ImageTk
import re

# Function to retrieve nutrition information from the API
def get_nutrition():
    query = entry_query.get()

    # Check if the query contains only letters
    if not re.match("^[A-Za-z\s]+$", query):
        messagebox.showerror("Error", "Please enter only letters")
        return

    # API URL for nutrition data
    api_url = f'https://api.api-ninjas.com/v1/nutrition?query={query}'
    response = requests.get(api_url, headers={'X-Api-Key': 'iq3i8dp7pwjmIbuCLYZ0mQ==DtkAcFwf90LgWAuS'})
    
    # Handle successful response
    if response.status_code == requests.codes.ok:
        try:
            data = json.loads(response.text)
            print(data)  # Print the entire response for debugging
            
            # Clear and populate the result_text widget
            if data and isinstance(data, list):
                result_text.config(state=tk.NORMAL)
                result_text.delete(1.0, tk.END)
                
                for item in data:
                    if 'name' in item:
                        name = item['name']
                        result_text.insert(tk.END, f"Food Item: {name}\n")
                    
                    if 'calories' in item:
                        calories = item['calories']
                        result_text.insert(tk.END, f"Calories: {calories} cal\n")
                    
                    if 'serving_size_g' in item:
                        serving_size = item['serving_size_g']
                        result_text.insert(tk.END, f"Serving Size: {serving_size} g\n")
                    
                    if 'fat_total_g' in item:
                        fat = item['fat_total_g']
                        result_text.insert(tk.END, f"Fats: {fat} g\n")
                    
                    if 'carbohydrates_total_g' in item:
                        carbs = item['carbohydrates_total_g']
                        result_text.insert(tk.END, f"Carbohydrates: {carbs} g\n")
                    
                    if 'protein_g' in item:
                        protein = item['protein_g']
                        result_text.insert(tk.END, f"Protein: {protein} g\n")
                    
                    result_text.insert(tk.END, "\n")
                
                result_text.config(state=tk.DISABLED)
            else:
                messagebox.showerror("Error", "Invalid/Food Item Unavailable")
        except Exception as e:
            messagebox.showerror("Error", f"Error parsing response: {e}")
    else:
        messagebox.showerror("Error", f"Error: {response.status_code}\n{response.text}")

# Create the main tkinter window
root = tk.Tk()
root.title("Nutrition Information")
root.geometry("800x1000")

# Set up background image
background_image = Image.open("images/backgroundful.png")  # Change the path as needed
background_image = ImageTk.PhotoImage(background_image)
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

# Create and place a frame for content with a grey border
content_frame = tk.Frame(root, bg="#d0cdd1", bd=40)
content_frame.pack(padx=20, pady=20)

# Load and display the logo image
image_path = "images/nutrition logo.png"  # Change the path to your image file
image = Image.open(image_path)
image = image.resize((500, 300))  # Adjust the size as needed
image = ImageTk.PhotoImage(image)
image_label = tk.Label(content_frame, image=image, bg="#d0cdd1")
image_label.pack()

# Create and place widgets inside the content frame
label = tk.Label(content_frame, text="Enter a Food", bg="#d0cdd1", font=("Verdana", 20))
label.pack(pady=10)

entry_query = tk.Entry(content_frame, width=30, bd=2, relief="solid", justify="center", highlightthickness=2, highlightbackground="#000000")
entry_query.pack()

search_button = tk.Button(content_frame, text="Search", command=get_nutrition, font=("Verdana", 12))
search_button.pack(pady=10)

result_text = tk.Text(content_frame, height=15, width=60, state=tk.DISABLED, bd=2, relief="solid", highlightthickness=2, highlightbackground="#000000")
result_text.pack()

# Start the main loop
root.mainloop()
