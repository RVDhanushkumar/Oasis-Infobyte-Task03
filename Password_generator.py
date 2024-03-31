import random
import string
import tkinter as tk
from tkinter import messagebox


def check():
    if var1.get() == 0 and var2.get() == 0 and var3.get() == 0:
        tk.messagebox.showwarning("Missing","At least one option must be selected!!")
        return ""
    click()


def click():

    password = []
    x = 0
    if var1.get() == 1 and var2.get() == 1 and var3.get() == 1:
        character = string.ascii_letters + string.punctuation + string.digits
        while x != int(length.get()):
            password.append(random.choice(character))
            x += 1
    elif var1.get() == 0 and var2.get() == 0 and var3.get == 1:
        character = string.ascii_letters
        while x != int(length.get()):
            password.append(random.choice(character))
            x += 1
    elif var1.get() == 0 and var2.get() == 1 and var3.get() == 0:
        character = string.digits
        while x != int(length.get()):
            password.append(random.choice(character))
            x += 1
    elif var1.get() == 0 and var2.get() == 1 and var3.get() == 1:
        character = string.ascii_letters + string.digits
        while x != int(length.get()):
            password.append(random.choice(character))
            x += 1
    elif var1.get() == 1 and var2.get() == 0 and var3.get() == 0:
        character = string.punctuation
        while x != int(length.get()):
            password.append(random.choice(character))
            x += 1
    elif var1.get() == 1 and var2.get() == 0 and var3.get() == 1:
        character = string.ascii_letters + string.punctuation
        while x != int(length.get()):
            password.append(random.choice(character))
            x += 1
    elif var1.get() == 1 and var2.get() == 1 and var3.get() == 0:
        character = string.punctuation + string.digits
        while x != int(length.get()):
            password.append(random.choice(character))
            x += 1
    password = "".join(password)
    c1.destroy()
    c2.destroy()
    c3.destroy()
    l1.config(text=f"Your New Password:\n\n {password}",fg="Green")
    l1.pack(pady=20)
    l2.destroy()
    length.destroy()
    l2.destroy()
    sp.destroy()


if __name__ == "__main__":
    window = tk.Tk()
    window.title("Password Generator🔑🔐")

    l1 = tk.Label(window,text="Welcome to Password generator:",fg="Blue",font='18')
    l1.pack(pady=20)

    f1 = tk.Frame(window)
    f1.pack(pady=20)

    l2 = tk.Label(f1, text="Enter length of Password: ")
    l2.pack(side=tk.LEFT)

    length = tk.Entry(f1, width=20)
    length.pack(side=tk.LEFT, padx=10)

    var1 = tk.IntVar()
    var2 = tk.IntVar()
    var3 = tk.IntVar()
    c3 = tk.Checkbutton(window, text="Character", variable=var3, onvalue=1, offvalue=0)
    c3.pack(pady=0)

    c1 = tk.Checkbutton(window,text="Special_Character",variable=var1,onvalue=1,offvalue=0)
    c1.pack(pady=00)

    c2 = tk.Checkbutton(window, text="Numbers", variable=var2, onvalue=1, offvalue=0)
    c2.pack(pady=0)

    sp = tk.Button(window, text="Submit",command=check)
    sp.pack(pady=10)
    window.geometry('500x300')
    window.mainloop()
