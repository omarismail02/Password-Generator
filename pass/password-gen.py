from tkinter import *
from tkinter import messagebox
import csv
import tkinter
import string
import random


def generate():
    # Define the length and character set for your password
    password_length = 15  # You can change this to your desired length
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate the password
    password = ''.join(random.choice(characters) for _ in range(password_length))

    # Set the password_entry to read-only
    password_entry.config(state="normal")

    # Update the password_entry field with the generated password
    password_entry.delete(0, tkinter.END)  # Clear any existing text
    password_entry.insert(0, password)  # Insert the generated password

    # Set the password_entry back to read-only

def add():
    website = Website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if website and email and password:  # Check if all fields are not empty
        with open('passwords.csv', 'a', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow([website, email, password])
        Website_entry.delete(0, tkinter.END)
        email_entry.delete(0, tkinter.END)
        password_entry.delete(0, tkinter.END)
    else:
        messagebox.showerror("Error", "All fields must be filled to add to the CSV.")

# Create the graphic user interface
window = Tk()

#import the image from the same folder of project
image = tkinter.PhotoImage(file='password.png')


image_label = Label(window, image=image,
                            width=500,
                            height=350)
image_label.grid(row=0, column=0, columnspan=3, padx=200, pady=40)
window.geometry("1000x1000")
window.title("Password Generator")
Website_label = Label(window, text="Website :",
                              font=("Arial", 12,'bold')).grid(column=0, row=1,pady=10)
Website_entry = Entry(window,width='80',
                             foreground="black",
                             borderwidth=2,
                             relief="groove")
Website_entry.grid(column=1, row=1,pady=10)
password_label = Label(window, text="Password :",
                               font=("Arial", 12,'bold')).grid(column=0, row=2,pady=10)
password_entry = Entry(window,width='80',
                              foreground="black",
                              borderwidth=2,
                              relief="groove")
password_entry.grid(column=1, row=2,pady=10)
generate_button = Button(window, text="Generate",
                                 width=15,
                                 bg='#FFD43B',
                                 font=("Verdana",8,'bold'),
                                 activebackground='#306998',
                                 command=generate).grid(column=2, row=2,pady=10)
email_label = Label(window, text="E-Mail!",
                            font=("Arial", 12,'bold')).grid(column=0, row=3,pady=10)
email_entry = Entry(window,width='80',
                           foreground="black",
                           borderwidth=2,
                           relief="groove")
email_entry.grid(column=1, row=3,pady=10)
add_button = Button(window, text="Add",
                            bg='#306998',
                            width='60',
                            font=("Verdana", 12,'bold'),
                            activebackground='#FFD43B',
                            command=add)
add_button.grid(row=4,column =0,columnspan=4,pady=40)

window.mainloop()
