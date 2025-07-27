import pandas as pd
from customtkinter import *

FONT = ("Arial", 20)
SOUR = "#8681BD"

data = pd.read_csv('code.csv', header=None, names=['char', 'code'])
print(data)

app = CTk()
app.title("Morse Code Converter 1.0")
app.minsize(400, 400)
app.config(pady=50, padx=50, background=SOUR)

app.grid_columnconfigure(0, weight=1)
app.grid_columnconfigure(1, weight=2)
app.grid_columnconfigure(2, weight=1)

textarea_label = CTkLabel(
    app,
    text="Enter your message here:",
    padx=10,
    pady=10,
    font=FONT,
    bg=SOUR
)
textarea_label.grid(column=1, row=0, sticky='n')

textarea = CTkTextbox(
    app,
    width=30,
    height=10
)
textarea.grid(column=1, row=1, sticky='n')

submit = CTkButton(
    app,
    text="Enter",
    font=FONT,
    width=5,
)
submit.grid(column=1, row=3, sticky='s')

app.mainloop()