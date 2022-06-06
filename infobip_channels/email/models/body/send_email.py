from io import IOBase
from typing import Optional

from pydantic import AnyHttpUrl, Field, StrictBool, constr

from infobip_channels.core.models import (
    CamelCaseModel,
    ContentTypeEnum,
    DateTimeValidator,
    MessageBodyBase,
    MultipartMixin,
)


class EmailMessageBody(MultipartMixin, MessageBodyBase, DateTimeValidator):
    from_email: str = Field(alias="from")
    to: str
    cc: Optional[str] = None
    bcc: Optional[str] = None
    subject: str
    text: Optional[str] = None
    bulk_id: Optional[str] = None
    message_id: Optional[str] = None
    templateid: Optional[int] = None
    attachment: Optional[IOBase] = None
    inline_image: Optional[IOBase] = None
    html: Optional[str] = Field(alias="HTML", default=None)
    replyto: Optional[str] = None
    defaultplaceholders: Optional[str] = None
    preserverecipients: Optional[StrictBool] = False
    tracking_url: Optional[str] = None
    trackclicks: Optional[StrictBool] = False
    trackopens: Optional[StrictBool] = False
    track: Optional[StrictBool] = True
    callback_data: Optional[constr(max_length=4000)] = None
    intermediateReport: Optional[StrictBool] = False
    notify_url: Optional[AnyHttpUrl] = None
    notify_content_type: Optional[ContentTypeEnum] = None
    send_at: Optional[str] = None
    landing_page_placeholders: Optional[str] = None
    landing_page_id: Optional[str] = None

    class Config(CamelCaseModel.Config):
        arbitrary_types_allowed = True
