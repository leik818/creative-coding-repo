import tkinter as tk
import random  


root = tk.Tk()
root.title("Phone Dialer")
root.geometry("300x400")


dialed_number = tk.StringVar()


display = tk.Entry(root, textvariable=dialed_number, font=("Helvetica", 24), justify="right", bd=5)
display.grid(row=0, column=0, columnspan=3, padx=10, pady=20, sticky="nsew")

buttons = [
    '1', '2', '3',
    '4', '5', '6',
    '7', '8', '9',
    '*', '0', '#'
]


def press(_):
    current = dialed_number.get()
    random_digit = str(random.randint(0, 9)) 
    dialed_number.set(current + random_digit)


for index, label in enumerate(buttons):
    row = (index // 3) + 1
    col = index % 3
    button = tk.Button(root, text=label, font=("Helvetica", 20), command=lambda l=label: press(l))
    button.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)


for i in range(4):
    root.rowconfigure(i, weight=1)
for i in range(3):
    root.columnconfigure(i, weight=1)

root.mainloop()