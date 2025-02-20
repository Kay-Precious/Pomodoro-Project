from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
timer = None
reps = 0
# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    '''Resets timer'''
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text='00:00')
    timer_label.config(text='TIMER', fg=GREEN)
    mark_label.config(text="")
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    '''Starts Timer'''
    global reps
    reps += 1

    work_min = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60

    if reps % 2 == 1:
        timer_count(work_min)
        timer_label.config(text="WORK", fg=GREEN)

    elif reps == 8:
        timer_count(long_break)
        timer_label.config(text="BREAK", fg=RED)

    else:
        timer_count(short_break)
        timer_label.config(text="BREAK", fg=PINK)

    if reps == 9:
        window.after_cancel(timer)
        canvas.itemconfig(timer_text, text='00:00')
        timer_label.config(text='TIMER', fg=GREEN)
        mark_label.config(text="")
        reps = 0

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def timer_count(count):
    '''Timer Countdown'''
    global reps
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_min <= 9:
        count_min = f"0{count_min}"
    if count_sec <= 9:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec}')
    if count > 0:
        global timer
        timer = window.after(1000, timer_count, count - 1)
    else:
        start_timer()
        mark = ''
        sessions = int(reps/2)
        for r in range(sessions):
            mark += '✔'
        mark_label.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('POMODORO')
window.minsize(300, 323)
window.config(padx=100, pady=50, bg=YELLOW)


canvas = Canvas(bg=YELLOW, highlightthickness=0)
img = PhotoImage(file='./tomato.png')
canvas.create_image(180, 100, image=img)
timer_text = canvas.create_text(
    180, 130, text='00:00', font=(FONT_NAME, 35, 'bold'), fill='green')
canvas.grid(column=1, row=1)

# Labels

timer_label = Label(text='TIMER', font=(
    FONT_NAME, 50, 'normal'), fg=GREEN, bg=YELLOW)
timer_label.grid(column=1, row=0)

mark_label = Label(fg=GREEN, bg=YELLOW, font=('Arial', 16, 'bold'))
mark_label.grid(column=1, row=3)

# Buttons
start_button = Button(text='Start', highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text='Reset', highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)


window.mainloop()
