"""
This module defines the ResultWindow class, which displays calculated caloric intake results.
"""
import subprocess
import tkinter as tk
from PIL import Image, ImageTk



# Define a custom class for the Result Window
class ResultWindow(tk.Toplevel):
    """
    Custom class for the Result Window that displays calculated caloric intake results.
    """
    def __init__(self, parent, calculated_data):
        """
        Initialize the ResultWindow class.
        """
        super().__init__(parent)
        self.title("Caloric Intake Results")
        self.geometry("1000x800")
        # Define a custom class for the Result Window
        self.calculated_data = calculated_data
        # Load the background image
        self.background_image = Image.open(r"images/backgroundful.png")
        self.background_photo = ImageTk.PhotoImage(self.background_image)
        # Create a canvas to display the background image
        self.canvas = tk.Canvas(self, width=800, height=500)
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.canvas.create_image(0, 0,
                                 image=self.background_photo, anchor=tk.NW)
        # Create a frame to hold content
        self.frame = tk.Frame(self, bg="#d0cdd1")
        self.frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.logo_image = Image.open("images/scalelogo.png")
        self.logo_image = self.logo_image.resize((500, 200))
        self.logo_photo = ImageTk.PhotoImage(self.logo_image)
        self.logo_label = tk.Label(self.frame,
                                   image=self.logo_photo, bg="#d0cdd1")
        self.logo_label.pack(pady=10)
        self.update_results()
        # Add text label before the button
        self.text_label = tk.Label(self,
                                   text="Search calories and macros for foods to achieve your goals!",
                                   font=("Verdana", 12))
        self.text_label.pack(side=tk.LEFT, padx=10, pady=10)
        # Add the extra button on the side
        self.extra_button_image = Image.open(r"images\DiscoverNutrition.png")
        self.extra_button_image = self.extra_button_image.resize((180, 40))
        self.extra_button_photo = ImageTk.PhotoImage(self.extra_button_image)
        self.extra_button = tk.Button(self, image=self.extra_button_photo,
                                      command=self.perform_extra_action, borderwidth=0)
        self.extra_button.pack(side=tk.LEFT, padx=5, pady=10)

    # Create a frame to hold content
    def perform_extra_action(self):
        """
        Open another window or perform an extra action.
        """
        subprocess.call(["python", r"Data\discovernutrition.py"])

    def get_bmi_category(self, bmi):
        """
        Determine the BMI category based on the BMI value.
        """
        if bmi < 18.5:
            return "Underweight"
        if 18.5 <= bmi < 24.9:
            return "Normal Weight"
        if 25 <= bmi < 29.9:
            return "Overweight"
        else:
            return "Obese"

    # Method to update the results display
    def update_results(self):
        """
        Update the results display.
        """
        bmi = self.calculated_data['bmi']
        bmi_category = self.get_bmi_category(bmi)
        result_text = (
            f"Caloric Intake Results\n\n For weight loss or gain, intake either below or above the BMR calories \n\n"
            f"- Your Basal Metabolic Rate (BMR): {int(self.calculated_data['bmr']):,} calories per day\n"
            f"- Your Total Daily Energy Expenditure (TDEE): {int(self.calculated_data['tdee']):,} calories\n"
            f"- Your Body Mass Index (BMI): {bmi:.1f} ({bmi_category})\n\n"
            "TDEE for different Activity Levels:\n"
            f"- Sedentary: {int(self.calculated_data['sedentary']):,} calories\n"
            f"- Lightly Active: {int(self.calculated_data['lightly_active']):,} calories\n"
            f"- Moderately Active: {int(self.calculated_data['moderately_active']):,} calories\n"
            f"- Very Active: {int(self.calculated_data['very_active']):,} calories\n"
            f"- Extra Active: {int(self.calculated_data['extra_active']):,} calories\n\n"
            "Weight Information:\n"
            f"- Average Weight for your height and age: {int(self.calculated_data['average_weight']):,} kg\n"
            f"- Healthy Weight for your height and age: {int(self.calculated_data['healthy_weight']):,} kg"
        )
        # Update frame geometry to calculate size
        self.frame.update_idletasks()
        text_widget = tk.Label(self.frame, text=result_text,
                               font=("Helvetica", 14),
                               bg="#d0cdd1", justify="left")
        text_widget.pack(fill=tk.BOTH,
                         expand=True, padx=20, pady=10)

# Test the ResultWindow class
if __name__ == "__main__":
    root = tk.Tk()
    calculated_data = {
        "bmi": 24.5,
        "bmr": 1800,
        "tdee": 2200,
        "sedentary": 2100,
        "lightly_active": 2350,
        "moderately_active": 2550,
        "very_active": 2700,
        "extra_active": 2900,
        "average_weight": 70,
        "healthy_weight": 75
    }
    result_window = ResultWindow(root, calculated_data)
    root.mainloop()
