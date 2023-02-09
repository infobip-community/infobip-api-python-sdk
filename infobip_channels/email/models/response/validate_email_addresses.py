from typing import Optional

from infobip_channels.core.models import ResponseBase


class ValidateEmailAddressesResponse(ResponseBase):
    to: str
    valid_mailbox: str
    valid_syntax: bool
    catch_all: bool
    disposable: bool
    role_based: bool
    reason: Optional[str] = None
