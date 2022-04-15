from typing import List
from infobip_channels.rcs.Models.body.send_rcs_message import RCSMessageBody

from infobip_channels.core.models import (
    MessageBodyBase,
)


class RCSMessageBodyList(MessageBodyBase):
    messages: List[RCSMessageBody]
