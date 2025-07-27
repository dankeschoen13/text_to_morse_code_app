from customtkinter import *
from encoder import Encoder


FONT1 = ("Courier", 20)
FONT2 = ("Helvetica", 15)
BG = "#8681BD"


# FUNC
encoder = Encoder()

def run_encoding():
    output_area.delete("1.0", "end")
    message = input_area.get('1.0', 'end-1c')
    morse_code = encoder.morsify(message)
    if morse_code:
        output_label.configure(text="Success!")
        output_area.insert('end', morse_code)
    else:
        output_label.configure(text="Please input a message!")
        output_area.insert('end', "🙄")


# USER INTERFACE  ----
app = CTk()
app.title("Morse Code Converter 1.0")
app.minsize(400, 400)
app.config(pady=50, padx=50, background=BG)
app.grid_columnconfigure(0, weight=1)
app.grid_columnconfigure(1, weight=2)
app.grid_columnconfigure(2, weight=1)

# input area label
input_label = CTkLabel(
    app,
    text="Your message:",
    padx=10,
    pady=10,
    font=FONT1,
    bg_color=BG
)
input_label.grid(column=1, row=0, sticky='n')
# input area
input_area = CTkTextbox(
    app,
    width=250,
    height=100
)
input_area.grid(column=1, row=1, sticky='n')


# submit button
submit = CTkButton(
    app,
    text="SUBMIT",
    font=FONT2,
    width=100,
    height=40,
    bg_color=BG,
    fg_color='#471396',
    command=run_encoding
)
submit.grid(column=1, row=3, sticky='s', pady=(15, 15))


# output/results textarea
output_area = CTkTextbox(
    app,
    width=250,
    height=100
)
output_area.grid(column=1, row=4, sticky='n')
# output/feedback_message
output_label = CTkLabel(
    app,
    text="",
    padx=10,
    pady=10,
    font=FONT1,
    bg_color=BG
)
output_label.grid(column=1, row=5, sticky='n')


app.mainloop()