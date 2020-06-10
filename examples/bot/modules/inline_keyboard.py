from .. import App
from pykeyboard import InlineKeyboard
from pyrogram import Filters, InlineKeyboardButton


@App.on_message(Filters.command('inline_keyboard'))
def inline_keyboard_command(client, message):
    message.reply_text(
        '<b>Inline keyboard:</b>\n\n'
        '/add_inline_button - add buttons\n'
        '/row_inline_button - add button row\n'
    )


@App.on_message(Filters.command('add_inline_button'))
def add_inline_button_command(client, message):
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
    message.reply_text(
        '<b>Add buttons:</b>\n\n'
        '<code>keyboard = InlineKeyboard(row_width=3)</code>\n'
        '<code>keyboard.add(</code>\n'
        "<code>    InlineKeyboardButton('1', 'inline_keyboard#1'),</code>\n"
        "<code>    InlineKeyboardButton('2', 'inline_keyboard#2'),</code>\n"
        "<code>    InlineKeyboardButton('3', 'inline_keyboard#3'),</code>\n"
        "<code>    InlineKeyboardButton('4', 'inline_keyboard#4'),</code>\n"
        "<code>    InlineKeyboardButton('5', 'inline_keyboard#5'),</code>\n"
        "<code>    InlineKeyboardButton('6', 'inline_keyboard#6'),</code>\n"
        "<code>    InlineKeyboardButton('7', 'inline_keyboard#7')</code>\n"
        '<code>)</code>\n',
        reply_markup=keyboard
    )


@App.on_message(Filters.command('row_inline_button'))
def row_inline_button_command(client, message):
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
    message.reply_text(
        '<b>Add button row:</b>\n\n'
        "<code>keyboard = InlineKeyboard()</code>\n"
        "<code>keyboard.row(InlineKeyboardButton('1', 'inline_keyboard#1'))</code>\n"
        "<code>keyboard.row(</code>\n"
        "<code>    InlineKeyboardButton('2', 'inline_keyboard#2'),</code>\n"
        "<code>    InlineKeyboardButton('3', 'inline_keyboard#3')</code>\n"
        "<code>)</code>\n"
        "<code>keyboard.row(InlineKeyboardButton('4', 'inline_keyboard#4'))</code>\n"
        "<code>keyboard.row(</code>\n"
        "<code>    InlineKeyboardButton('5', 'inline_keyboard#5'),</code>\n"
        "<code>    InlineKeyboardButton('6', 'inline_keyboard#6')</code>\n"
        "<code>)</code>\n",
        reply_markup=keyboard
    )
