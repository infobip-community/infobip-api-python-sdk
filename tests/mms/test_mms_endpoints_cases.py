from pytest_cases import parametrize

from tests.mms.conftest import get_mms_response


@parametrize(
    responses=(
        [200, get_mms_response()],
        [400, get_mms_response()],
        [500, get_mms_response()],
    )
)
def case__valid_content(responses):
    return responses[0], responses[1]
