<div align="center">
<p align="center">
<img src="https://raw.githubusercontent.com/pystorage/pykeyboard/master/docs/source/images/logo.png" alt="Pykeyboard">
</p>

![PyPI](https://img.shields.io/pypi/v/pykeyboard)
[![Downloads](https://pepy.tech/badge/pykeyboard)](https://pepy.tech/project/pykeyboard)
![GitHub](https://img.shields.io/github/license/pystorage/pykeyboard)

</div>

## Installation

```shell
pip install pykeyboard
```

## Documentation

### Inline Keyboard

```python
from pykeyboard import InlineKeyboard
```

#### Parameters:

- row_width (integer, default 3)

#### Inline Keyboard add buttons

##### Code

```python
from pykeyboard import InlineKeyboard
from pyrogram.types import InlineKeyboardButton


keyboard = InlineKeyboard(row_width=3)
keyboard.add(
    InlineKeyboardButton('1', 'inline_keyboard#1'),
    InlineKeyboardButton('2', 'inline_keyboard#2'),
    InlineKeyboardButton('3', 'inline_keyboard#3'),
    InlineKeyboardButton('4', 'inline_keyboard#4'),
    InlineKeyboardButton('5', 'inline_keyboard#5'),
    InlineKeyboardButton('6', 'inline_keyboard#6'),
    InlineKeyboardButton('7', 'inline_keyboard#7')
)
```

##### Result

<p><img src="https://raw.githubusercontent.com/pystorage/pykeyboard/master/docs/source/images/add_inline_button.png" alt="add_inline_button"></p>

#### Inline Keyboard row buttons

##### Code

```python
from pykeyboard import InlineKeyboard
from pyrogram.types import InlineKeyboardButton


keyboard = InlineKeyboard()
keyboard.row(InlineKeyboardButton('1', 'inline_keyboard#1'))
keyboard.row(
    InlineKeyboardButton('2', 'inline_keyboard#2'),
    InlineKeyboardButton('3', 'inline_keyboard#3')
)
keyboard.row(InlineKeyboardButton('4', 'inline_keyboard#4'))
keyboard.row(
    InlineKeyboardButton('5', 'inline_keyboard#5'),
    InlineKeyboardButton('6', 'inline_keyboard#6')
)
```

##### Result

<p><img src="https://raw.githubusercontent.com/pystorage/pykeyboard/master/docs/source/images/row_inline_button.png" alt="row_inline_button"></p>

### Reply Keyboard

```python
from pykeyboard import ReplyKeyboard
```

#### Parameters:

- resize_keyboard (bool, optional)
- one_time_keyboard (bool, optional)
- selective (bool, optional)
- row_width (integer, default 3)

#### Reply Keyboard add buttons

##### Code

```python
from pykeyboard import ReplyKeyboard
from pyrogram.types import KeyboardButton


keyboard = ReplyKeyboard(row_width=3)
keyboard.add(
    KeyboardButton('1', 'reply_keyboard#1'),
    KeyboardButton('2', 'reply_keyboard#2'),
    KeyboardButton('3', 'reply_keyboard#3'),
    KeyboardButton('4', 'reply_keyboard#4'),
    KeyboardButton('5', 'reply_keyboard#5'),
)
```

##### Result

<p><img src="https://raw.githubusercontent.com/pystorage/pykeyboard/master/docs/source/images/add_reply_button.png" alt="add_reply_button"></p>

#### Reply Keyboard row buttons

##### Code

```python
from pykeyboard import ReplyKeyboard
from pyrogram.types import KeyboardButton


keyboard = ReplyKeyboard()
keyboard.row(KeyboardButton('1', 'reply_keyboard#1'))
keyboard.row(
    KeyboardButton('2', 'reply_keyboard#2'),
    KeyboardButton('3', 'reply_keyboard#3')
)
keyboard.row(KeyboardButton('4', 'reply_keyboard#4'))
keyboard.row(KeyboardButton('5', 'reply_keyboard#5'))
```

##### Result

<p><img src="https://raw.githubusercontent.com/pystorage/pykeyboard/master/docs/source/images/row_reply_button.png" alt="row_reply_button"></p>

### Pagination inline keyboard

```python
from pykeyboard import InlinePaginationKeyboard
```

#### Parameters:

- count_pages (integer)
- current_page (integer)
- callback_pattern (string) - use of the `{number}` pattern is <ins>required</ins>

#### Pagination 3 pages

##### Code

```python
from pykeyboard import InlinePaginationKeyboard


keyboard = InlinePaginationKeyboard(3, 3, 'pagination_keyboard#{number}')
```

##### Result

<p><img src="https://raw.githubusercontent.com/pystorage/pykeyboard/master/docs/source/images/pagination_keyboard_3.png" alt="pagination_keyboard_3"></p>

#### Pagination 5 pages

##### Code

```python
from pykeyboard import InlinePaginationKeyboard


keyboard = InlinePaginationKeyboard(5, 3, 'pagination_keyboard#{number}')
```

##### Result

<p><img src="https://raw.githubusercontent.com/pystorage/pykeyboard/master/docs/source/images/pagination_keyboard_5.png" alt="pagination_keyboard_5"></p>

#### Pagination 9 pages

##### Code

```python
from pykeyboard import InlinePaginationKeyboard


keyboard = InlinePaginationKeyboard(9, 5, 'pagination_keyboard#{number}')
```

##### Result

<p><img src="https://raw.githubusercontent.com/pystorage/pykeyboard/master/docs/source/images/pagination_keyboard_9.png" alt="pagination_keyboard_9"></p>

#### Pagination 25 pages

##### Code

```python
from pykeyboard import InlinePaginationKeyboard


keyboard = InlinePaginationKeyboard(25, 14, 'pagination_keyboard#{number}')
```

##### Result

<p><img src="https://raw.githubusercontent.com/pystorage/pykeyboard/master/docs/source/images/pagination_keyboard_25.png" alt="pagination_keyboard_25"></p>

#### Pagination 100 pages

##### Code

```python
from pykeyboard import InlinePaginationKeyboard


keyboard = InlinePaginationKeyboard(100, 100, 'pagination_keyboard#{number}')
```

##### Result

<p><img src="https://raw.githubusercontent.com/pystorage/pykeyboard/master/docs/source/images/pagination_keyboard_100.png" alt="pagination_keyboard_100"></p>

#### Pagination 150 pages and buttons

##### Code

```python
from pykeyboard import InlinePaginationKeyboard
from pyrogram.types import InlineKeyboardButton


keyboard = InlinePaginationKeyboard(150, 123, 'pagination_keyboard#{number}')
keyboard.row(
    InlineKeyboardButton('Back', 'pagination_keyboard#back'),
    InlineKeyboardButton('Close', 'pagination_keyboard#close')
)
```

##### Result

<p><img src="https://raw.githubusercontent.com/pystorage/pykeyboard/master/docs/source/images/pagination_keyboard_150.png" alt="pagination_keyboard_150"></p>
