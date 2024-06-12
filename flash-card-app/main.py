from tkinter import *
from tkinter import messagebox

import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"

# ------------------------ Change Card -------------------------
# Load the data
try:
    data = pd.read_csv("./data/words_to_learn.csv")

except FileNotFoundError:
    messagebox.showerror("Message", "Words to learn file not found! Starting new learning!")
    data = pd.read_csv("./data/french_words.csv")

words_to_learn = data.to_dict(orient="records")
current_card = {}


def next_card():
    global current_card, flip_timer
    if words_to_learn:
        window.after_cancel(flip_timer)
        current_card = random.choice(words_to_learn)
        canvas.itemconfig(word_text, fill="black", text=current_card["French"])
        canvas.itemconfig(title_text, fill="black", text="French")
        canvas.itemconfig(card_background, image=card_french_png)
        flip_timer = window.after(3000, reveal_english_card)
    else:
        messagebox.showinfo("Info", "No more words to learn!")
        window.destroy()


def reveal_english_card():
    canvas.itemconfig(card_background, image=card_english_png)
    canvas.itemconfig(word_text, fill="white", text=current_card["English"])
    canvas.itemconfig(title_text, fill="white", text="English")


def known_card():
    words_to_learn.remove(current_card)
    update_data = pd.DataFrame(words_to_learn)
    update_data.to_csv("./data/words_to_learn.csv", index=False)
    next_card()


# ------------------------ Set Up Screen -------------------------
window = Tk()
window.title("Flashy")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)


flip_timer = window.after(3000, reveal_english_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_french_png = PhotoImage(file="./images/card_front.png")
card_english_png = PhotoImage(file="./images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_french_png)

title_text = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 300, text="", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

cross_btn_png = PhotoImage(file="./images/wrong.png")
unknown_btn = Button(image=cross_btn_png, bg=BACKGROUND_COLOR, padx=50, highlightthickness=0, command=next_card)
unknown_btn.grid(row=1, column=0)

check_btn_png = PhotoImage(file="./images/right.png")
known_btn = Button(image=check_btn_png, bg=BACKGROUND_COLOR, padx=50, highlightthickness=0, command=known_card)
known_btn.grid(row=1, column=1)

next_card()

window.mainloop()
