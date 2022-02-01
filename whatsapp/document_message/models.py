from pydantic import AnyHttpUrl, constr
from typing import Optional

from whatsapp.core.models import CamelCaseModel, BaseMessageBody


class Content(CamelCaseModel):
    media_url: AnyHttpUrl
    caption: Optional[constr(max_length=3000)] = None
    filename: Optional[constr(max_length=240)] = None


class MessageBody(BaseMessageBody):
    content: Content
