import pandas as pd

data = pd.read_csv('code.csv', header=None, names=['char', 'code'])

class Encoder:

    def __init__(self):
        self.data = data

    def morsify(self, message):
        self.data = data.set_index('char')
        return self.converter(message, input_type='text')

    def demorsify(self, code):
        self.data = data.set_index('code')
        return self.converter(code, input_type='morse_code')

    def converter(self, message, input_type):
        char_list = ''
        if input_type == 'text':
            char_list = list(message.upper())
        elif input_type == 'morse_code':
            char_list = message.split()
        output = " ".join(
            self.data.reindex(char_list)
            .iloc[:, 0]
            .fillna('')
            .tolist()
        )
        return output if message else None

# Testing area:
# print(Encoder().demorsify(code='.... . .-.. .-.. ---'))