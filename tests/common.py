from infobip.client import APIClient

TEST_URL = "https://some.url"
TEST_API_KEY = "some-api-key"


def get_test_client():
    return APIClient(base_url=TEST_URL, api_key=TEST_API_KEY)
