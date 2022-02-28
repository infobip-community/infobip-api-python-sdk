from infobip_channels.whatsapp.models.response.core import WhatsAppResponse
from infobip_channels.whatsapp.models.response.get_templates import Template


class CreateTemplateResponseOK(WhatsAppResponse, Template):
    pass
