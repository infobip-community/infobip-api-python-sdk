import unittest
from http import HTTPStatus

import pytest

from infobip_platform.app_entities.api import ApplicationEntityManagement


@pytest.mark.skip(reason="credentials needed, server state dependent")
class EntityManagementTestCase(unittest.TestCase):
    api = ApplicationEntityManagement.from_env()

    def test_get_entities(self):
        response = EntityManagementTestCase.api.get_entities()

        self.assertIsNotNone(response)
        self.assertEqual(HTTPStatus.OK, response.status_code)

    def test_create_entity(self):
        entity_body = {"entityName": "A cool Entity", "entityId": "test-entity"}
        response = EntityManagementTestCase.api.create_entity(entity_body)

        self.assertIsNotNone(response)
        self.assertEqual(HTTPStatus.CREATED, response.status_code)
