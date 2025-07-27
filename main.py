from customtkinter import *
from encoder import Encoder

FONT = ("Courier", 20)
SOUR = "#8681BD"

app_engine = Encoder()

app = CTk()
app.title("Morse Code Converter 1.0")
app.minsize(400, 400)
app.config(pady=50, padx=50, background=SOUR)
app.grid_columnconfigure(0, weight=1)
app.grid_columnconfigure(1, weight=2)
app.grid_columnconfigure(2, weight=1)

# TEXT AREA LABEL
textarea_label = CTkLabel(
    app,
    text="Your message:",
    padx=10,
    pady=10,
    font=FONT,
    bg_color=SOUR
)
textarea_label.grid(column=1, row=0, sticky='n')

# TEXT AREA
textarea = CTkTextbox(
    app,
    width=250,
    height=100
)
textarea.grid(column=1, row=1, sticky='n')

# SUBMIT BUTTON
submit = CTkButton(
    app,
    text="SUBMIT",
    font=FONT,
    width=100,
    height=40,
    bg_color=SOUR,
    fg_color='#471396',
)
submit.grid(column=1, row=3, sticky='s', pady=(10, 10))

# RESULT BOX LABEL
result_label = CTkLabel(
    app,
    text="",
    padx=10,
    pady=10,
    font=FONT,
    bg_color=SOUR
)
result_label.grid(column=1, row=4, sticky='n')

# RESULT BOX
textarea = CTkTextbox(
    app,
    width=250,
    height=100
)
textarea.grid(column=1, row=5, sticky='n')

app.mainloop()