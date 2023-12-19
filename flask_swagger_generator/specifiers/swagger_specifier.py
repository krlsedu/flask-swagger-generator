from abc import ABC, abstractmethod
from typing import List
from flask_swagger_generator.utils import RequestType, SecurityType


class SwaggerSpecifier(ABC):

    def __init__(self):
        self.application_name = None
        self.application_version = None
        self.server_url = None
        self.application_description = None

    @abstractmethod
    def add_response(
            self,
            function_name: str,
            status_code: int,
            schema,
            description: str = ""
    ):
        raise NotImplementedError()

    @abstractmethod
    def add_endpoint(
            self,
            function_name,
            path: str,
            request_types: List[RequestType],
            group: str = None
    ):
        raise NotImplementedError()

    @abstractmethod
    def add_query_parameters(self, function_name, parameters):
        raise NotImplementedError()

    @abstractmethod
    def add_request_body(self, function_name, schema):
        raise NotImplementedError()

    @abstractmethod
    def add_security(self, function_name, security_type: SecurityType):
        raise NotImplementedError()

    def set_application_name(self, application_name):
        self.application_name = application_name

    def set_application_version(self, application_version):
        self.application_version = application_version

    def set_server_url(self, server_url):
        self.server_url = server_url

    def set_application_description(self, application_description):
        self.application_description = application_description

    @abstractmethod
    def clean(self):
        pass
