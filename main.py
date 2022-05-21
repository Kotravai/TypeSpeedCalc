from time import perf_counter as timer
from tkinter import *


def game():

    windows = Tk()
    windows.title("Type speed Tester")
    windows.minsize(width=600, height=350)
    windows.config(padx=40, pady=20)

    def speed_calc():
        error = 0
        type_input = user_input.get("1.0", "end-1c")
        actual = str(prompt).split()
        user_in = str(type_input).split()
        for i in range(len(user_in)):
            if actual[i] == user_in[i]:
                continue
            else:
                error += 1
        end = timer()
        word_count = len(user_in) - error
        time = end-start
        type_speed = round(word_count / (time/60), 0)
        return error_out.insert(END, str(error)), wpm_out.insert(END, f"{type_speed} wpm")


    prompt = "Pirates are evil? The Marines are righteous? These terms have always changed throughout the course of history!" \
             " Kids who have never seen peace and kids who have never seen war have different values! Those who stand at the" \
             " top determine what's wrong and what's right! This very place is neutral ground! Justice will prevail, you say?" \
             " But of course it will! Whoever wins becomes justice!"

    start = timer()

    title = Label(text="Check your Typing Speed!!", font=("verdana", 20, "bold"))
    title.config(pady=20, padx=30)
    title.grid(row=0, column=0, columnspan=6)

    actual_text = Text(windows, width=60, height=8, pady=10, padx=10, font=("verdana", 14) )
    actual_text.insert(END, prompt)
    actual_text.grid(row=2, columnspan=6, column=0)

    user_label = Label(text="Type the above text: ", font=("sanserif", 16, "bold"))
    user_label.config(pady=10, padx=10)
    user_label.grid(row=3, column=0)

    user_input = Text(windows, width=60, height=8, pady=10, padx=10, bg='white', fg='black', font=("verdana", 14))
    user_input.grid(row=4, columnspan=6, column=0)

    check_button = Button(text="Check", fg='green', command=speed_calc, font=("arial", 12, 'bold'))
    check_button.config(padx=8, pady=8)
    check_button.grid(row=5, column=1)

    reset_button = Button(text="Reset", fg='green', command=game, font=("arial", 12, 'bold'))
    reset_button.config(padx=8, pady=8)
    reset_button.grid(row=5, column=2)

    results = Label(text="Results", font=("sanserif", 15, "bold"))
    results.config(padx=10, pady=10)
    results.grid(row=6, column=0)

    error_label = Label(text="Number of errors", font=("sanserif", 13, "bold"))
    error_label.config(padx=0, pady=10)
    error_label.grid(row=7, column=0)

    error_out = Text(windows, width=10, pady=5, padx=10, height=3, bg='grey', fg='blue')
    error_out.grid(row=7, column=1)

    wpm_label = Label(text="Typing speed:", font=("sanserif", 13, "bold"))
    wpm_label.config(padx=10, pady=10)
    wpm_label.grid(row=7, column=2)

    wpm_out = Text(windows, width=10, height=3, pady=5, padx=10, bg='grey', fg='blue')
    wpm_out.grid(row=7, column=3)

    windows.mainloop()


game()
