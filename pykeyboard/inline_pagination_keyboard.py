from pyrogram import InlineKeyboardMarkup, InlineKeyboardButton


class InlinePaginationKeyboard(InlineKeyboardMarkup):
    SYMBOL_FIRST_PAGE = '« {}'
    SYMBOL_PREVIOUS_PAGE = '‹ {}'
    SYMBOL_CURRENT_PAGE = '· {} ·'
    SYMBOL_NEXT_PAGE = '{} ›'
    SYMBOL_LAST_PAGE = '{} »'

    def __init__(self, count_pages: int, current_page: int,
                 callback_pattern: str):
        self.inline_keyboard = list()
        super().__init__(inline_keyboard=self.inline_keyboard)
        self.count_pages = count_pages
        self.current_page = current_page
        self.callback_pattern = callback_pattern
        self.markup

    def add_button(self, text, callback_data):
        return InlineKeyboardButton(
            text=text,
            callback_data=self.callback_pattern.format(
                number=callback_data)
        )

    @property
    def left_pagination(self):
        return [
            self.add_button(
                self.SYMBOL_CURRENT_PAGE.format(number), number)
            if number == self.current_page else self.add_button(
                self.SYMBOL_NEXT_PAGE.format(number), number)
            if number == 4 else self.add_button(
                self.SYMBOL_LAST_PAGE.format(self.count_pages),
                self.count_pages)
            if number == 5 else self.add_button(number, number)
            for number in range(1, 6)
        ]

    @property
    def middle__pagination(self):
        return [
            self.add_button(
                self.SYMBOL_FIRST_PAGE.format(1), 1),
            self.add_button(
                self.SYMBOL_PREVIOUS_PAGE.format(self.current_page - 1),
                self.current_page - 1),
            self.add_button(
                self.SYMBOL_CURRENT_PAGE.format(self.current_page),
                self.current_page),
            self.add_button(
                self.SYMBOL_NEXT_PAGE.format(self.current_page + 1),
                self.current_page + 1),
            self.add_button(
                self.SYMBOL_LAST_PAGE.format(self.count_pages),
                self.count_pages),
        ]

    @property
    def right_pagination(self):
        return [
            self.add_button(
                self.SYMBOL_FIRST_PAGE.format(1), 1),
            self.add_button(
                self.SYMBOL_PREVIOUS_PAGE.format(self.count_pages - 3),
                self.count_pages - 3)
        ] + [
            self.add_button(
                self.SYMBOL_CURRENT_PAGE.format(number), number)
            if number == self.current_page else self.add_button(number, number)
            for number in range(self.count_pages - 2, self.count_pages + 1)
        ]

    @property
    def full_pagination(self):
        return [
            self.add_button(number, number)
            if number != self.current_page else self.add_button(
                self.SYMBOL_CURRENT_PAGE.format(number), number)
            for number in range(1, self.count_pages + 1)
        ]

    @property
    def build_pagination(self):
        if self.count_pages <= 5:
            return self.full_pagination
        else:
            if self.current_page <= 3:
                return self.left_pagination
            elif self.current_page > self.count_pages - 3:
                return self.right_pagination
            else:
                return self.middle__pagination

    def row(self, *args):
        self.inline_keyboard.append([button for button in args])

    @property
    def markup(self):
        self.inline_keyboard.append(self.build_pagination)
