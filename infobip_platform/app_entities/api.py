from http import HTTPStatus
from typing import Any, Dict, Type, Union

import requests

from infobip_channels.core.channel import Channel
from infobip_channels.core.models import ResponseBase
from infobip_platform.app_entities.models.body.create_entity import CreateEntityBody
from infobip_platform.app_entities.models.body.modify_entity import ModifyEntityBody
from infobip_platform.app_entities.models.query_parameters.get_entities import (
    GetEntitiesQueryParameters,
)
from infobip_platform.app_entities.models.response.core import PlatformResponseError
from infobip_platform.app_entities.models.response.create_entity import (
    CreateEntityResponse,
)
from infobip_platform.app_entities.models.response.get_entities import (
    GetEntitiesResponse,
)
from infobip_platform.app_entities.models.response.get_entity import GetEntityResponse
from infobip_platform.app_entities.models.response.modify_entity import (
    ModifyEntityResponse,
)


class ApplicationEntityManagement(Channel):
    """Class used for interaction with the Infobip Application and Entity Management API."""

    PROVISIONING_PATH_VERSION_1 = "/provisioning/1/"

    def _get_custom_response_class(
        self,
        raw_response: Union[requests.Response, Any],
        response_class: Type[ResponseBase],
        *args,
        **kwargs,
    ) -> Type[ResponseBase]:
        if raw_response.status_code == HTTPStatus.OK:
            return response_class
        elif raw_response.status_code in (
            HTTPStatus.BAD_REQUEST,
            HTTPStatus.UNAUTHORIZED,
            HTTPStatus.FORBIDDEN,
            HTTPStatus.TOO_MANY_REQUESTS,
            HTTPStatus.INTERNAL_SERVER_ERROR,
            HTTPStatus.NOT_FOUND,
        ):
            return PlatformResponseError

        raise ValueError

    def get_entities(
        self,
        query_parameters: Union[GetEntitiesQueryParameters, Dict],
    ) -> Union[GetEntitiesResponse, ResponseBase, Any]:
        """Get a paginated list of entities.

        :return Response with a list of Entity objects.
        """
        query_parameters = self.validate_query_parameter(
            query_parameters or {}, GetEntitiesQueryParameters
        )

        response = self._client.get(
            self.PROVISIONING_PATH_VERSION_1 + "entities",
            params=query_parameters.dict(by_alias=True),
        )
        return self._construct_response(response, GetEntitiesResponse)

    def create_entity(
        self,
        request_body: Union[CreateEntityBody, Dict],
    ) -> Union[CreateEntityResponse, ResponseBase, Any]:
        """Create an entity associated with the specified entityId.

        :param request_body: Body of the Entity to be created.
        :return Response with status.
        """

        message = self.validate_message_body(request_body, CreateEntityBody)

        response = self._client.post(
            self.PROVISIONING_PATH_VERSION_1 + "entities",
            message.dict(by_alias=True),
        )

        return self._construct_response(response, CreateEntityResponse)

    def get_entity(self, entity_id: str) -> Union[GetEntityResponse, ResponseBase, Any]:
        """Get an entity for the specified entityId.

        :param entity_id: Entity ID.
        :return Response with the Entity object.
        """
        response = self._client.get(
            self.PROVISIONING_PATH_VERSION_1 + "entities/" + entity_id
        )
        return self._construct_response(response, GetEntityResponse)

    def modify_entity(
        self,
        entity_id: str,
        request_body: Union[ModifyEntityBody, Dict],
    ) -> Union[ModifyEntityResponse, ResponseBase, Any]:
        """Modify an entity for the specified entityId.

        :param entity_id: Entity ID.
        :param request_body: Body of the Entity to be modified.
        :return Response with status.
        """
        message = self.validate_message_body(request_body, ModifyEntityBody)

        response = self._client.put(
            self.PROVISIONING_PATH_VERSION_1 + "entities/" + entity_id,
            message.dict(by_alias=True),
        )

        return self._construct_response(response, ModifyEntityResponse)
