from pydantic import AnyHttpUrl, validator

from infobip_channels.core.models import CamelCaseModel, UrlLengthValidatorMixin
from infobip_channels.whatsapp.models.body.core import MessageBody


class Content(UrlLengthValidatorMixin, CamelCaseModel):
    media_url: AnyHttpUrl

    @validator("media_url", pre=True)
    def validate_url_length(cls, value: str) -> str:
        return super().validate_url_length(value)


class StickerMessageBody(MessageBody):
    content: Content
