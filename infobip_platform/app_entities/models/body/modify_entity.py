from typing import Optional

from pydantic.types import constr

from infobip_channels.core.models import MessageBodyBase


class ModifyEntityBody(MessageBodyBase):
    entity_name: Optional[constr(max_length=255)] = None
