from pydantic_factories import ModelFactory

from infobip_platform.app_entities.models.body.create_entity import CreateEntityBody
from infobip_platform.app_entities.models.body.modify_entity import ModifyEntityBody


def get_get_entities_response():
    return {
        "results": [{"entityName": "Test name", "entityId": "test-entity"}],
        "paging": {"page": 0, "size": 1, "totalPages": 0, "totalResults": 0},
    }


def get_create_entity_request_error_response():
    return {
        "requestError": {
            "serviceException": {
                "messageId": "BAD_REQUEST",
                "text": "Bad request",
                "validationErrors": {
                    "request.message.content.media.file.url": ["is not a valid url"],
                },
            }
        }
    }


def get_create_entity_body():
    return {"entityName": "Test name", "entityId": "test-entity"}


class GenerateCreateEntityBodyFactoryIntegration(ModelFactory):
    __model__ = CreateEntityBody

    @classmethod
    def build(cls, *args, **kwargs):
        """Needed because factory classes don't play well with custom validation."""
        return CreateEntityBody(**get_create_entity_body())


class GenerateModifyEntityBodyFactoryIntegration(ModelFactory):
    __model__ = ModifyEntityBody

    @classmethod
    def build(cls, *args, **kwargs):
        """Needed because factory classes don't play well with custom validation."""
        return ModifyEntityBody(**get_modify_entity_body())


def get_create_entity_response():
    return None


def get_get_entity_response():
    return {"entityName": "Test name", "entityId": "test-entity"}


def get_get_entity_request_error_response():
    return get_create_entity_request_error_response()


def get_modify_entity_body():
    return {"entityName": "Test name"}


def get_modify_entity_response():
    return None


def get_modify_entity_request_error_response():
    return get_get_entity_request_error_response()
