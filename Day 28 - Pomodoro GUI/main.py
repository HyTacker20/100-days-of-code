from tkinter import *

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
checkmarks_count = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(canvas_text, text="00:00")
    label.config(text="Timer", fg=GREEN)

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    global checkmarks_count

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    reps += 1

    checkmark.config(text="✔" * checkmarks_count)

    if reps % 8 == 0:
        # count_down(long_break_sec)
        label.config(text="Break", fg=RED)
        checkmarks_count = 0
        count_down(7)
    elif reps % 2 == 0:
        # count_down(short_break_sec)
        label.config(text="Break", fg=PINK)
        count_down(3)
    else:
        # count_down(work_sec)
        label.config(text="Work", fg=GREEN)
        count_down(5)
        checkmarks_count += 1


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global timer
    count_min = count // 60
    count_sec = count % 60
    canvas.itemconfig(canvas_text, text=f"{count_min}:{count_sec if count_sec >= 10 else "0" + str(count_sec)}")
    if count >= 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=223, bg=YELLOW, highlightthickness=0)
bg_image = PhotoImage(file="tomato.png")
canvas.create_image(101, 112, image=bg_image)
canvas_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=2, row=2)

label = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 35, "bold"), bg=YELLOW)
label.grid(column=2, row=1)

start_button = Button(text="Start", command=start_timer)
start_button.grid(column=1, row=3)

reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(column=3, row=3)

checkmark = Label(text="", fg=GREEN, font=(FONT_NAME, 15, "bold"), bg=YELLOW)
checkmark.grid(column=2, row=4)

window.mainloop()
