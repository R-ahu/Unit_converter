import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Unit Converter")
root.geometry("500x500")
root.configure(bg="#f0f0f0")

font_style = ("Arial", 12)

title_label = tk.Label(root, text="Length Unit Converter", font=("Arial", 16, "bold"), fg="#333", bg="#f0f0f0")
title_label.pack(pady=10)

label_input = tk.Label(root, text="Enter the value:", font=font_style, bg="#f0f0f0")
label_input.pack(pady=5)

entry_value = tk.Entry(root, font=font_style, width=20)
entry_value.pack(pady=5)

label_from = tk.Label(root, text="From:", font=font_style, bg="#f0f0f0")
label_from.pack(pady=5)

x = ["kilometers", "hectometers", "meters", "decimeters", "centimeters", "millimeters", "miles"]
combo_from = ttk.Combobox(root, values=x, font=font_style, width=18)
combo_from.pack(pady=5)

label_to = tk.Label(root, text="To:", font=font_style, bg="#f0f0f0")
label_to.pack(pady=5)

combo_to = ttk.Combobox(root, values=x, font=font_style, width=18)
combo_to.pack(pady=5)

result_label = tk.Label(root, text="", font=("Arial", 13, "bold"), fg="blue", bg="#f0f0f0")
result_label.pack(pady=10)

def convert():
    try:
        p = float(entry_value.get())
        q = combo_from.get()
        r = combo_to.get()

        if not q or not r:
            result_label.config(text="Please select both units.")
            return

        to_meters = {
            "kilometers": 1000,
            "hectometers": 100,
            "meters": 1,
            "decimeters": 0.1,
            "centimeters": 0.01,
            "millimeters": 0.001,
            "miles": 1609.34
        }

        value_in_meters = p * to_meters[q]
        result = value_in_meters / to_meters[r]

        result_label.config(text=f"{p} {q} = {round(result, 4)} {r}")

    except ValueError:
        result_label.config(text="Please enter a valid number.")

convert_button = tk.Button(root, text="Convert", command=convert, font=font_style, bg="#007acc", fg="white", padx=10, pady=5)
convert_button.pack(pady=10)

root.mainloop()