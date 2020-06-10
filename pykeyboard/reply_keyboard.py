from pyrogram import ReplyKeyboardMarkup


class ReplyKeyboard(ReplyKeyboardMarkup):
    def __init__(self, resize_keyboard=None, one_time_keyboard=None,
                 selective=None, row_width=3):
        self.keyboard = list()
        super().__init__(
            keyboard=self.keyboard,
            resize_keyboard=resize_keyboard,
            one_time_keyboard=one_time_keyboard,
            selective=selective
        )
        self.row_width = row_width

    def add(self, *args):
        self.keyboard = [
            args[i:i + self.row_width]
            for i in range(0, len(args), self.row_width)
        ]

    def row(self, *args):
        self.keyboard.append([button for button in args])
