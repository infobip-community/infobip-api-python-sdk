from typing import Optional

from models.core import CamelCaseModel, MessageBody
from pydantic import AnyUrl, constr


class Content(CamelCaseModel):
    media_url: AnyUrl
    caption: Optional[constr(max_length=3000)] = None
    filename: Optional[constr(max_length=240)] = None


class DocumentMessageBody(MessageBody):
    content: Content
