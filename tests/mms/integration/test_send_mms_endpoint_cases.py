from pytest_cases import parametrize

from tests.mms.conftest import get_send_mms_response


@parametrize(
    responses=(
        [200, get_send_mms_response()],
        [400, get_send_mms_response()],
        [500, get_send_mms_response()],
    )
)
def case__supported_status(responses):
    return responses[0], responses[1]


def case__unsupported_status():
    return 201, get_send_mms_response()
