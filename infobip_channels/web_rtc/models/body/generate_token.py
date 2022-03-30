from enum import Enum
from typing import Optional

from pydantic import conint, constr

from infobip_channels.core.models import CamelCaseModel, MessageBodyBase


class RecordingEnum(str, Enum):
    ALWAYS = "ALWAYS"
    ON_DEMAND = "ON_DEMAND"
    DISABLED = "DISABLED"


class Capabilities(CamelCaseModel):
    recording: Optional[RecordingEnum] = None


class GenerateTokenBody(MessageBodyBase):
    identity: constr(regex=r"[\u0020-\ud7ff]{3,64}$")  # noqa: F722
    application_id: Optional[str] = None
    display_name: Optional[constr(min_length=5, max_length=50)] = None
    capabilities: Optional[Capabilities] = None
    time_to_live: Optional[conint(gt=0, lt=86401)] = None
