import tkinter as tk
class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        # Create Entry Widget
        self.entry = tk.Entry(master, width=25, font=('Arial', 18), borderwidth=5)
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # Create Buttons
        button_list = [
            "1", "2", "3", "+",
            "4", "5", "6", "-",
            "7", "8", "9", "*",
            "C", "0", "=", "/"
        ]

        # Create a Dictionary to hold all the buttons
        self.buttons = {}

        # Loop over the button list and create a button for each item
        row = 1
        col = 0
        for label in button_list:
            # Define the button properties
            button = tk.Button(master, text=label, padx=20, pady=10, font=('Arial', 18), command=lambda label=label: self.button_click(label))
            self.buttons[label] = button

            # Position the button on the grid
            button.grid(row=row, column=col, padx=5, pady=5)

            # Update the row and column values
            col += 1
            if col > 3:
                row += 1
                col = 0

    def button_click(self, label):
        # Handle the button clicks
        if label == "C":
            # Clear the entry widget
            self.entry.delete(0, tk.END)
        elif label == "=":
            # Evaluate the expression and update the entry widget
            try:
                result = eval(self.entry.get())
                self.entry.delete(0, tk.END)
                self.entry.insert(0, str(result))
            except:
                # Handle invalid expressions
                self.entry.delete(0, tk.END)
                self.entry.insert(0, "Error")
        else:
            # Append the button label to the entry widget
            self.entry.insert(tk.END, label)


# Create the main window and run the application
root = tk.Tk()
calculator = Calculator(root)
root.mainloop()
