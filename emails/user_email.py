import csv
from tkinter import Tk, Canvas, Label, Entry, Button, messagebox


def save_email():
    # Retrieve the text from the entry fields
    names = name_entry.get().title()  # Capitalize the name
    emails = email_entry.get()

    # Check if either field is empty
    if not names or not emails:
        messagebox.showinfo(title='Error', message="Please fill in both fields.")

    # Save the name and email to the CSV file
    else:
        # try and incorporate sheety api with this to make it be more lasting
        with open('emails.csv', mode='a', newline='') as data:
            writer = csv.writer(data)
            writer.writerow([names, emails])

        # Clear the entry fields after saving
        name_entry.delete(0, 'end')
        email_entry.delete(0, 'end')

        # Print a confirmation message
        messagebox.showinfo(title='Error', message=f"Saved: {names}, {emails}")


window = Tk()
window.title('Pass Manager')
window.config(padx=70, pady=70, width=200, height=200)

canvas = Canvas(width=200, height=200, highlightthickness=0)

name = Label(text='Name: ', font=('Arial', 10, 'bold'), padx=5, pady=5)
name.grid(column=0, row=1)

email = Label(text='Email: ', font=('Arial', 10, 'bold'), padx=5, pady=5)
email.grid(column=0, row=2)

name_entry = Entry(width=50)
name_entry.grid(column=1, row=1)
name_entry.focus()

email_entry = Entry(width=50)
email_entry.grid(column=1, row=2, columnspan=2)

add_button = Button(text='Add', width=43, command=save_email, padx=2, pady=2)
add_button.grid(column=1, row=5, columnspan=2)

window.mainloop()
