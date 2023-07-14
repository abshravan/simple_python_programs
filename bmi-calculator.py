import tkinter as tk

class BMICalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("BMI Calculator")

        # Labels
        height_label = tk.Label(root, text="Height (cm):")
        height_label.grid(row=0, column=0, padx=10, pady=10)

        weight_label = tk.Label(root, text="Weight (kg):")
        weight_label.grid(row=1, column=0, padx=10, pady=10)

        bmi_label = tk.Label(root, text="BMI:")
        bmi_label.grid(row=2, column=0, padx=10, pady=10)

        # Input fields
        self.height_entry = tk.Entry(root)
        self.height_entry.grid(row=0, column=1, padx=10, pady=10)

        self.weight_entry = tk.Entry(root)
        self.weight_entry.grid(row=1, column=1, padx=10, pady=10)

        # Output field
        self.bmi_entry = tk.Entry(root, state="readonly")
        self.bmi_entry.grid(row=2, column=1, padx=10, pady=10)

        # Button
        calculate_button = tk.Button(root, text="Calculate", command=self.calculate_bmi)
        calculate_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    def calculate_bmi(self):
        height = float(self.height_entry.get())
        weight = float(self.weight_entry.get())

        # Calculate BMI
        bmi = weight / ((height / 100) ** 2)

        # Display the result
        self.bmi_entry.configure(state="normal")
        self.bmi_entry.delete(0, tk.END)
        self.bmi_entry.insert(tk.END, f"{bmi:.2f}")
        self.bmi_entry.configure(state="readonly")


if __name__ == "__main__":
    root = tk.Tk()
    bmi_calculator = BMICalculator(root)
    root.mainloop()
