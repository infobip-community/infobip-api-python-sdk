from enum import Enum
from typing import Optional

from infobip_channels.core.models import CamelCaseModel
from infobip_channels.sms.models.body.core import Regional


class PINTypeEnum(str, Enum):
    NUMERIC = "NUMERIC"
    ALPHA = "ALPHA"
    HEX = "HEX"
    ALPHANUMERIC = "ALPHANUMERIC"


class LanguageEnum(str, Enum):
    EN = "en"
    ES = "es"
    CA = "ca"
    DA = "da"
    NL = "nl"
    FR = "fr"
    DE = "de"
    IT = "it"
    JA = "ja"
    KO = "ko"
    NO = "no"
    PL = "pl"
    RU = "ru"
    SV = "sv"
    FI = "fi"
    HR = "hr"
    SL = "sl"
    RO = "ro"
    PT_PT = "pt-pt"
    PT_BR = "pt-br"
    ZH_CN = "zh-cn"
    ZH_TW = "zh-tw"


class TFAMessageTemplate(CamelCaseModel):
    application_id: Optional[str]
    language: Optional[LanguageEnum]
    message_id: Optional[str]
    message_text: Optional[str]
    pin_length: Optional[int]
    pin_placeholder: Optional[str]
    pin_type: Optional[PINTypeEnum]
    regional: Optional[Regional]
    repeat_dtmf: Optional[str]
    sender_id: Optional[str]
    speech_rate: Optional[float]
