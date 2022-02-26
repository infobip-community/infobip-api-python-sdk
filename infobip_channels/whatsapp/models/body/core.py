from typing import Optional

from pydantic import AnyHttpUrl, BaseModel, Field, constr, validator

from infobip_channels.whatsapp.models.core import CamelCaseModel


class UrlLengthValidatorMixin:
    MAX_URL_LENGTH = 2048

    @classmethod
    def validate_url_length(cls, value: str) -> str:
        if not isinstance(value, str):
            return value

        if len(value) > cls.MAX_URL_LENGTH:
            raise ValueError(f"Url length must be less than {cls.MAX_URL_LENGTH}")

        return value


class MessageBody(UrlLengthValidatorMixin, CamelCaseModel):
    from_number: constr(min_length=1, max_length=24) = Field(alias="from")
    to: constr(min_length=1, max_length=24)
    message_id: Optional[constr(max_length=50)] = None
    callback_data: Optional[constr(max_length=4000)] = None
    notify_url: Optional[AnyHttpUrl] = None

    @validator("notify_url", pre=True)
    def validate_url_length(cls, value: str) -> str:
        return super().validate_url_length(value)


class Authentication(BaseModel):
    base_url: AnyHttpUrl
    api_key: constr(min_length=1)

    @validator("base_url", pre=True)
    def validate_scheme(cls, value: str) -> str:
        if not isinstance(value, str):
            return value

        if value.startswith(("http://", "https://")):
            return value

        return f"https://{value}"
