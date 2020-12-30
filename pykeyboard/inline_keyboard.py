from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


class InlineKeyboard(InlineKeyboardMarkup):
    _SYMBOL_FIRST_PAGE = '« {}'
    _SYMBOL_PREVIOUS_PAGE = '‹ {}'
    _SYMBOL_CURRENT_PAGE = '· {} ·'
    _SYMBOL_NEXT_PAGE = '{} ›'
    _SYMBOL_LAST_PAGE = '{} »'

    def __init__(self, row_width=3):
        self.inline_keyboard = list()
        super().__init__(inline_keyboard=self.inline_keyboard)
        self.row_width = row_width

    def add(self, *args):
        self.inline_keyboard = [
            args[i:i + self.row_width]
            for i in range(0, len(args), self.row_width)
        ]

    def row(self, *args):
        self.inline_keyboard.append([button for button in args])

    def _add_button(self, text, callback_data):
        return InlineKeyboardButton(
            text=text,
            callback_data=self.callback_pattern.format(
                number=callback_data)
        )

    @property
    def _left_pagination(self):
        return [
            self._add_button(
                self._SYMBOL_CURRENT_PAGE.format(number), number)
            if number == self.current_page else self._add_button(
                self._SYMBOL_NEXT_PAGE.format(number), number)
            if number == 4 else self._add_button(
                self._SYMBOL_LAST_PAGE.format(self.count_pages),
                self.count_pages)
            if number == 5 else self._add_button(number, number)
            for number in range(1, 6)
        ]

    @property
    def _middle_pagination(self):
        return [
            self._add_button(
                self._SYMBOL_FIRST_PAGE.format(1), 1),
            self._add_button(
                self._SYMBOL_PREVIOUS_PAGE.format(self.current_page - 1),
                self.current_page - 1),
            self._add_button(
                self._SYMBOL_CURRENT_PAGE.format(self.current_page),
                self.current_page),
            self._add_button(
                self._SYMBOL_NEXT_PAGE.format(self.current_page + 1),
                self.current_page + 1),
            self._add_button(
                self._SYMBOL_LAST_PAGE.format(self.count_pages),
                self.count_pages)
        ]

    @property
    def _right_pagination(self):
        return [
            self._add_button(
                self._SYMBOL_FIRST_PAGE.format(1), 1),
            self._add_button(
                self._SYMBOL_PREVIOUS_PAGE.format(self.count_pages - 3),
                self.count_pages - 3)
        ] + [
            self._add_button(
                self._SYMBOL_CURRENT_PAGE.format(number), number)
            if number == self.current_page else self._add_button(number, number)
            for number in range(self.count_pages - 2, self.count_pages + 1)
        ]

    @property
    def _full_pagination(self):
        return [
            self._add_button(number, number)
            if number != self.current_page else self._add_button(
                self._SYMBOL_CURRENT_PAGE.format(number), number)
            for number in range(1, self.count_pages + 1)
        ]

    @property
    def _build_pagination(self):
        if self.count_pages <= 5:
            return self._full_pagination
        else:
            if self.current_page <= 3:
                return self._left_pagination
            elif self.current_page > self.count_pages - 3:
                return self._right_pagination
            else:
                return self._middle_pagination

    def paginate(self, count_pages: int, current_page: int,
                 callback_pattern: str):
        self.count_pages = count_pages
        self.current_page = current_page
        self.callback_pattern = callback_pattern

        return self.inline_keyboard.append(self._build_pagination)
