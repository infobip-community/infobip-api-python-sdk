from typing import Optional

from pydantic import constr

from infobip_channels.whatsapp.models.response.core import CamelCaseModel, MessageBody


class Action(CamelCaseModel):
    catalog_id: str
    product_retailer_id: str


class Footer(CamelCaseModel):
    text: constr(min_length=1, max_length=60)


class Body(CamelCaseModel):
    text: constr(min_length=1, max_length=1024)


class Content(CamelCaseModel):
    action: Action
    body: Optional[Body] = None
    footer: Optional[Footer] = None


class ProductMessageBody(MessageBody):
    content: Content
