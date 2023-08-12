from PIL import Image, ImageTk
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk


class CaloricIntakeCalculator:
    def __init__(self, master):
        self.master = master
        self.master.geometry('1000x2000')  # Set initial window size
        self.master.title('Caloric Intake Calculator')
        self.is_fullscreen = False

        # Create a background frame
        self.background_frame = tk.Frame(self.master)
        self.background_frame.place(x=0, y=0, relwidth=1, relheight=1)

        # Set the background image
        self.background_image = tk.PhotoImage(file="images/backgroundful.png")
        self.background_label = tk.Label(self.background_frame, image=self.background_image)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Create a content frame
        self.content_frame = tk.Frame(self.background_frame, bg="#d0cdd1")
        self.content_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self.image_title = Image.open("images/scalelogo.png")
        self.image_title = self.image_title.resize((600, 250))
        self.image_title = ImageTk.PhotoImage(self.image_title)
        self.label_title = tk.Label(self.content_frame, image=self.image_title, bg="#d0cdd1")
        self.label_title.pack(pady=20)

        # Add other content elements to the content frame
        self.label_gender = tk.Label(self.content_frame, text="Sex:", font=("Verdana", 14), fg="Black", bg="#d0cdd1")
        self.label_gender.pack(pady=2)

        self.radio_var = tk.StringVar()
        self.radio_var.set("male")

        self.radio_male = ttk.Radiobutton(self.content_frame, text="Male", variable=self.radio_var, value="male", style="TRadiobutton", command=self.update_button_state)
        self.radio_male.pack(pady=2)

        self.radio_female = ttk.Radiobutton(self.content_frame, text="Female", variable=self.radio_var, value="female", style="TRadiobutton", command=self.update_button_state)
        self.radio_female.pack()

        self.label_weight = tk.Label(self.content_frame, text="Weight (kg):", font=("Verdana", 14), fg="Black", bg="#d0cdd1")
        self.label_weight.pack()

        self.entry_weight = tk.Entry(self.content_frame, font=("Verdana", 12))
        self.entry_weight.pack()

        self.label_height = tk.Label(self.content_frame, text="Height (cm):", font=("Verdana", 14), fg="Black", bg="#d0cdd1")
        self.label_height.pack()

        self.entry_height = tk.Entry(self.content_frame, font=("Verdana", 12))
        self.entry_height.pack()

        self.label_age = tk.Label(self.content_frame, text="Age:", font=("Verdana", 14), fg="Black", bg="#d0cdd1")
        self.label_age.pack()

        self.entry_age = tk.Entry(self.content_frame, font=("Verdana", 12))
        self.entry_age.pack()

        self.label_activity_level = tk.Label(self.content_frame, text="Activity Level:", font=("Verdana", 14), fg="black", bg="#d0cdd1")
        self.label_activity_level.pack()

        self.activity_levels = ["Sedentary", "Lightly Active", "Moderately Active", "Very Active", "Extra Active"]
        self.activity_level_var = tk.StringVar()
        self.activity_level_var.set(self.activity_levels[0])

        self.dropdown_activity_level = tk.OptionMenu(self.content_frame, self.activity_level_var, *self.activity_levels)
        self.dropdown_activity_level.config(font=("Verdana", 12))
        self.dropdown_activity_level.pack()

        self.button_calculate = ttk.Button(self.content_frame, text="Calculate", style="TButton", command=self.calculate_caloric_intake, state="enabled")
        self.button_calculate.pack(pady=20)

        # Create custom styles for Radiobutton and Button
        style = ttk.Style()
        style.configure("TRadiobutton", background="#d0cdd1", foreground="black", font=("Verdana", 12))
        style.configure("TButton", background="#d0cdd1", foreground="black", font=("Verdana", 14))

    def update_button_state(self):
        if self.entry_weight.get() and self.entry_height.get() and self.entry_age.get() != '':
            self.button_calculate.config(state="enabled")
        else:
            self.button_calculate.config(state="disabled")

    def calculate_caloric_intake(self):
        try:
            weight = float(self.entry_weight.get())
            height = float(self.entry_height.get())
            age = int(self.entry_age.get())
            gender = self.radio_var.get()
            activity_level = self.activity_level_var.get()

            if gender == "male":
                bmr = 10 * weight + 6.25 * height - 5 * age + 5
            else:
                bmr = 10 * weight + 6.25 * height - 5 * age - 161

            activity_multiplier = 1.2  # Default value for sedentary activity level

            if activity_level == "Lightly Active":
                activity_multiplier = 1.375
            elif activity_level == "Moderately Active":
                activity_multiplier = 1.55
            elif activity_level == "Very Active":
                activity_multiplier = 1.725
            elif activity_level == "Extra Active":
                activity_multiplier = 1.9

            caloric_intake = bmr * activity_multiplier

            messagebox.showinfo("Caloric Intake", f"Your Basal Metabolic Rate (BMR) is: {bmr} calories per day.\n"
                                                   f"Your Total Daily Energy Expenditure (TDEE) is: {caloric_intake} calories per day.")

        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter numeric values for weight, height, and age.")


# Create the main window
root = tk.Tk()
app = CaloricIntakeCalculator(root)

# Start the main event loop
root.mainloop()
