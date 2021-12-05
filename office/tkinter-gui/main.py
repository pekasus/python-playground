import tkinter as tk

window = tk.Tk()
window.title("GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Label

my_label = tk.Label(text="This is a label", font=("Arial", 24, "bold"))
# my_label.pack(side="left")
# my_label.place(x=100, y=200)
my_label.grid(column=0, row=0) # can't use grid and pack

my_label["text"] = "New Label"
my_label.config(text="New Label")

# Button

def button_clicked():
    print("I got clicked.")
#    my_label["text"] = "Button got clicked."
    new_text = input.get()
    my_label["text"] = new_text

button1 = tk.Button(text="Show")
button1.grid(column=2, row=0)

button2 = tk.Button(text="Click Me", command=button_clicked)
# button2.pack()
button2.grid(column=1, row=1)

# Entry

input = tk.Entry(width=10)
# input.pack()
input.grid(column=3, row=2)



window.mainloop()