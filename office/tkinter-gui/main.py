import tkinter

window = tkinter.Tk()
window.title("GUI Program")
window.minsize(width=500, height=300)

# Label

my_label = tkinter.Label(text="This is a label", font=("Arial", 24, "bold"))
my_label.pack()




window.mainloop()