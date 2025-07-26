import pandas as pd
from tkinter import *

FONT = ("Arial", 20)
SOUR = "#8681BD"

data = pd.read_csv('code.csv', header=None, names=['char', 'code'])
print(data)

window = Tk()
window.title("Morse Code Converter 1.0")
window.minsize(400, 400)
window.config(pady=50, padx=50, background=SOUR)

window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=2)
window.grid_columnconfigure(2, weight=1)

textarea_label = Label(
    window,
    text="Enter your message here:",
    padx=10,
    pady=10,
    font=FONT,
    bg=SOUR
)
textarea_label.grid(column=1, row=0, sticky='n')

textarea = Text(
    window,
    width=30,
    height=10
)
textarea.grid(column=1, row=1, sticky='n')

submit = Button(
    window,
    text="Enter",
    font=FONT,
    width=5,
)
submit.grid(column=1, row=3, sticky='s')

window.mainloop()