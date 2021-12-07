import tkinter as tk
import random
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Ariel"

try:
    data = pd.read_csv("data/russian_words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("data/russian_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

current_card = {}

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(canvas_image, image=card_front_image)
    canvas.itemconfig(russian_text, text="Russian", fill="black")
    canvas.itemconfig(word_text, text=current_card["Russian"], fill="black")
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(canvas_image, image=card_back_image)
    canvas.itemconfig(russian_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=current_card["English"], fill="white")

def remove_word():
    global current_card, to_learn
    to_learn.remove(current_card)
    df = pd.DataFrame(to_learn)
    df.to_csv("data/russian_words_to_learn.csv", index=False)
    next_card()

window = tk.Tk()
window.title("Russian Flash")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = tk.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_image = tk.PhotoImage(file="images/card_front.png")
card_back_image = tk.PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=card_front_image)
canvas.grid(column=0, row=0, columnspan=2)
russian_text = canvas.create_text(400, 150, text="Russian", fill="black", font=(FONT_NAME, 40, "italic"))
word_text = canvas.create_text(400, 263, text="word", fill="black", font=(FONT_NAME, 60, "bold"))

no_button_image = tk.PhotoImage(file="images/wrong.png")
no_button = tk.Button(image=no_button_image, command= next_card, highlightthickness=0, bd=0, highlightbackground = BACKGROUND_COLOR)
no_button.grid(column=0, row=1)

yes_button_image = tk.PhotoImage(file="images/right.png")
yes_button = tk.Button(image=yes_button_image, command= remove_word, highlightthickness=0, bd=0, highlightbackground = BACKGROUND_COLOR)
yes_button.grid(column=1, row=1)

next_card()

window.mainloop()