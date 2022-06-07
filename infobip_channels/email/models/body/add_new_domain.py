from infobip_channels.core.models import MessageBodyBase


class AddNewDomainMessageBody(MessageBodyBase):
    domain_name: str
