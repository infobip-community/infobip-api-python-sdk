from typing import List

from infobip_channels.core.models import MessageBodyBase
from infobip_channels.rcs.Models.body.send_rcs_message import RCSMessageBody


class RCSMessageBodyList(MessageBodyBase):
    messages: List[RCSMessageBody]
