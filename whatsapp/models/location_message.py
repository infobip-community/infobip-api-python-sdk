from typing import Optional

from pydantic import confloat, constr

from whatsapp.models.core import CamelCaseModel, MessageBody


class Content(CamelCaseModel):
    latitude: confloat(ge=-90, le=90)
    longitude: confloat(ge=-180, le=180)
    name: Optional[constr(min_length=1, max_length=1000)]
    address: Optional[constr(min_length=1, max_length=1000)]


class LocationMessageBody(MessageBody):
    content: Content
