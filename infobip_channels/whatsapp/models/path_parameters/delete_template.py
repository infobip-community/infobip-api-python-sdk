from infobip_channels.whatsapp.models.path_parameters.core import WhatsAppPathParameters


class DeleteTemplatePathParameters(WhatsAppPathParameters):
    template_name: str
