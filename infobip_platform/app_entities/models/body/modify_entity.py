from typing import Optional

from pydantic.types import constr

from infobip_channels.whatsapp.models.body.core import MessageBody


class ModifyEntityBody(MessageBody):
    entityName: Optional[constr(max_length=255)] = None
