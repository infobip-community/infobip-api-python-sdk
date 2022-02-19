from pydantic import AnyHttpUrl, validator

from infobip_channels.whatsapp.models.core import (
    CamelCaseModel,
    MessageBody,
    UrlLengthValidatorMixin,
)


class Content(UrlLengthValidatorMixin, CamelCaseModel):
    media_url: AnyHttpUrl

    @validator("media_url", pre=True)
    def validate_url_length(cls, value: str) -> str:
        return super().validate_url_length(value)


class StickerMessageBody(MessageBody):
    content: Content
