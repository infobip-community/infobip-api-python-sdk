from typing import Optional

from infobip_channels.whatsapp.models.headers.core import RequestHeaders


class PostHeaders(RequestHeaders):
    content_type: Optional[str] = "application/json"
