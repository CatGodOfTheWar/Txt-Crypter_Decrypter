from tkinter import *
from tkinter import filedialog as fd

INDEX = 0
data = ""
password = ""
command = ""


def crypt(password_):
    global data
    global INDEX
    final_result = ""
    data = list(data)
    for char in data:
        if (INDEX + 1) == len(password_):
            INDEX = 0
        add = ord(password_[INDEX])
        if (ord(char) + add) < 256:
            result = ord(char) + add
        else:
            result = ((ord(char) + add) % 255)
        final_result += chr(result)
        with open("New_Data.txt", "a") as new_data:
            new_data.write(chr(result))
    print(final_result)


def decrypt(password_):
    global data
    global INDEX
    final_result = ""
    data = list(data)
    for char in data:
        if (INDEX + 1) == len(password_):
            INDEX = 0
        add = ord(password_[INDEX])
        result = ord(char) - add
        final_result += chr(result)
        with open("New_Data.txt", "a") as new_data:
            new_data.write(chr(result))
    print(final_result)


def select_file():
    global data
    filetypes = (('text file', '.txt'),
                 ('All files', '*.*')
                 )

    content = fd.askopenfile(
        title='Open files',
        initialdir='/',
        filetypes=filetypes
    )
    data = content.read()


def submit():
    global password
    global command
    password = password_user.get()
    command = command_user.get().lower()
    main()


def main():
    global password
    global command
    with open("New_Data.txt", "w+") as _:
        pass
    if command == "crypt":
        crypt(password)
    else:
        decrypt(password)


if __name__ == '__main__':
    window = Tk()
    window.title('Crypter/Decrypter')
    window.resizable(False, False)
    window.geometry("600x600")
    window.config(bg='#696880')

    password_user = StringVar()
    command_user = StringVar()

    open_btn = Button(window, text="Choose the file!",
                      command=select_file,
                      font=('Times New Roman', 25),
                      borderwidth=0,
                      border=0,
                      bg='#7c6e7f',
                      fg='#322d31',
                      activebackground='#adadc9',
                      activeforeground='#322d31')
    open_btn.place(x=130, y=80)

    enter_frame = Frame(window,
                        padx=10,
                        pady=10,
                        bg='#7f7d9c')
    enter_frame.place(x=15, y=200)

    password_label = Label(enter_frame,
                           text="Password:",
                           font=('Times New Roman', 15),
                           bg='#7f7d9c',
                           fg='#322d31')
    password_label.grid(row=0, column=0)

    space_label = Label(enter_frame, bg='#7f7d9c')
    space_label.grid(row=1, column=0)

    command_label = Label(enter_frame,
                          text="Command:",
                          font=('Times New Roman', 15),
                          bg='#7f7d9c',
                          fg='#322d31')
    command_label.grid(row=2, column=0)

    password_entry = Entry(enter_frame,
                           width=20,
                           font=('Times New Roman', 20),
                           bg='#c5c6d0',
                           textvariable=password_user)
    password_entry.grid(row=0, column=1)

    command_entry = Entry(enter_frame,
                          width=20,
                          font=('Times New Roman', 20),
                          bg='#c5c6d0',
                          textvariable=command_user)
    command_entry.grid(row=2, column=1)

    enter_frame.config(highlightbackground='#adadc9',
                       highlightthickness=5,
                       highlightcolor='#adadc9'
                       )

    submit_btn = Button(window, text="Apply!",
                        font=('Times New Roman', 20),
                        borderwidth=0,
                        border=0,
                        bg='#7c6e7f',
                        fg='#322d31',
                        activebackground='#adadc9',
                        activeforeground='#322d31',
                        command=submit)
    submit_btn.place(x=225, y=400)

    window.mainloop()
