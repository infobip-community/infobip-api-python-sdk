from pytest_cases import parametrize

from tests.conftest import (  # TemplateMessageBodyFactory,
    AudioMessageBodyFactory,
    ButtonsMessageBodyFactory,
    ContactMessageBodyFactory,
    DocumentMessageBodyFactory,
    ImageMessageBodyFactory,
    ListMessageBodyFactory,
    LocationMessageBodyFactory,
    MultiProductMessageBodyFactory,
    ProductMessageBodyFactory,
    StickerMessageBodyFactory,
    TextMessageBodyFactory,
    VideoMessageBodyFactory,
    get_response_error_content,
    get_response_error_invalid_content,
    get_response_object,
    get_response_ok_content,
    get_response_ok_invalid_content,
)

MESSAGE_TYPE_ATTRIBUTES = {
    # "template": {
    #     "message_body_factory": TemplateMessageBodyFactory,
    #     "endpoint": "/whatsapp/1/message/template",
    #     "method_name": "send_template_message",
    # },
    "text": {
        "message_body_factory": TextMessageBodyFactory,
        "endpoint": "/whatsapp/1/message/text",
        "method_name": "send_text_message",
    },
    "document": {
        "message_body_factory": DocumentMessageBodyFactory,
        "endpoint": "/whatsapp/1/message/document",
        "method_name": "send_document_message",
    },
    "audio": {
        "message_body_factory": AudioMessageBodyFactory,
        "endpoint": "/whatsapp/1/message/audio",
        "method_name": "send_audio_message",
    },
    "image": {
        "message_body_factory": ImageMessageBodyFactory,
        "endpoint": "/whatsapp/1/message/image",
        "method_name": "send_image_message",
    },
    "sticker": {
        "message_body_factory": StickerMessageBodyFactory,
        "endpoint": "/whatsapp/1/message/sticker",
        "method_name": "send_sticker_message",
    },
    "video": {
        "message_body_factory": VideoMessageBodyFactory,
        "endpoint": "/whatsapp/1/message/video",
        "method_name": "send_video_message",
    },
    "location": {
        "message_body_factory": LocationMessageBodyFactory,
        "endpoint": "/whatsapp/1/message/location",
        "method_name": "send_location_message",
    },
    "contact": {
        "message_body_factory": ContactMessageBodyFactory,
        "endpoint": "/whatsapp/1/message/contact",
        "method_name": "send_contact_message",
    },
    "buttons": {
        "message_body_factory": ButtonsMessageBodyFactory,
        "endpoint": "/whatsapp/1/message/interactive/buttons",
        "method_name": "send_interactive_buttons_message",
    },
    "list": {
        "message_body_factory": ListMessageBodyFactory,
        "endpoint": "/whatsapp/1/message/interactive/list",
        "method_name": "send_interactive_list_message",
    },
    "product": {
        "message_body_factory": ProductMessageBodyFactory,
        "endpoint": "/whatsapp/1/message/interactive/product",
        "method_name": "send_interactive_product_message",
    },
    "multi_product": {
        "message_body_factory": MultiProductMessageBodyFactory,
        "endpoint": "/whatsapp/1/message/interactive/multi-product",
        "method_name": "send_interactive_multi_product_message",
    },
}


@parametrize(
    message_type=MESSAGE_TYPE_ATTRIBUTES.keys(),
    message_body_type=("message_body_instance", "dict"),
    whatsapp_channel_instantiation_type=("auth_params", "auth_instance", "client"),
    responses=(
        (200, get_response_object, get_response_ok_content),
        (201, get_response_object, get_response_ok_content),
        (400, get_response_object, get_response_error_content),
        (401, get_response_object, get_response_error_content),
    ),
)
def from_all_instantiation_types_case__valid_content(
    message_type, responses, message_body_type, whatsapp_channel_instantiation_type
):
    return (
        MESSAGE_TYPE_ATTRIBUTES[message_type]["endpoint"],
        MESSAGE_TYPE_ATTRIBUTES[message_type]["message_body_factory"],
        MESSAGE_TYPE_ATTRIBUTES[message_type]["method_name"],
        responses[1],
        responses[0],
        responses[2](),
        message_body_type,
        whatsapp_channel_instantiation_type,
    )


@parametrize(
    message_type=MESSAGE_TYPE_ATTRIBUTES.keys(),
    message_body_type=("message_body_instance", "dict"),
    whatsapp_channel_instantiation_type=("auth_params", "auth_instance", "client"),
    responses=(
        (201, get_response_object, get_response_ok_invalid_content),
        (500, get_response_object, get_response_error_invalid_content),
    ),
)
def from_all_instantiation_types_case__invalid_content(
    message_type, responses, message_body_type, whatsapp_channel_instantiation_type
):
    return (
        MESSAGE_TYPE_ATTRIBUTES[message_type]["endpoint"],
        MESSAGE_TYPE_ATTRIBUTES[message_type]["message_body_factory"],
        MESSAGE_TYPE_ATTRIBUTES[message_type]["method_name"],
        responses[1],
        responses[0],
        responses[2](),
        message_body_type,
        whatsapp_channel_instantiation_type,
    )
