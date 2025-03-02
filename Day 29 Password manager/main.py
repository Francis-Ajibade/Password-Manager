from tkinter import *
from tkinter import messagebox, ttk
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import random


button_pressed = 0
def password_generator():
    global button_pressed
    button_pressed += 1
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for _ in range(nr_letters)]
    password_list += [random.choice(symbols) for _ in range(nr_symbols)]
    password_list += [random.choice(numbers) for _ in range(nr_numbers)]

    random.shuffle(password_list)

    #using the join function
    password = "".join(password_list)
    password_entry.insert(0, password)
    if button_pressed > 1:
        password_entry.delete(0, END)
        password_entry.insert(0, password)
    pyperclip.copy(password_entry.get())



# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_to_text():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if website.isspace() or password.isspace():
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any of the fields empty")
    elif len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any of the fields empty")
    else:
        is_okay = messagebox.askokcancel(title=website,
                                         message=f"These are the details enetered: \nEmail: {email}\nPassword: {password}\n Is it okay to save? ")
        if is_okay:
            with open("data.txt", "a") as fi:
                print(f"{website_entry.get()} | {email_entry.get()} | {password_entry.get()}", file=fi)
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=20)

#image canvas
canvas = Canvas(width=200, height=200,  highlightthickness=2)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)

#Label
txt_label1 = ttk.Label(text="website:")
txt_label2 = ttk.Label(text="Email/Username:")
txt_label3 = ttk.Label(text="Password:")

#Entries
website_entry = ttk.Entry(width=35)
website_entry.focus()
email_entry = ttk.Entry(width=35)
email_entry.insert(0, "melonrice15@gmail.com")
password_entry = ttk.Entry(width=21)

#Buttons
password_generate_button = ttk.Button(text="Generate Password", command=password_generator)
add_button = ttk.Button(text="Add", command=add_to_text, width=36)

#GRID
canvas.grid(row=0, column=1)
txt_label1.grid(row=1, column=0)
txt_label2.grid(row=2, column=0)
txt_label3.grid(row=3, column=0)

website_entry.grid(row=1, column=1, columnspan=2, sticky="EW")
email_entry.grid(row=2, column=1, columnspan=2, sticky="EW")
password_entry.grid(row=3, column=1, sticky="EW")

password_generate_button.grid(row=3, column=2, sticky="EW")
add_button.grid(row=4, column=1, columnspan=2, sticky="EW")

window.mainloop()
