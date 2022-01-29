from pydantic import Field, StrictBool, constr
from typing import Optional

from whatsapp.core.models import CamelCaseModel


class Content(CamelCaseModel):
    text: constr(max_length=4096)
    preview_url: Optional[StrictBool] = False
    callback_data: Optional[constr(max_length=4000)]


class MessageBody(CamelCaseModel):
    from_number: constr(max_length=24) = Field(alias="from")
    to: constr(max_length=24)
    message_id: Optional[constr(max_length=50)]
    content: Content
