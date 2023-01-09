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
reps = 0
check_mark = 1
timer=None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():


    window.after_cancel(timer)
    time_label.config(text="Timer", font=(FONT_NAME, 36, "bold"), bg=YELLOW, fg=GREEN)
    canvas.itemconfig(timer_text, text=f"00:00")
    global check_mark
    check_mark = 0
    global reps
    reps = 0
    check_marks.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- #


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def start_timer():

    global reps
    short_break = SHORT_BREAK_MIN*60
    long_break = LONG_BREAK_MIN*60
    work = WORK_MIN*60
    reps += 1
    if reps == 8:
        count_down(long_break)
        time_label["text"] = "Break"
    elif reps % 2 == 0:
        count_down(short_break)
        time_label["text"] = "Break"
    else:
        count_down(work)
        time_label["text"] = "Work"



    return reps


def count_down(count):
    global check_mark
    count_min = math.floor(count / 60)
    count_seconds = count % 60
    if count_seconds == 0:
        count_seconds = "00"
    elif count_seconds < 10:
        count_seconds = f"0{count_seconds}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        if reps % 2 == 0:
            check_marks.config(text="✓"*check_mark, bg=YELLOW, fg=GREEN, font=(FONT_NAME, 15, "bold"))
            check_mark += 1
        start_timer()



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 110, image=tomato_img) # x-value, y-value, PhotoImage variable
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

time_label = Label(text="Timer", font=(FONT_NAME, 36, "bold"), bg=YELLOW, fg=GREEN)
time_label.grid(column=1, row=0)

start_button = Button(text="Start", bg="white", command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", bg="white", command=reset_timer)
reset_button.grid(column=3, row=2)

check_marks = Label()
check_marks.grid(column=1, row=4)




















window.mainloop()