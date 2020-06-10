from .. import App
from pykeyboard import ReplyKeyboard
from pyrogram import Filters, KeyboardButton


@App.on_message(Filters.command('reply_keyboard'))
def reply_keyboard_command(client, message):
    message.reply_text(
        '<b>Reply keyboard:</b>\n\n'
        '/add_reply_button - add buttons\n'
        '/row_reply_button - add button row\n'
    )


@App.on_message(Filters.command('add_reply_button'))
def add_reply_button_command(client, message):
    keyboard = ReplyKeyboard(row_width=3)
    keyboard.add(
        KeyboardButton('1', 'reply_keyboard#1'),
        KeyboardButton('2', 'reply_keyboard#2'),
        KeyboardButton('3', 'reply_keyboard#3'),
        KeyboardButton('4', 'reply_keyboard#4'),
        KeyboardButton('5', 'reply_keyboard#5'),
    )
    message.reply_text(
        '<b>Add buttons:</b>\n\n'
        '<code>keyboard = ReplyKeyboard(row_width=3)</code>\n'
        '<code>keyboard.add(</code>\n'
        "<code>    KeyboardButton('1', 'reply_keyboard#1'),</code>\n"
        "<code>    KeyboardButton('2', 'reply_keyboard#2'),</code>\n"
        "<code>    KeyboardButton('3', 'reply_keyboard#3'),</code>\n"
        "<code>    KeyboardButton('4', 'reply_keyboard#4'),</code>\n"
        "<code>    KeyboardButton('5', 'reply_keyboard#5'),</code>\n"
        '<code>)</code>\n',
        reply_markup=keyboard
    )


@App.on_message(Filters.command('row_reply_button'))
def row_reply_button_command(client, message):
    keyboard = ReplyKeyboard()
    keyboard.row(KeyboardButton('1', 'reply_keyboard#1'))
    keyboard.row(
        KeyboardButton('2', 'reply_keyboard#2'),
        KeyboardButton('3', 'reply_keyboard#3')
    )
    keyboard.row(KeyboardButton('4', 'reply_keyboard#4'))
    keyboard.row(KeyboardButton('5', 'reply_keyboard#5'))
    message.reply_text(
        '<b>Add button row:</b>\n\n'
        "<code>keyboard = ReplyKeyboard()</code>\n"
        "<code>keyboard.row(KeyboardButton('1', 'reply_keyboard#1'))</code>\n"
        "<code>keyboard.row(</code>\n"
        "<code>    KeyboardButton('2', 'reply_keyboard#2'),</code>\n"
        "<code>    KeyboardButton('3', 'reply_keyboard#3')</code>\n"
        "<code>)</code>\n"
        "<code>keyboard.row(KeyboardButton('4', 'reply_keyboard#4'))</code>\n"
        "<code>keyboard.row(KeyboardButton('5', 'reply_keyboard#5'))</code>\n",
        reply_markup=keyboard
    )
