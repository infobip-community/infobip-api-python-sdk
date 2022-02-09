from typing import Optional

from pydantic import confloat, constr

from whatsapp.models.core import CamelCaseModel, MessageBody


class Content(CamelCaseModel):
    latitude: confloat(ge=-90, le=90)
    longitude: confloat(ge=-180, le=180)
    name: Optional[constr(max_length=1000)] = None
    address: Optional[constr(max_length=1000)] = None


class LocationMessageBody(MessageBody):
    content: Content
