from abc import ABC, abstractmethod
from typing import Any, Dict, Type, Union

import requests
from pydantic import AnyHttpUrl, BaseModel, ValidationError

from infobip_channels.core.http_client import _HttpClient
from infobip_channels.core.models import (
    Authentication,
    GetHeaders,
    MessageBodyBase,
    PathParameter,
    PostHeaders,
    QueryParameter,
    ResponseBase,
)


class Channel(ABC):
    """Parent class for all Infobip channels."""

    def __init__(self, client: Union[_HttpClient, Any]) -> None:
        self._client = client

    @classmethod
    def from_auth_params(cls, auth_params: Dict[str, str]) -> "Channel":
        """Create an Authentication instance from the provided dictionary and
        use it to instantiate the Channel subclass. Dictionary has to contain
        "base_url" and "api_key" to be able to authenticate with the Infobip's API.
        The Channel subclass instantiated this way will use the default _HttpClient
        class for making HTTP requests.

        :param auth_params: Dictionary containing "base_url" and "api_key"
        :return: Instance of the subclass
        """
        client = _HttpClient(Authentication(**auth_params))
        return cls(client)

    @classmethod
    def from_auth_instance(cls, auth_instance: Authentication) -> "Channel":
        """Instantiate the Channel subclass with the provided auth object.
        The Channel subclass instantiated this way will use the default _HttpClient
        class for making HTTP requests.

        :param auth_instance: Authentication class instance
        :return: Instance of the subclass
        """
        client = _HttpClient(auth_instance)
        return cls(client)

    @classmethod
    def from_provided_client(cls, client: Any) -> "Channel":
        """Instantiate the Channel subclass with the provided client object.
        The Channel subclass instantiated this way will use the provided client for
        making HTTP requests. This client can implement its own retry mechanisms,
        timeouts, etc., but it has to implement all the methods used in the default
        _HttpClient class. When using the Channel subclass this way, the user has to
        take care of providing a valid base_url and constructing headers to be used for
        every Channel subclass request.

        :param client: Client used for making HTTP requests
        :return: Instance of the subclass
        """
        return cls(client)

    @staticmethod
    def validate_query_parameter(
        parameter: Union[QueryParameter, Dict], parameter_type: Type[QueryParameter]
    ) -> QueryParameter:
        """
        Validate the query parameter by trying to instantiate the provided class.
        If the passed parameter is already of that type, just return it as is.

        :param parameter: Query parameter to validate
        :param parameter_type: Type of the query parameter
        :return: Class instance corresponding to the provided parameter type
        """
        return (
            parameter
            if isinstance(parameter, parameter_type)
            else parameter_type(**parameter)
        )

    @staticmethod
    def validate_auth_params(
        base_url: Union[AnyHttpUrl, str], api_key: str
    ) -> Authentication:
        """Validate the provided base_url and api_key. This validation is purely client
        side. If the parameters are validated successfully, an instance of the
        Authentication class is returned which holds the base_url and api_key values.

        :param base_url: Base url which the requests will call for each endpoint
        :param api_key: Secret used for authenticating the user
        :return: Authentication class instance
        """
        return Authentication(base_url=base_url, api_key=api_key)

    @staticmethod
    def build_post_request_headers(api_key: str) -> Dict:
        """Build the request headers dictionary which has to be used for each of the
        post requests.

        :param api_key: Key used for populating Authorization header
        :return: Dictionary of headers to be used for post requests
        """
        return PostHeaders(authorization=api_key).dict(by_alias=True)

    @staticmethod
    def build_get_request_headers(api_key: str) -> Dict:
        """Build the request headers dictionary which has to be used for each of the
        get requests.

        :param api_key: Key used for populating Authorization header
        :return: Dictionary of headers to be used for get requests
        """
        return GetHeaders(authorization=api_key).dict(by_alias=True)

    @staticmethod
    def convert_model_to_dict(
        model: BaseModel, by_alias: bool = True, exclude_unset: bool = True, **kwargs
    ) -> Dict:
        """
        Convert the Pydantic model into a Python dictionary. By default, model is
        converted with by_alias=True and exclude_unset=True flags. The former changes
        model fields to camel case and the latter omits the fields which were not
        received from the server originally.
        For additional flags, check Pydantic's documentation on exporting models:
        https://pydantic-docs.helpmanual.io/usage/exporting_models/.

        :param model: Pydantic model to convert
        :param by_alias: Whether the model should be converted with aliased fields
        :param exclude_unset: Whether the model's unset values should be omitted
        :return: Dictionary of the converted model
        """
        return model.dict(by_alias=by_alias, exclude_unset=exclude_unset, **kwargs)

    @staticmethod
    def validate_path_parameter(
        parameter: Union[PathParameter, Dict], parameter_type: Type[PathParameter]
    ) -> Union[PathParameter]:
        """
        Validate path parameter by trying to instantiate the provided class and
        extract valid path parameter.

        :param parameter: Path parameter to validate
        :param parameter_type: Type of path parameter
        :return: Class instance corresponding to the provided parameter type
        """
        return (
            parameter
            if isinstance(parameter, parameter_type)
            else parameter_type(**parameter)
        )

    @staticmethod
    def validate_message_body(
        message: Union[MessageBodyBase, Dict],
        message_type: Type[MessageBodyBase],
    ) -> Union[MessageBodyBase]:
        """Validate the message by trying to instantiate the provided type class.
        If the passed message is already of that type, just return it as is.

        :param message: Message body to validate
        :param message_type: Type of the message body
        :return: Class instance corresponding to the provided message body type
        """
        return message if isinstance(message, message_type) else message_type(**message)

    def _construct_response(
        self, raw_response: Union[requests.Response, Any], *args, **kwargs
    ) -> Union[ResponseBase, requests.Response, Any]:
        try:
            response_class = self._get_custom_response_class(
                raw_response, *args, **kwargs
            )

            response_json = raw_response.json()
            if type(response_json) is list:
                raw_response_data = {"list": response_json}
            else:
                raw_response_data = response_json

            return response_class(
                **{
                    "status_code": raw_response.status_code,
                    "raw_response": raw_response,
                    **raw_response_data,
                }
            )

        except (AttributeError, ValueError, ValidationError):
            return raw_response

    @abstractmethod
    def _get_custom_response_class(
        self, raw_response: Union[requests.Response, Any], *args, **kwargs
    ) -> Type[ResponseBase]:
        raise NotImplementedError
