from typing import Optional

from pydantic import AnyHttpUrl, Field, constr, validator

from infobip_channels.core.models import MessageBodyBase, UrlLengthValidatorMixin


class MessageBody(UrlLengthValidatorMixin, MessageBodyBase):
    from_number: constr(min_length=1, max_length=24) = Field(alias="from")
    to: constr(min_length=1, max_length=24)
    message_id: Optional[constr(max_length=50)] = None
    callback_data: Optional[constr(max_length=4000)] = None
    notify_url: Optional[AnyHttpUrl] = None

    @validator("notify_url", pre=True)
    def validate_url_length(cls, value: str) -> str:
        return super().validate_url_length(value)
