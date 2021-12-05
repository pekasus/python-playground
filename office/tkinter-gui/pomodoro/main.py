import tkinter as tk
import time
import math
from playsound import playsound

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
work_call = False
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    check_marks.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    global work_call
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 2 == 1:
        countdown(work_sec)
        title_label.config(text="Work", fg=GREEN)
        if work_call:
            playsound("sound/rabota.mp3")
            work_call = False
        else:
            playsound("sound/back2work.mp3")
            work_call = True

    elif reps % 8 == 0:
        countdown(long_break_sec)
        title_label.config(text="Break", fg=RED)
        playsound("sound/long_break.mp3")
        reps = 0
    else:
        countdown(short_break_sec)
        title_label.config(text="Break", fg=PINK)
        playsound("sound/short_break.mp3")


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def countdown(count):
    global timer
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        marks = ""
        for _ in range(math.floor(reps/2)):
            marks += "✅"
        check_marks.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# window.after(1000, func=, )

title_label = tk.Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
title_label.grid(column=1, row=0)

canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
image_file = tk.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=image_file)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
# canvas.pack()
canvas.grid(column=1, row=1)

start_button = tk.Button(text="Start", fg=YELLOW, highlightthickness=0, bd=0, borderwidth=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = tk.Button(text="Reset", fg=YELLOW, highlightthickness=0, bd=0, command=reset_timer)
reset_button.grid(column=3, row=2)

check_marks = tk.Label(text="", fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)

window.mainloop()