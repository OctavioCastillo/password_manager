from tkinter import *
from tkinter import messagebox
from random import randint, shuffle, choice
# Pyperclip is a cross-platform Python module for copy and paste clipboard functions
import pyperclip
import json


# ---------------------------- FIND PASSWORD ------------------------------------ #

def find_pwd():
    website = web_entry.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showwarning(title="FileNotFound", message="No Data File Found")
    except KeyError:
        messagebox.showwarning(title="Keyword error", message="Website doesn't exist in file")

    else:
        email = data[website]["email"]
        pwd = data[website]["password"]
        messagebox.showinfo(title="Website", message=f"Site: {website}"
                                                     f"\nEmail: {email}"
                                                     f"\nPassword: {pwd}")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pwd():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # Get random char list
    password_list = []
    password_list += [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]

    # Shuffle the list
    shuffle(password_list)

    # Add every char into a string
    # join method, check documentation
    password = "".join(password_list)

    pyperclip.copy(password)

    # Insert the generated password into the password entry
    password_entry.delete(0, END)
    password_entry.insert(END, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

# Save the data in the file
def add():
    website = web_entry.get()
    email = email_user_entry.get()
    pwd = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": pwd,
        }
    }

    # Check if all fields have info
    if len(website) == 0 or len(email) == 0 or len(pwd) == 0:
        messagebox.showwarning(title="Oops", message="Please don't leave any fields empty")
    # If all fields completed, proceed to save
    else:
        try:
            # The file is in the desktop
            with open("./data.json", "r") as data_file:
                # reading old data
                data = json.load(data_file)
                # updating old data with new data
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)

        else:
            data.update(new_data)

            with open("data.json", "w") as data_file:
                # saving updated data
                json.dump(data, data_file, indent=4)
        finally:

            # Clear entry after press Add button
            web_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

# Create window
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="white")

# Create lock logo
canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
lock_img = PhotoImage(file="./img.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(row=0, column=1)

# Labels

web_label = Label(text="Website:", bg="white", fg="black")
web_label.grid(row=1, column=0)

email_user_label = Label(text="Email/Username:", bg="white")
email_user_label.grid(row=2, column=0)

password_label = Label(text="Password:", bg="white")
password_label.grid(row=3, column=0)

# Entries

web_entry = Entry(width=32)
web_entry.grid(row=1, column=1)
web_entry.focus()

email_user_entry = Entry(width=51)
email_user_entry.grid(row=2, column=1, columnspan=2)

# insert method receive 2 parameters, index that is used to place the cursor in the textbox, and the string
email_user_entry.insert(END, string="luisoctaviocs02@gmail.com")

password_entry = Entry(width=32)
password_entry.grid(row=3, column=1)

# Buttons

generate_pwd_button = Button(text="Generate Password", command=generate_pwd)
generate_pwd_button.grid(row=3, column=2)

add_button = Button(text="Add", width=43, command=add)
add_button.grid(row=4, column=1, columnspan=2)

search_button = Button(text="Search", width=15, command=find_pwd)
search_button.grid(row=1, column=2)

window.mainloop()
