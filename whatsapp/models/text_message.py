from typing import Optional

from pydantic import StrictBool, constr

from whatsapp.models.core import CamelCaseModel, MessageBody


class Content(CamelCaseModel):
    text: constr(min_length=1, max_length=4096)
    preview_url: Optional[StrictBool] = False


class TextMessageBody(MessageBody):
    content: Content
