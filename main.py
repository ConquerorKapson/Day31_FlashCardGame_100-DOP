from tkinter import *

BACKGROUND = "#B1DDC6"

# ==========================UI================================

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND)

canvas = Canvas(window, width=800, height=526)
front_image = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=front_image)
canvas.create_text(400, 150, text="title", font=("Ariel", 40, "italic"))
canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold italic"))

canvas.config(bg=BACKGROUND, highlightthickness=0)
canvas.grid(row=0, column=0)

right = PhotoImage(file="images/right.png")
tick_button = Button(image=right, highlightthickness=0)
tick_button.grid(row=1, column=0, sticky=E)

wrong = PhotoImage(file="images/wrong.png")
cross_button = Button(image=wrong, highlightthickness=0)
cross_button.grid(row=1, column=0, sticky=W)
canvas.create_image(700, 630, image=wrong)
window.mainloop()
