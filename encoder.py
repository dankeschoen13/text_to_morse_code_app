import pandas as pd

data = pd.read_csv('code.csv', header=None, names=['char', 'code'])

class Encoder:

    def __init__(self):
        self.data = data.set_index('char')

    def morsify(self, message):
        char_list = list(message.upper())
        morse_code = " ".join(
            self.data.reindex(char_list)
            .iloc[:, 0]
            .fillna('')
            .tolist()
        )
        return morse_code if message else None

# Testing area:
# print(Encoder().morsify(message='Hello!'))