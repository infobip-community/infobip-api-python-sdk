from pydantic import AnyHttpUrl, validator

from infobip_channels.whatsapp.models.body.core import (
    CamelCaseModel,
    MessageBody,
    ValidateUrlLengthMixin,
)


class Content(ValidateUrlLengthMixin, CamelCaseModel):
    media_url: AnyHttpUrl

    @validator("media_url", pre=True)
    def validate_url_length(cls, value: str) -> str:
        return super().validate_url_length(value)


class StickerMessageBody(MessageBody):
    content: Content
