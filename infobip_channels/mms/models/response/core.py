from typing import Optional

from infobip_channels.core.models import CamelCaseModel


class Price(CamelCaseModel):
    price_per_message: Optional[int] = None
    currency: Optional[str] = None
