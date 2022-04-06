from enum import Enum
from typing import Optional

import regex
from pydantic import conint, constr, validator

from infobip_channels.core.models import CamelCaseModel, MessageBodyBase


class RecordingEnum(str, Enum):
    ALWAYS = "ALWAYS"
    ON_DEMAND = "ON_DEMAND"
    DISABLED = "DISABLED"


class Capabilities(CamelCaseModel):
    recording: RecordingEnum


class GenerateTokenBody(MessageBodyBase):
    identity: str
    application_id: Optional[str] = None
    display_name: Optional[constr(min_length=5, max_length=50)] = None
    capabilities: Optional[Capabilities] = None
    time_to_live: Optional[conint(gt=0, lt=86401)] = None

    @validator("identity")
    def validate_identity(cls, identity: str) -> str:
        """
        Using regex lib for unicode characters
        This module supports Unicode 14.0.0.
        Full Unicode case-folding is supported.
        https://pypi.org/project/regex/

        :param identity: Identity string to check
        :return: Valid Identity string format
        """
        identity_match = regex.match(r"^[\p{L}\p{N}\-_+=/.]{3,64}$", identity)
        if identity_match:
            return identity
        else:
            raise ValueError("Identity format is not valid")
