from .. import App
from pyrogram import Filters


@App.on_message(Filters.command(['start', 'help']))
def start_command(client, message):
    message.reply_text(
        f'Welcome <b>{message.from_user.first_name}</b>!\n\n'
        'I will help you learn how to wrk with the <b>pykeyboard</b> library.\n\n'
        '<b>Library features:</b>\n\n'
        '/install - library installation\n'
        '/inline_keyboard - inline keyboard\n'
        '/pagination_keyboard - pagination inline keyboard\n'
        '/reply_keyboard - reply keyboard'
    )