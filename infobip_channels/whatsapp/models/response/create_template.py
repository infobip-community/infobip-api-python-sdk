from infobip_channels.core.models import ResponseBase
from infobip_channels.whatsapp.models.response.get_templates import Template


class CreateTemplateResponseOK(ResponseBase, Template):
    pass
