from pyrogram.types import InlineQueryResultArticle,InputTextMessageContent,InlineQueryResult
from uuid import uuid4

class InlineQueryResults(list):
    def __init__(self):
        self.results = list()
        super().__init__(self.results)


    def add(self,title,message_text,message_parse_mode = None,message_disable_web_page_preview = None, url = None, description = None, thumb_url = None,reply_markup = None):
        self.results.append(
            InlineQueryResultArticle(
                id = uuid4(),
                title = title,
                input_message_content = InputTextMessageContent(message_text=message_text,parse_mode=message_parse_mode,disable_web_page_preview=message_disable_web_page_preview),
                url = url,
                description = description,
                thumb_url = thumb_url,
                reply_markup = reply_markup
            )
        )

        super().__init__(self.results)
