from customtkinter import *
from encoder import Encoder


FONT1 = ("Courier", 20)
FONT2 = ("Helvetica", 15)
BG = "#1E201E"


# FUNC
encoder = Encoder()

def run_encoding():
    encode_output.delete("1.0", "end")
    message = encode_input.get('1.0', 'end-1c')
    morse_code = encoder.morsify(message)
    if morse_code:
        encode_feedback.configure(text="Success!")
        encode_output.insert('end', morse_code)
    else:
        encode_feedback.configure(text="Please input a message!")
        encode_output.insert('end', "🙄")


def create_ui(parent, background_color, command, action):
    parent.grid_columnconfigure(0, weight=1)
    parent.configure(fg_color=background_color)

    input_label = CTkLabel(
        parent,
        text="Your message:",
        padx=10,
        pady=10,
        font=FONT1,
    )
    input_label.grid(column=0, row=0, sticky='n')

    input_area = CTkTextbox(
        parent,
        width=250,
        height=100
    )
    input_area.grid(column=0, row=1, sticky='n')

    submit = CTkButton(
        parent,
        text=action,
        font=FONT2,
        width=100,
        height=40,
        fg_color='#471396',
        command=command
    )
    submit.grid(column=0, row=3, sticky='s', pady=(15, 15))

    output_area = CTkTextbox(
        parent,
        width=250,
        height=100
    )
    output_area.grid(column=0, row=4, sticky='n')

    output_label = CTkLabel(
        parent,
        text="",
        padx=10,
        pady=10,
        font=FONT1,
    )
    output_label.grid(column=0, row=5, sticky='n')

    return output_area, output_label, input_area


# USER INTERFACE  ----
app = CTk()
app.title("Morse Code Converter 1.1")
app.minsize(400, 400)
app.config(pady=50, padx=50, background=BG)
app.grid_columnconfigure(0, weight=1)
app.grid_rowconfigure(0, weight=1)

tabview = CTkTabview(master=app)
tabview.grid(column=0, row=0)

encode_tab = tabview.add("Encode")
decode_tab = tabview.add("Decode")


encode_output, encode_feedback, encode_input = create_ui(encode_tab, '#56021F', run_encoding, "MAKE MORSE")

decode_output, decode_feedback, decode_input = create_ui(decode_tab, '#004030', run_encoding, "UN-MORSE")

# input area label

# input area

# submit button

# output/results textarea

# output/feedback_message


app.mainloop()