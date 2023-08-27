from tkinter import *
from tkinter import messagebox
import pandas as pd
import random
from PIL import Image , ImageTk
import csv

BACKGROUND_COLOR = "#B1DDC6"

# --------------------------- CSV file setup -----------------------------------------------------------------------------
to_learn = {}
try:
    data_frame = pd.read_csv('data/words_to_learn.csv')
except FileNotFoundError:
    original_data = pd.read_csv('data/english_hindi.csv')
    to_learn = original_data.to_dict(orient='records')
else:
    to_learn = data_frame.to_dict(orient='records')

current_card = {}

# get random word card
def get_card():
    global current_card
    global flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(title_card_id , text="English" , fill="black")
    canvas.itemconfig(card_word_id , text=current_card['English'] , fill="black")
    canvas.itemconfig(card_background , image=front_img)
    flip_timer = window.after(3000 , func=flip_card)


# if tick is pressed
def is_known():
    to_learn.remove(current_card)
    data = pd.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv" , index=False)
    get_card()
    
def flip_card():
    canvas.itemconfig(title_card_id , text="Hindi" , fill="white")
    canvas.itemconfig(card_word_id , text=current_card['Hindi'] , fill="white")
    canvas.itemconfig(card_background , image=card_back_img)


# --------------------------- UI DESIGN --------------------------------------------------------------------------------------------

window = Tk()
window.title("Flash Cards")
window.config(padx=20 , pady=20 , bg=BACKGROUND_COLOR)
flip_timer = window.after(3000 , func=flip_card)

canvas = Canvas(height=526 , width=800)
front_img = PhotoImage(file='images/card_front.png')
card_back_img = PhotoImage(file='images/card_back.png')
card_background = canvas.create_image(400 , 263 , image=front_img)
title_card_id = canvas.create_text(400 , 150 ,text="Title" , font=("Ariel" , 20 , "italic"))
card_word_id = canvas.create_text(400 , 263 ,text="word" , font=("Ariel" , 40 , "bold"))
canvas.config(bg=BACKGROUND_COLOR , highlightthickness=0)
canvas.grid(row=0 , column=0 , columnspan=2)

#Buttons
cross_img = PhotoImage(file="images/wrong.png")
unknown_btn = Button(image=cross_img , highlightthickness=0 , command=get_card)
unknown_btn.grid(row=1 , column=0)

check_img = PhotoImage(file="images/right.png")
known_btn = Button(image=check_img , highlightthickness=0 , command=is_known)
known_btn.grid(row=1 , column=1)

get_card()

mainloop()
