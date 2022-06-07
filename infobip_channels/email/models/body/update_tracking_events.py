from typing import Optional

from pydantic import StrictBool

from infobip_channels.core.models import MessageBodyBase


class UpdateTrackingEventsMessageBody(MessageBodyBase):
    open: Optional[StrictBool] = None
    clicks: Optional[StrictBool] = None
    unsubscribe: Optional[StrictBool] = None
