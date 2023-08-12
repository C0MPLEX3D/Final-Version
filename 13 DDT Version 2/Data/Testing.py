import requests
import tkinter as tk
from tkinter import messagebox
import json

def get_nutrition():
    query = entry_query.get()
    api_url = f'https://api.api-ninjas.com/v1/nutrition?query={query}'
    response = requests.get(api_url, headers={'X-Api-Key': 'iq3i8dp7pwjmIbuCLYZ0mQ==DtkAcFwf90LgWAuS'})
    
    if response.status_code == requests.codes.ok:
        try:
            data = json.loads(response.text)
            print(data)  # Print the entire response for debugging
            
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
                messagebox.showerror("Error", "Invalid or empty response from the API.")
        except Exception as e:
            messagebox.showerror("Error", f"Error parsing response: {e}")
    else:
        messagebox.showerror("Error", f"Error: {response.status_code}\n{response.text}")

# Create the main window
root = tk.Tk()
root.title("Nutrition Information")

# Create and place widgets
label = tk.Label(root, text="Enter a query:")
label.pack(pady=10)

entry_query = tk.Entry(root, width=30)
entry_query.pack()

search_button = tk.Button(root, text="Search", command=get_nutrition)
search_button.pack(pady=10)

result_text = tk.Text(root, height=15, width=60, state=tk.DISABLED)
result_text.pack()

# Start the main loop
root.mainloop()
