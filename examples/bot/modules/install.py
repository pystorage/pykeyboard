from .. import App
from pyrogram import Filters


@App.on_message(Filters.command('install'))
def install_command(client, message):
    message.reply_text(
        '<b>Installation:</b>\n\n'
        '<code>pip install -U pykeyboard</code>'
    )
