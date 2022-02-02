from typing import Optional

from pydantic import AnyHttpUrl, constr

from whatsapp.core.models import CamelCaseModel, MessageBody


class Content(CamelCaseModel):
    media_url: AnyHttpUrl
    caption: Optional[constr(max_length=3000)] = None
    filename: Optional[constr(max_length=240)] = None


class DocumentMessageBody(MessageBody):
    content: Content
