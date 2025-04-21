
#### assignment draft ###
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



##### IN CLASS ######
# import tkinter as tk

# root = tk.Tk()
# root.title("never login")
# root.geometry("300x200")

# # username label
# tk.Label(root, text="username:").pack()
# # username field
# username_entry = tk.Entry(root)
# username_entry.pack()

# # password label
# tk.Label(root, text="password:").pack()
# # password field
# password_entry = tk.Entry(root, show="*")
# password_entry.pack()

# # login btn
# login_button = tk.Button(root, text="login", font=("Helvetica", 12))
# login_button.pack(pady=10)

# # warning
# warning_label = tk.Label(root, text="", fg="red") #fg for foreground color
# warning_label.pack()

# def auto_erase():
#     username_entry.delete(0, tk.END) # delete chars .delete(start, end)
#     password_entry.delete(0, tk.END)
#     warning_label.config(text="re-enter your credentials...")
#     root.after(2000, auto_erase)

# root.after(2000, auto_erase) # delay 2 secs

# root.mainloop()


### evil slider ###
# root = tk.Tk()
# root.title("evil slider")
# root.geometry("400x250")

# label = tk.Label(root, text="slide to accept the terms and conditions", font=("Helvetica", 12))
# label.pack(pady=20) #.pack() makes sure the element show

# slider_value = tk.IntVar()

# message_label = tk.Label(root, text="", font=("Helvetica", 12))
# message_label.pack(pady=20)

# def check_slider(value):
#     if int(value) == 100:
#         message_label.config(text="you agreed 😈")
#         slider.config(state="disabled")  # disable the slider once hits 100

# slider = tk.Scale(root, from_=0, to=100, orient="horizontal", length=300,
#                   variable=slider_value, showvalue=True, command=check_slider)
# slider.pack()

# root.mainloop()

#### infinite confirm ###
#  import tkinter as tk
# import random

# import tkinter as tk

# def show_confirm(level=1):
#     confirm_window = tk.Toplevel()
#     confirm_window.title(f"confirm Level {level}")
#     confirm_window.geometry("300x100")

#     label = tk.Label(confirm_window, text=f"are you sure? (Level {level})", 
#                      font=("Times New Roman", 12))
#     label.pack(pady=10)

#     confirm_button = tk.Button(confirm_window, text="yes", command=lambda: show_confirm(level+1), 
#                                font=("Times New Roman", 12))
#     confirm_button.pack()

#     cancel_button = tk.Button(confirm_window, text="cancel", command=confirm_window.destroy, font=("Times New Roman", 12))
#     cancel_button.pack(pady=5)

# root = tk.Tk()
# root.title("infinite confirm")
# root.geometry("300x200")

# main_label = tk.Label(root, text="please confirm!")
# main_label.pack(pady=20)

# main_button = tk.Button(root, text="confirm!", font=("Times New Roman", 14), command=lambda: show_confirm(1))
# main_button.pack(pady=10)

# root.mainloop()

#### click me if you can ### 
# root = tk.Tk()
# root.title("click me if you can!")
# root.geometry("400x300")


# button = tk.Button(root, text="Click Me!", font=("Helvetica", 16))
# button.place(x=150, y=120)

# def move_button(event):
#     new_x = random.randint(0, 300)
#     new_y = random.randint(0, 220)
#     button.place(x=new_x, y=new_y)


# button.bind("<Enter>", move_button)

# root.mainloop() 

## in class phone button ###
# root = tk.Tk()
# root.title("You Used to Call Me on My Cell Phone")
# root.geometry("300x400")

# dialed_number = tk.StringVar()

# display = tk.Entry(root, textvariable=dialed_number, font=("Times New Roman", 24), justify="right", bd=5)
# display.grid(row=0, column=0, columnspan=3, padx=10, pady=20, sticky="nsew")

# buttons = [
#     '1', '2', '3',
#     '4', '5', '6',
#     '7', '8', '9',
#     '*', '0', '#'
# ]

# def press(key):
#     current = dialed_number.get()
#     dialed_number.set(current + key)

# for index, label in enumerate(buttons):
#     row = (index // 3) + 1  # start from row 1 because row 0 is display
#     col = index % 3
#     button = tk.Button(root, text=label, font=("Times New Roman", 20), command=lambda l=label: press(l))
#     button.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)

# for i in range(4):
#     root.rowconfigure(i, weight=1) # weight=1 makes row or column to grow/stretch
# for i in range(3):
#     root.columnconfigure(i, weight=1)

# root.mainloop()

### in class grid ###
# root = tk.Tk()
# root.title("grid")
# root.geometry("300x300")


# btn_00 = tk.Button(root, text="(0,0)")
# btn_00.grid(row=0, column=0, sticky="nsew")
# btn_00.grid(row=0, column=0, columnspan=2, sticky="nsew") # 

# #btn_01 = tk.Button(root, text="(0,1)")
# #btn_01.grid(row=0, column=1, sticky="nsew")

# btn_02 = tk.Button(root, text="(0,2)")
# btn_02.grid(row=0, column=2, sticky="nsew")

# # row 1
# btn_10 = tk.Button(root, text="(1,0)")
# btn_10.grid(row=1, column=0, sticky="nsew")

# btn_11 = tk.Button(root, text="(1,1)")
# btn_11.grid(row=1, column=1, sticky="nsew")

# btn_12 = tk.Button(root, text="(1,2)")
# btn_12.grid(row=1, column=2, sticky="nsew")

# # row 2
# btn_20 = tk.Button(root, text= "(2,0)")
# btn_20.grid(row=2, column=0, sticky="nsew")


# btn_21 = tk.Button(root, text="(2,1)")
# btn_21.grid(row=2, column=1, columnspan=2, sticky="nsew")

#btn_22 = tk.Button(root, text="(2,2)")
#btn_22.grid(row=2, column=2, sticky="nsew")

# for i in range(3):
#     root.rowconfigure(i, weight=1) # weight=1 lets the cells stretch if the window resizes
# for i in range(3):
#     root.columnconfigure(i, weight=1)

# root.mainloop()

### in class dice ###
# # window
# root = tk.Tk()
# root.title("D20 Roller")
# root.geometry("300x200")

# # label
# result_label = tk.Label(root, text="", font=("Comic Sans", 48), width=2, borderwidth=2, relief="solid")
# result_label.pack(pady=20)

# # roll dice function
# def roll_d20():
#     roll = random.randint(1, 20)
#     result_label.config(text=str(roll))

#     if roll < 10:
#         root.config(bg="pink")
#         result_label.config(bg="lightblue", fg="black")
#     else:
#         root.config(bg="pink")
#         result_label.config(bg="lightgreen", fg="white")

# # button with an event
# roll_button = tk.Button(root, text="Roll On!", font=("Comic Sans", 16), command=roll_d20)
# roll_button.pack(pady=10) # padding on the y direction

# # main loop
# root.mainloop()
