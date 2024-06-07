from tkinter import *
from tkinter import messagebox
import secrets
import pyperclip
import json

window = Tk()
window.title("Password Manager")
window.config(pady=40, padx=40, bg="white")


# ------------------------ Generate Password -------------------------
def random_passwd():
    passwd_len = 8
    secret_passwd = secrets.token_urlsafe(passwd_len)
    if len(passwd_entry.get()) > 0:
        passwd_entry.delete(0, END)

    passwd_entry.insert(END, string=f"{secret_passwd}")
    pyperclip.copy(secret_passwd)


# ------------------------ Save Password -------------------------
def save():
    new_data = {
        website_entry.get(): {
            "email": username_entry.get(),
            "password": passwd_entry.get()
        }
    }

    if len(website_entry.get()) == 0 or len(passwd_entry.get()) == 0:
        messagebox.showinfo(title="Opps!", message="Please don't leave empty fields!")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)

            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            website_entry.focus()
            passwd_entry.delete(0, END)


# ------------------------ Find Password -------------------------
def find_password():
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found!")
    else:
        if website_entry.get() in data:
            email = data[website_entry.get()]["email"]
            passwd = data[website_entry.get()]["password"]
            messagebox.showinfo(title=website_entry.get(),
                                message=f"Email: {email}\n"
                                        f"Password: {passwd}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website_entry.get()} exists.")


# Set Up Screen

canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:", bg="white")
website_label.grid(row=1, column=0)

website_entry = Entry(width=23)
website_entry.grid(row=1, column=1, padx=2, pady=2)
website_entry.focus()

search_btn = Button(text="Search", width=15, bg="white", padx=2, pady=2, command=find_password)
search_btn.grid(row=1, column=2)

username_label = Label(text="Email/Username:", bg="white")
username_label.grid(row=2, column=0)

username_entry = Entry(width=40)
username_entry.grid(row=2, column=1, columnspan=2, padx=2, pady=2)
username_entry.insert(0, "test@gmail.com")

passwd_label = Label(text="Password:", bg="white")
passwd_label.grid(row=3, column=0)

passwd_entry = Entry(width=23)
passwd_entry.grid(row=3, column=1, padx=2, pady=2)

generate_passwd_btn = Button(text="Generate Password", width=13, bg="white", command=random_passwd)
generate_passwd_btn.grid(row=3, column=2, padx=2, pady=2)

add_btn = Button(text="Add", width=38, bg="white", command=save)
add_btn.grid(row=4, column=1, columnspan=2)

window.mainloop()
