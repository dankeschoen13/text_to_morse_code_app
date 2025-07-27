import pandas as pd

data = pd.read_csv('code.csv', header=None, names=['char', 'code'])

class Encoder:

    def __init__(self):
        self.data = data.set_index('char')

    def morsify(self, message):
        char_list = list(message.upper())
        morse_list = [self.data[self.data.index == char].values[0][0] for char in char_list]
        morse_code = ", ".join(morse_list)
        return morse_code


# Testing area:
print(Encoder().morsify(message='Hello'))
