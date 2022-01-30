from pydantic import Field, AnyHttpUrl, constr
from typing import Optional

from whatsapp.core.models import CamelCaseModel


class Content(CamelCaseModel):
    media_url: AnyHttpUrl
    caption: Optional[constr(max_length=3000)]
    filename: Optional[constr(max_length=240)]


class MessageBody(CamelCaseModel):
    from_number: constr(max_length=24) = Field(alias="from")
    to: constr(max_length=24)
    message_id: Optional[constr(max_length=50)]
    content: Content
    callback_data: Optional[constr(max_length=4000)]
