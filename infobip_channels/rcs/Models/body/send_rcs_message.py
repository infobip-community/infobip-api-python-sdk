from enum import Enum
from typing import List, Optional, Union

try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal

from pydantic import AnyHttpUrl, Field, confloat, constr, validator

from infobip_channels.core.models import (
    CamelCaseModel,
    MessageBodyBase,
    UrlLengthValidatorMixin,
)


class ValidityPeriodTimeUnitEnum(str, Enum):
    SECONDS = "SECONDS"
    MINUTES = "MINUTES"
    HOURS = "HOURS"
    DAYS = "DAYS"


class CardWidth(str, Enum):
    SMALL = "SMALL"
    MEDIUM = "MEDIUM"


class HeightEnum(str, Enum):
    SHORT = "SHORT"
    MEDIUM = "MEDIUM"
    TALL = "TALL"


class AlignmentEnum(str, Enum):
    LEFT = "LEFT"
    RIGHT = "RIGHT"


class OrientationEnum(str, Enum):
    HORIZONTAL = "HORIZONTAL"
    VERTICAL = "VERTICAL"


class FileProperties(CamelCaseModel, UrlLengthValidatorMixin):
    url: AnyHttpUrl

    _MAX_URL_LENGTH = 1000

    @validator("url", pre=True)
    def validate_url_length(cls, value: str) -> str:
        return super().validate_url_length(value)


class ThumbnailProperties(CamelCaseModel, UrlLengthValidatorMixin):
    url: AnyHttpUrl

    _MAX_URL_LENGTH = 1000

    @validator("url", pre=True)
    def validate_url_length(cls, value: str) -> str:
        return super().validate_url_length(value)


class Suggestion(CamelCaseModel):
    text: constr(min_length=1, max_length=25)
    postback_data: constr(min_length=1, max_length=2048)


class SuggestionReply(Suggestion):
    type: Literal["REPLY"]


class SuggestionOpenUrl(Suggestion, UrlLengthValidatorMixin):
    type: Literal["OPEN_URL"]
    url: AnyHttpUrl

    _MAX_URL_LENGTH = 1000

    @validator("url", pre=True)
    def validate_url_length(cls, value: str) -> str:
        return super().validate_url_length(value)


class SuggestionDialPhone(Suggestion):
    type: Literal["DIAL_PHONE"]
    phone_number: Optional[constr(regex=r"\+?\d{5,15}")] = None  # noqa: F722


class SuggestionShowLocation(Suggestion):
    type: Literal["SHOW_LOCATION"]
    latitude: confloat(ge=-90, le=90)
    longitude: confloat(ge=-180, le=180)
    label: Optional[constr(min_length=1, max_length=100)] = None


class SuggestionRequestLocation(Suggestion):
    type: Literal["REQUEST_LOCATION"]


class CardMedia(CamelCaseModel):
    file: FileProperties
    thumbnail: Optional[ThumbnailProperties] = None
    height: HeightEnum


class CardContent(CamelCaseModel):
    title: Optional[constr(min_length=1, max_length=200)] = None
    description: Optional[constr(min_length=1, max_length=2000)] = None
    media: Optional[CardMedia] = None
    suggestions: Optional[
        List[
            Union[
                SuggestionShowLocation,
                SuggestionDialPhone,
                SuggestionOpenUrl,
                SuggestionReply,
                SuggestionRequestLocation,
            ]
        ]
    ] = None

    @validator("suggestions")
    def validate_suggestions(cls, suggestions: List[Suggestion]) -> List[Suggestion]:
        if len(suggestions) > 4:
            raise ValueError("There can be only four suggestions in a card")
        return suggestions


class Contents(CardContent):
    pass


class ContentCarousel(CamelCaseModel):
    type: Literal["CAROUSEL"]
    card_width: CardWidth
    contents: List[Contents]
    suggestions: Optional[
        List[
            Union[
                SuggestionShowLocation,
                SuggestionDialPhone,
                SuggestionOpenUrl,
                SuggestionReply,
                SuggestionRequestLocation,
            ]
        ]
    ] = None

    @validator("contents")
    def validate_contents(cls, contents: List[Contents]) -> List[Contents]:
        if len(contents) < 2 or len(contents) > 10:
            raise ValueError("There can be only 2 - 10 content objects in a Carousel")

        return contents


class ContentCard(CamelCaseModel):
    type: Literal["CARD"]
    orientation: OrientationEnum
    alignment: AlignmentEnum
    content: CardContent
    suggestions: Optional[
        List[
            Union[
                SuggestionShowLocation,
                SuggestionDialPhone,
                SuggestionOpenUrl,
                SuggestionReply,
                SuggestionRequestLocation,
            ]
        ]
    ] = None


class ContentFile(CamelCaseModel):
    type: Literal["FILE"]
    file: FileProperties
    thumbnail: Optional[ThumbnailProperties] = None


class ContentText(CamelCaseModel):
    type: Literal["TEXT"]
    text: constr(min_length=1, max_length=1000)
    suggestions: Optional[
        List[
            Union[
                SuggestionShowLocation,
                SuggestionDialPhone,
                SuggestionOpenUrl,
                SuggestionReply,
                SuggestionRequestLocation,
            ]
        ]
    ] = []


class SmsFailover(CamelCaseModel):
    from_number: constr(min_length=1) = Field(alias="from")
    text: constr(min_length=1)
    validity_period: Optional[int] = None
    validity_period_time_unit: Optional[ValidityPeriodTimeUnitEnum] = None


class RCSMessageBody(MessageBodyBase):
    from_number: Optional[str] = Field(alias="from")
    to: str
    validity_period: Optional[int] = None
    validity_period_time_unit: Optional[ValidityPeriodTimeUnitEnum] = None
    content: Union[ContentCarousel, ContentCard, ContentFile, ContentText]
    sms_failover: Optional[SmsFailover] = None
    notify_url: Optional[str] = None
    callback_data: Optional[str] = None
    message_id: Optional[str] = None
