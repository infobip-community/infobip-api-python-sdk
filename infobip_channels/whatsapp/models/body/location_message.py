from typing import Optional

from pydantic import confloat, constr

from infobip_channels.core.models import CamelCaseModel
from infobip_channels.whatsapp.models.body.core import MessageBody


class Content(CamelCaseModel):
    latitude: confloat(ge=-90, le=90)
    longitude: confloat(ge=-180, le=180)
    name: Optional[constr(max_length=1000)] = None
    address: Optional[constr(max_length=1000)] = None


class LocationMessageBody(MessageBody):
    content: Content
