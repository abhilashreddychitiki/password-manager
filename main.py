from tkinter import *
from tkinter import messagebox

#Password Generator Project
import random
import pyperclip
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo("Error", "Please enter all fields")
    else:
        is_ok = messagebox.askyesnocancel(title=website,message=f"These are the details entered:\nEmail:{email}\nPassword:{password}\nIs it ok to save?")
        print(is_ok)
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f'{website},{email},{password}\n')
                website_entry.delete(0, END)
                password_entry.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

# Logo
canvas = Canvas(height=200, width=200, highlightthickness=0)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text='Website:')
website_label.grid(row=1, column=0, sticky='e')

email_label = Label(text='Email/Username:')
email_label.grid(row=2, column=0, sticky='e')

password_label = Label(text='Password:')
password_label.grid(row=3, column=0, sticky='e')

# Entries
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2, sticky='w')
website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2, sticky='w')

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1, sticky='w')

# Buttons
generate_password_button = Button(text="Generate Password",command=generate_password)
generate_password_button.grid(row=3, column=2, sticky='w')

add_button = Button(text="Add", width=36,command=save)
add_button.grid(row=4, column=1, columnspan=2, pady=10)

window.mainloop()
