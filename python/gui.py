import tkinter as tk

root = tk.Tk()

# create an Entry widget
entry = tk.Entry(root)
entry.pack()

# define a function to get the value of the Entry widget
def get_input():
    user_input = entry.get()
    print(f"User entered: {user_input}")

# create a button to get the value of the Entry widget
button = tk.Button(root, text="Get input", command=get_input)
button.pack()

root.mainloop()
