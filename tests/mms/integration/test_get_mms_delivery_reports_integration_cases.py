from pytest_cases import parametrize

from tests.mms.conftest import get_mms_delivery_reports_response


@parametrize(
    responses=(
        [200, get_mms_delivery_reports_response()],
        [400, get_mms_delivery_reports_response()],
        [500, get_mms_delivery_reports_response()],
    )
)
def case__supported_status(responses):
    return responses[0], responses[1]


def case__unsupported_status():
    return 201, get_mms_delivery_reports_response()
