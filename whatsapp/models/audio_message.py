from pydantic import AnyHttpUrl, validator

from whatsapp.models.core import CamelCaseModel, MessageBody, ValidateUrlLengthMixin


class Content(ValidateUrlLengthMixin, CamelCaseModel):
    media_url: AnyHttpUrl

    @validator("media_url", pre=True)
    def validate_url_length(cls, value: str) -> str:
        return super().validate_url_length(value)


class AudioMessageBody(MessageBody):
    content: Content
