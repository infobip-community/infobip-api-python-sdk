from pydantic import Field, StrictBool, constr
from typing import Optional

from whatsapp.core.models import CamelCaseModel


class Content(CamelCaseModel):
    text: constr(min_length=1, max_length=4096)
    preview_url: Optional[StrictBool] = False
    callback_data: Optional[constr(max_length=4000)] = None


class MessageBody(CamelCaseModel):
    from_number: constr(min_length=1, max_length=24) = Field(alias="from")
    to: constr(min_length=1, max_length=24)
    message_id: Optional[constr(max_length=50)] = None
    content: Content
