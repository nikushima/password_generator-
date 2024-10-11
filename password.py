from tkinter import *
from random import choice
import string


def generate_password(length=28):
    """Generates a password with the given length using letters, digits, and punctuation."""
    characters = string.ascii_letters + string.punctuation + string.digits
    return ''.join(choice(characters) for _ in range(length))


class App:
    def __init__(self):
        self.window = Tk()
        self.window.title('Password Generator')
        self.window.iconbitmap('logo.ico')
        self.window.iconphoto(False, PhotoImage(file='logo.png'))
        self.window.geometry('500x255')
        self.window.config(bg='gray')

        # component creation
        self.create_label()
        self.create_entry()
        self.create_button()

    def create_label(self):
        label_title = Label(self.window, text='Welcome to Password Generator', font=('Courier', 20), bg='gray',
                            fg='black')
        label_title.pack()

    def create_entry(self):
        self.password_entry = Entry(self.window, font=('Courier', 25), bg='white', fg='black', width=30,
                                    relief='solid')
        self.password_entry.pack(pady=50)

    def create_button(self):
        password_generator = Button(self.window, text="Generate Password", font=('Courier', 12), bg='white',
                                    fg='black', width=25, command=self.on_generate_password)
        password_generator.pack()

    def on_generate_password(self):
        password = generate_password()  # Use the external function
        self.password_entry.delete(0, END)
        self.password_entry.insert(0, password)


# Entry point of the application
if __name__ == "__main__":
    app = App()
app.window.mainloop()
