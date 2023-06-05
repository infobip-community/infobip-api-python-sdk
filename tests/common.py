from infobip.client import APIClient
from infobip.sync_client import SyncAPIClient

TEST_URL = "https://some.url"
TEST_API_KEY = "some-api-key"


def get_test_client():
    return APIClient(base_url=TEST_URL, api_key=TEST_API_KEY)


def get_test_sync_client():
    return SyncAPIClient(base_url=TEST_URL, api_key=TEST_API_KEY)
