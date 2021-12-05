import tkinter as tk

window = tk.Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=150)
window.config(padx=20, pady=20)

input = tk.Entry(width=10)
input.grid(column=1, row=0)

miles_label = tk.Label(text="Miles", font=("Arial", 14, "bold"))
miles_label.grid(column=2, row=0)

equal_label = tk.Label(text="is equal to", font=("Arial", 14, "bold"))
equal_label.grid(column=0, row=1)

km_label = tk.Label(text="Km", font=("Arial", 14, "bold"))
km_label.grid(column=2, row=1)

result_label = tk.Label(text="0", font=("Arial", 14, "bold"))
result_label.grid(column=1, row=1)

def calculate():
    result_label["text"] = float(input.get()) * 1.6

button2 = tk.Button(text="Calculate", command=calculate)
button2.grid(column=1, row=2)


window.mainloop()