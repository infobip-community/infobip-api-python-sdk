from enum import Enum
from typing import Optional, Union

try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal

from pydantic import AnyHttpUrl, conlist, constr, validator

from infobip_channels.whatsapp.models.response.core import (
    CamelCaseModel,
    UrlLengthValidatorMixin,
)


class LanguageEnum(str, Enum):
    AF = "af"
    SQ = "sq"
    AR = "ar"
    AZ = "az"
    BN = "bn"
    BG = "bg"
    CA = "ca"
    ZH_CN = "zh_CN"
    ZH_HK = "zh_HK"
    ZH_TW = "zh_TW"
    HR = "hr"
    CS = "cs"
    DA = "da"
    NL = "nl"
    EN = "en"
    EN_GB = "en_GB"
    EN_US = "en_US"
    ET = "et"
    FIL = "fil"
    FI = "fi"
    FR = "fr"
    DE = "de"
    EL = "el"
    GU = "gu"
    HA = "ha"
    HE = "he"
    HI = "hi"
    HU = "hu"
    ID = "id"
    GA = "ga"
    IT = "it"
    JA = "ja"
    KN = "kn"
    KK = "kk"
    KO = "ko"
    LO = "lo"
    LV = "lv"
    LT = "lt"
    MK = "mk"
    MS = "ms"
    ML = "ml"
    MR = "mr"
    NB = "nb"
    FA = "fa"
    PL = "pl"
    PT_BR = "pt_BR"
    PT_PT = "pt_PT"
    PA = "pa"
    RO = "ro"
    RU = "ru"
    SR = "sr"
    SK = "sk"
    SL = "sl"
    ES = "es"
    ES_AR = "es_AR"
    ES_ES = "es_ES"
    ES_MX = "es_MX"
    SW = "sw"
    SV = "sv"
    TA = "ta"
    TE = "te"
    TH = "th"
    TR = "tr"
    UK = "uk"
    UR = "ur"
    UZ = "uz"
    VI = "vi"
    UNKNOWN = "unknown"


class HeaderText(CamelCaseModel):
    format: Literal["TEXT"]
    text: constr(max_length=60)


class HeaderImage(CamelCaseModel):
    format: Literal["IMAGE"]


class HeaderVideo(CamelCaseModel):
    format: Literal["VIDEO"]


class HeaderDocument(CamelCaseModel):
    format: Literal["DOCUMENT"]


class HeaderLocation(CamelCaseModel):
    format: Literal["LOCATION"]


class CategoryEnum(str, Enum):
    ACCOUNT_UPDATE = "ACCOUNT_UPDATE"
    PAYMENT_UPDATE = "PAYMENT_UPDATE"
    PERSONAL_FINANCE_UPDATE = "PERSONAL_FINANCE_UPDATE"
    SHIPPING_UPDATE = "SHIPPING_UPDATE"
    RESERVATION_UPDATE = "RESERVATION_UPDATE"
    ISSUE_RESOLUTION = "ISSUE_RESOLUTION"
    APPOINTMENT_UPDATE = "APPOINTMENT_UPDATE"
    TRANSPORTATION_UPDATE = "TRANSPORTATION_UPDATE"
    TICKET_UPDATE = "TICKET_UPDATE"
    ALERT_UPDATE = "ALERT_UPDATE"
    AUTO_REPLY = "AUTO_REPLY"


class ButtonPhoneNumber(CamelCaseModel):
    type: Literal["PHONE_NUMBER"]
    text: constr(max_length=200)
    phone_number: str


class ButtonUrl(UrlLengthValidatorMixin, CamelCaseModel):
    type: Literal["URL"]
    text: constr(max_length=200)
    url: AnyHttpUrl

    @validator("url", pre=True)
    def validate_url_length(cls, value: str) -> str:
        return super().validate_url_length(value)


class ButtonQuickReply(CamelCaseModel):
    type: Literal["QUICK_REPLY"]
    text: constr(max_length=200)


class Structure(CamelCaseModel):
    header: Optional[
        Union[HeaderText, HeaderImage, HeaderVideo, HeaderDocument, HeaderLocation]
    ] = None
    body: str
    footer: Optional[constr(max_length=60)] = None
    buttons: Optional[
        conlist(
            Union[ButtonPhoneNumber, ButtonUrl, ButtonQuickReply],
            min_items=1,
            max_items=3,
        )
    ]


class CreateTemplate(CamelCaseModel):
    name: constr(regex=r"^[a-z0-9_]+$")  # noqa: F722
    language: LanguageEnum
    category: CategoryEnum
    structure: Structure
