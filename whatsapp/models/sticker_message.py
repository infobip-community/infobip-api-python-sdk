from pydantic import AnyUrl

from whatsapp.models.core import CamelCaseModel, MessageBody


class Content(CamelCaseModel):
    media_url: AnyUrl


class StickerMessageBody(MessageBody):
    content: Content
