from typing import Optional

from pydantic import conint

from infobip_channels.core.models import QueryParameter


class GetAllDomainsForAccountQueryParameters(QueryParameter):
    size: Optional[conint(ge=1, le=20)] = None
    page: Optional[conint(ge=0)] = None
