from customtkinter import *
from encoder import Encoder

# === UI CONFIG / STYLE CONSTANTS ===
LABEL_FONT = ("Courier", 20)
BUTTON_FONT = ("Helvetica", 15)
APP_BG = "#1E201E"
TAB1_COLOR = "#56021F"
TAB2_COLOR = "#004030"
BUTTON_COLOR = "#471396"
DEFAULT_OUTPUT = "🙄"

# === FUNCTIONS ===
encoder = Encoder()

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

    submit_button = CTkButton(
        parent,
        text=action,
        font=BUTTON_FONT,
        width=100,
        height=40,
        fg_color=BUTTON_COLOR,
        command=command
    )
    submit_button.grid(column=0, row=3, sticky='s', pady=(15, 15))

    output_area = CTkTextbox(
        parent,
        width=250,
        height=100
    )
    output_area.grid(column=0, row=4, sticky='n')

    output_feedback = CTkLabel(
        parent,
        text="",
        padx=10,
        pady=10,
        font=LABEL_FONT,
    )
    output_feedback.grid(column=0, row=5, sticky='n')

    return input_area, output_area, output_feedback


def initialize():
    current_tab = tabview.get()
    input_field, output_field, feedback = widgets[current_tab]

    output_field.delete("1.0", "end")
    message = input_field.get('1.0', 'end-1c')

    if not message:
        feedback.configure(text="Please input a message!")
        output_field.insert('end', text=DEFAULT_OUTPUT)
        return None

    if current_tab == 'Encode':
        output_field.insert('end', text=encoder.morsify(message))
    elif current_tab == 'Decode':
        output_field.insert('end', text=encoder.demorsify(message))

    feedback.configure(text="Success!")
    return None


# === USER INTERFACE ===
app = CTk()
app.title("Morse-ify 1.1")
app.minsize(400, 400)
app.config(pady=50, padx=50, background=APP_BG)
app.grid_columnconfigure(0, weight=1)
app.grid_rowconfigure(0, weight=1)

tabview = CTkTabview(master=app)
tabview.grid(column=0, row=0)

encode_tab = tabview.add("Encode")
decode_tab = tabview.add("Decode")

widgets = dict()

widgets['Encode'] = create_ui(encode_tab, TAB1_COLOR, initialize, "MAKE MORSE")
widgets['Decode'] = create_ui(decode_tab, TAB2_COLOR, initialize, "UN-MORSE")

app.mainloop()