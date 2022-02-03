from typing import Optional

from models.core import CamelCaseModel, MessageBody
from pydantic import StrictBool, constr


class Content(CamelCaseModel):
    text: constr(min_length=1, max_length=4096)
    preview_url: Optional[StrictBool] = False


class TextMessageBody(MessageBody):
    content: Content
