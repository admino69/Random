from tkinter import *
import customtkinter

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

root = customtkinter.CTk()

root.title("Practical App")

root.resizable(False, False)

height = 400
width = 550
x = (root.winfo_screenwidth()//2)-(width//3)
y = (root.winfo_screenheight()//2)-(height//2)
root.geometry('{}x{}+{}+{}'.format(width, height, x, y))
#root.geometry("400x400")

def submit():
    my_label.configure(text=f"Hello {my_entry.get()}")
    my_entry.configure(state=DISABLED)

def clear():
    my_entry.delete(0, END)
    my_entry.configure(state=NORMAL)

my_label = customtkinter.CTkLabel(root, text="")
my_label.pack(pady=40)

creat_name_label = customtkinter.CTkLabel(root,
     text="Created By Adam",
     font=("",12))
creat_name_label.place(x=15,y=5)

my_entry = customtkinter.CTkEntry(root, 
    placeholder_text="Enter Your Name",
    height=50,
    width=200,
    font=("",18),
    corner_radius=50,
    fg_color=("","black"))
my_entry.pack(pady=20)

my_button = customtkinter.CTkButton(root, text="Submit", command=submit)
my_button.pack(pady=10)

clear_button = customtkinter.CTkButton(root, text="Clear", command=clear)
clear_button.pack(pady=10)

root.mainloop()