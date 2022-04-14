from typing import List
from infobip_channels.rcs.Models.body.send_rcs_message import RcsMessageBody

from infobip_channels.core.models import (
    MessageBodyBase,
)


class RcsMessageBodyList(MessageBodyBase):
    messages: List[RcsMessageBody]
