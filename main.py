from customtkinter import *
from encoder import Encoder

# === UI CONFIG / STYLE CONSTANTS ===
LABEL_FONT = ("Courier", 20)
BUTTON_FONT = ("Helvetica", 15)
APP_BG = "#1E201E"
TAB1_COLOR = "#56021F"
TAB2_COLOR = "#004030"
BUTTON_COLOR = "#471396"

# === FUNCTIONS ===
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

def create_ui(parent, tab_color, command, action):
    parent.grid_columnconfigure(0, weight=1)
    parent.configure(fg_color=tab_color)

    input_label = CTkLabel(
        parent,
        text="Your message:",
        padx=10,
        pady=10,
        font=LABEL_FONT,
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
        font=BUTTON_FONT,
        width=100,
        height=40,
        fg_color=BUTTON_COLOR,
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
        font=LABEL_FONT,
    )
    output_label.grid(column=0, row=5, sticky='n')

    return output_area, output_label, input_area

# === USER INTERFACE ===
app = CTk()
app.title("Morse Code Converter 1.1")
app.minsize(400, 400)
app.config(pady=50, padx=50, background=APP_BG)
app.grid_columnconfigure(0, weight=1)
app.grid_rowconfigure(0, weight=1)

tabview = CTkTabview(master=app)
tabview.grid(column=0, row=0)

encode_tab = tabview.add("Encode")
decode_tab = tabview.add("Decode")

encode_output, encode_feedback, encode_input = create_ui(encode_tab, TAB1_COLOR, run_encoding, "MAKE MORSE")
decode_output, decode_feedback, decode_input = create_ui(decode_tab, TAB2_COLOR, run_encoding, "UN-MORSE")

app.mainloop()