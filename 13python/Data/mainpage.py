from PIL import Image, ImageTk
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from result_window import ResultWindow


# Create a class for the Caloric Intake Calculator
class CaloricIntakeCalculator:
    """
    A graphical user interface for a Caloric Intake Calculator.
    """
    # Initialize the class
    def __init__(self, master):  # Constructor, receives the main window as 'master'
        """
        Initialize the CaloricIntakeCalculator class.
        """
        self.master = master  # Store the main window

        # Set main window properties
        self.master.geometry('1000x2000')
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

        # Load and resize the title image
        self.image_title = Image.open("images/scalelogo.png")
        self.image_title = self.image_title.resize((700, 300))
        self.image_title = ImageTk.PhotoImage(self.image_title)
        self.label_title = tk.Label(self.content_frame,
                                    image=self.image_title, bg="#d0cdd1")
        self.label_title.grid(row=0, column=0,
                              columnspan=2, pady=20)  # Display the title image

        # Add other content elements to the content frame
        self.label_gender = tk.Label(self.content_frame, text="Sex:",
                                     font=("Verdana", 14), fg="Black", bg="#d0cdd1")
        self.label_gender.grid(row=1, column=0, sticky="E", pady=2)

        style = ttk.Style()
        style.configure("TRadiobutton", background="#d0cdd1",
                        foreground="black", font=("Verdana", 12))

        # Define the style for the Calculate button
        style.configure("TButton", borderwidth=0, padding=0, relief=tk.FLAT,
                        background="#d0cdd1", activebackground="#d0cdd1")

        self.radio_var = tk.StringVar()
        self.radio_var.set("male")

        self.radio_male = ttk.Radiobutton(self.content_frame, text="Male",
                                          variable=self.radio_var, value="male",
                                          style="TRadiobutton",
                                          command=self.update_button_state)
        self.radio_male.grid(row=1, column=1, sticky="W", pady=2)

        self.radio_female = ttk.Radiobutton(self.content_frame, text="Female",
                                            variable=self.radio_var,
                                            value="female", style="TRadiobutton",
                                            command=self.update_button_state)
        self.radio_female.grid(row=2, column=1, sticky="W", pady=2)

        self.label_weight = tk.Label(self.content_frame, text="Weight (kg):",
                                     font=("Verdana", 14), fg="Black",
                                     bg="#d0cdd1")
        self.label_weight.grid(row=3, column=0, sticky="E", pady=2)

        self.entry_weight = tk.Entry(self.content_frame, font=("Verdana", 12),
                                     width=20, bd=2, relief="solid",
                                     justify="center", highlightthickness=2,
                                     highlightbackground="#000000")
        self.entry_weight.grid(row=3, column=1, sticky="W", pady=20)

        self.label_height = tk.Label(self.content_frame, text="Height (cm):",
                                     font=("Verdana", 14), fg="Black",
                                     bg="#d0cdd1")
        self.label_height.grid(row=4, column=0, sticky="E", pady=20)

        self.entry_height = tk.Entry(self.content_frame, font=("Verdana", 12),
                                     width=20, bd=2, relief="solid",
                                     justify="center", highlightthickness=2,
                                     highlightbackground="#000000")
        self.entry_height.grid(row=4, column=1, sticky="W", pady=20)

        self.label_age = tk.Label(self.content_frame, text="Age:",
                                  font=("Verdana", 14), fg="Black", bg="#d0cdd1")
        self.label_age.grid(row=5, column=0, sticky="E", pady=20)

        self.entry_age = tk.Entry(self.content_frame, font=("Verdana", 12),
                                  width=20, bd=2, relief="solid",
                                  justify="center", highlightthickness=2,
                                  highlightbackground="#000000")
        self.entry_age.grid(row=5, column=1, sticky="W", pady=20)

        self.label_activity_level = tk.Label(self.content_frame,
                                             text="Activity Level:", font=("Verdana", 14),
                                              fg="black", bg="#d0cdd1")
        self.label_activity_level.grid(row=6, column=0, sticky="E", pady=20)

        self.activity_levels = ["Sedentary", "Lightly Active",
                                "Moderately Active", "Very Active", "Extra Active"]
        self.activity_level_var = tk.StringVar()
        self.activity_level_var.set(self.activity_levels[0])

        self.dropdown_activity_level = tk.OptionMenu(self.content_frame,
                                                     self.activity_level_var, *self.activity_levels)
        self.dropdown_activity_level.config(font=("Verdana", 12))
        self.dropdown_activity_level.grid(row=6, column=1, sticky="W", pady=2)

        # Create a custom image button for "Calculate"
        self.calculate_image = Image.open("images/button_calculate.png")
        self.calculate_image = self.calculate_image.resize((200, 60))
        self.calculate_image = ImageTk.PhotoImage(self.calculate_image)

        # Set the "TButton" style to the "button_calculate" button
        self.button_calculate = ttk.Button(self.content_frame, image=self.calculate_image,
                                           command=self.calculate_caloric_intake)
        self.button_calculate.grid(row=7, column=0, columnspan=2, pady=20)

    # Method to update the state of the calculate button based on input validity
    def update_button_state(self):
        """
        Update the state of the calculate button based on input validity.
        """
        # Check if weight, height, and age are all provided
        if self.entry_weight.get() and self.entry_height.get() and self.entry_age.get() != '':
            self.button_calculate.config(state="enabled")  # Enable the calculate button
        else:
            self.button_calculate.config(state="disabled")  # Disable the calculate button

    # Method to determine the BMI category based on the BMI value
    def get_bmi_category(self, bmi):
        """
        Determine the BMI category based on the BMI value.
        """
        if bmi < 18.5:
            return "Underweight"  # Return category if BMI is less than 18.5
        elif 18.5 <= bmi < 24.9:
            return "Healthy"  # Return category if BMI is between 18.5 and 24.9
        elif 24.9 <= bmi < 29.9:
            return "Overweight"  # Return category if BMI is between 24.9 and 29.9
        else:
            return "Obese"  # Return category if BMI is 30 or greater

    def calculate_caloric_intake(self):
        """
        Calculate the caloric intake and display the result in a new window.
        """
        try:
            weight = float(self.entry_weight.get())
            height = float(self.entry_height.get())
            age = int(self.entry_age.get())
            gender = self.radio_var.get()
            activity_level = self.activity_level_var.get()

            # Calculate BMI
            bmi = weight / ((height / 100) ** 2)


            #Calcuate BMR
            if gender == "male":
                bmr = 10 * weight + 6.25 * height - 5 * age + 5
            else:
                bmr = 10 * weight + 6.25 * height - 5 * age - 161

            activity_multiplier = 1.2  # Default value for sedentary activity level

            #Determine Activity level
            if activity_level == "Lightly Active":
                activity_multiplier = 1.375
            elif activity_level == "Moderately Active":
                activity_multiplier = 1.55
            elif activity_level == "Very Active":
                activity_multiplier = 1.725
            elif activity_level == "Extra Active":
                activity_multiplier = 1.9

            caloric_intake = bmr * activity_multiplier

            average_weight = (height - 100) - ((height - 150) / 4) + ((age - 20) / 4)
            healthy_weight = (height - 100) - ((height - 150) / 2.5) + ((age - 20) / 4)

            bmi_category = self.get_bmi_category(bmi)

            #Create Dictionary with calcualted Data for display
            calculated_data = {
            "bmi": bmi,
            "bmr": bmr,
            "tdee": caloric_intake,
            "sedentary": bmr * 1.2,
            "lightly_active": bmr * 1.375,
            "moderately_active": bmr * 1.55,
            "very_active": bmr * 1.725,
            "extra_active": bmr * 1.9,
            "average_weight": average_weight,
            "healthy_weight": healthy_weight
        }
            #Create an instance of ResultWindow and pass calcualted data
            result_window = ResultWindow(self.master, calculated_data)

        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter numeric values for weight, height, and age.")

# Create the main window
root = tk.Tk()
app = CaloricIntakeCalculator(root)


root.mainloop()
