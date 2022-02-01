__title__ = 'pykeyboard'
__version__ = '0.1.5'
__author__ = 'PyMaster'
__license__ = 'MIT License'
__copyright__ = 'Copyright 2020-2022 PyMaster'

from .inline_keyboard import InlineKeyboard, InlineButton
from .inline_pagination_keyboard import InlinePaginationKeyboard, InlineButton
from .reply_keyboard import (
    ReplyKeyboard, ReplyButton, ReplyKeyboardRemove, ForceReply)
