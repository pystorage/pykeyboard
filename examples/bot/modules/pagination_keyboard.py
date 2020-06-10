from .. import App
from pyrogram import Filters, InlineKeyboardButton
from pykeyboard import InlinePaginationKeyboard


TEXT = 'sed risus pretium quam vulputate dignissim suspendisse in est ante in nibh mauris cursus mattis molestie a iaculis at erat pellentesque adipiscing commodo elit at imperdiet dui accumsan sit amet nulla facilisi morbi tempus iaculis urna id volutpat lacus laoreet non curabitur gravida arcu ac tortor dignissim convallis aenean et'


@App.on_message(Filters.command('pagination_keyboard'))
def pagination_keyboard_command(client, message):
    message.reply_text(
        '<b>Pagination inline keyboard:</b>\n\n'
        '/pagination_keyboard_3 - 3 pages\n'
        '/pagination_keyboard_5 - 5 pages\n'
        '/pagination_keyboard_9 - 9 pages\n'
        '/pagination_keyboard_25 - 25 pages\n'
        '/pagination_keyboard_100 - 100 pages\n'
        '/pagination_keyboard_150 - 150 page and buttons'
    )


@App.on_message(Filters.command('pagination_keyboard_3'))
def pagination_keyboard_3_command(client, message):
    keyboard = InlinePaginationKeyboard(3, 3, 'pagination_keyboard#{number}')

    message.reply_text(
        f'<b>3 page pagination:</b>\n\n {TEXT}',
        reply_markup=keyboard
    )


@App.on_message(Filters.command('pagination_keyboard_5'))
def pagination_keyboard_5_command(client, message):
    keyboard = InlinePaginationKeyboard(5, 3, 'pagination_keyboard#{number}')

    message.reply_text(
        f'<b>5 page pagination:</b>\n\n {TEXT}',
        reply_markup=keyboard
    )


@App.on_message(Filters.command('pagination_keyboard_9'))
def pagination_keyboard_9_command(client, message):
    keyboard = InlinePaginationKeyboard(9, 5, 'pagination_keyboard#{number}')

    message.reply_text(
        f'<b>9 page pagination:</b>\n\n {TEXT}',
        reply_markup=keyboard
    )


@App.on_message(Filters.command('pagination_keyboard_25'))
def pagination_keyboard_25_command(client, message):
    keyboard = InlinePaginationKeyboard(
        25, 14, 'pagination_keyboard#{number}')

    message.reply_text(
        f'<b>25 page pagination:</b>\n\n {TEXT}',
        reply_markup=keyboard
    )


@App.on_message(Filters.command('pagination_keyboard_100'))
def pagination_keyboard_100_command(client, message):
    keyboard = InlinePaginationKeyboard(
        100, 100, 'pagination_keyboard#{number}')

    message.reply_text(
        f'<b>100 page pagination:</b>\n\n {TEXT}',
        reply_markup=keyboard
    )


@App.on_message(Filters.command('pagination_keyboard_150'))
def pagination_keyboard_150_command(client, message):
    keyboard = InlinePaginationKeyboard(
        150, 123, 'pagination_keyboard#{number}')
    keyboard.row(
        InlineKeyboardButton('Back', 'pagination_keyboard#back'),
        InlineKeyboardButton('Close', 'pagination_keyboard#close')
    )

    message.reply_text(
        f'<b>150 page pagination and buttons:</b>\n\n {TEXT}',
        reply_markup=keyboard
    )
