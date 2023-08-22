import tkinter as tk
from tkinter import ttk


answers = []
labels_list = []

root = tk.Tk()
root.geometry("200x250")
root.title("Freedom Unit Converter")


def clear_answers():
    for label in labels_list:
        label.destroy()


def on_menu_select(event):
    selected_item = menu_var.get()
    status_label.config(text=f"Converting: {selected_item}")


def get_input():
    entered_text = entry.get()
    if menu_var.get() == "miles":
        miles2kilo(entered_text)
    elif menu_var.get() == "inches":
        inch2cm(entered_text)
    elif menu_var.get() == "feet":
        feet2mtr(entered_text)
    elif menu_var.get() == "gallons":
        gallon2liter(entered_text)


menu_var = tk.StringVar()
status_label = tk.Label(root, text="which unit would you like to convert?", pady=10)
status_label.pack()


menu = ttk.Combobox(
    root, textvariable=menu_var, values=["miles", "inches", "feet", "gallons"]
)
menu.pack()
menu.bind("<<ComboboxSelected>>", on_menu_select)

entry = tk.Entry(root)
entry.pack()
get_input_button = tk.Button(root, text="CONVERT!", command=get_input)
get_input_button.pack()


def miles2kilo(userinput):
    converted = float(userinput) * 1.60934
    answers.append(converted)
    clear_answers()
    converted_label = tk.Label(root, text=answers[-1], pady=10)
    labels_list.append(converted_label)
    labels_list[-1].pack()


def inch2cm(userinput):
    converted = float(userinput) * 2.54
    answers.append(converted)
    clear_answers()
    converted_label = tk.Label(root, text=answers[-1], pady=10)
    labels_list.append(converted_label)
    labels_list[-1].pack()


def feet2mtr(userinput):
    converted = float(userinput) / 3.281
    answers.append(converted)
    clear_answers()
    converted_label = tk.Label(root, text=answers[-1], pady=10)
    labels_list.append(converted_label)
    labels_list[-1].pack()


def gallon2liter(userinput):
    converted = float(userinput) * 3.785
    answers.append(converted)
    clear_answers()
    converted_label = tk.Label(root, text=answers[-1], pady=10)
    labels_list.append(converted_label)
    labels_list[-1].pack()


"""funcdict = {
    'miles': [miles2kilo, "Kilometers"],
    'inch': [inch2cm, "Centimeters"],
    'feet': [feet2mtr,"Meters"],
    'gallon' : [gallon2liter,"Liters"],
}"""


root.mainloop()
