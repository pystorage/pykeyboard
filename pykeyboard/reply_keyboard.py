from pyrogram.types import (
    ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, ForceReply)


class ReplyKeyboard(ReplyKeyboardMarkup):
    def __init__(self, resize_keyboard=None, one_time_keyboard=None,
                 selective=None, placeholder=None, row_width=3):
        self.keyboard = list()
        super().__init__(
            keyboard=self.keyboard,
            resize_keyboard=resize_keyboard,
            one_time_keyboard=one_time_keyboard,
            selective=selective,
            placeholder=placeholder
        )
        self.row_width = row_width

    def add(self, *args):
        self.keyboard = [
            args[i:i + self.row_width]
            for i in range(0, len(args), self.row_width)
        ]

    def row(self, *args):
        self.keyboard.append([button for button in args])


class ReplyButton(KeyboardButton):
    def __init__(self, text=None, request_contact=None, request_location=None):
        super().__init__(
            text=text,
            request_contact=request_contact,
            request_location=request_location
        )


class ReplyKeyboardRemove(ReplyKeyboardRemove):
    def __init__(self, selective=None):
        super().__init__(selective=selective)


class ForceReply(ForceReply):
    def __init__(self, selective=None, placeholder=None):
        super().__init__(selective=selective, placeholder=placeholder)
