import pytest
from pydantic.error_wrappers import ValidationError

from infobip_channels.whatsapp.models.core import MessageBody
from infobip_channels.whatsapp.models.list_message import ListMessageBody
from tests.conftest import ListMessageBodyFactory, get_random_string


@pytest.fixture
def valid_action():
    return {
        "action": {
            "title": "title",
            "sections": [
                {
                    "title": "title",
                    "rows": [{"id": "200", "title": "row title"}],
                }
            ],
        },
    }


def test_list_message_body__is_an_instance_of_message_body():
    assert isinstance(ListMessageBodyFactory.build(), MessageBody) is True


@pytest.mark.parametrize(
    "content",
    [
        None,
        "",
        {},
        {"body": {"text": "test"}},
        {
            "action": {
                "title": "title",
                "sections": [
                    {
                        "title": "title",
                        "rows": [{"id": "200", "title": "row title"}],
                    }
                ],
            },
        },
    ],
)
def test_when_content_is_invalid__validation_error_is_raised(content):
    with pytest.raises(ValidationError):
        ListMessageBody(
            **{"from": "441134960000", "to": "38598451987", "content": content}
        )


@pytest.mark.parametrize("body", [None, "", {}])
def test_when_body_is_invalid__validation_error_is_raised(body, valid_action):
    with pytest.raises(ValidationError):
        ListMessageBody(
            **{
                "from": "441134960000",
                "to": "38598451987",
                "content": {"body": body, **valid_action},
            }
        )


@pytest.mark.parametrize("text", [None, "", {}, get_random_string(1025)])
def test_when_body_text_is_invalid__validation_error_is_raised(text, valid_action):
    with pytest.raises(ValidationError):
        ListMessageBody(
            **{
                "from": "441134960000",
                "to": "38598451987",
                "content": {"body": {"text": text}, **valid_action},
            }
        )


@pytest.mark.parametrize(
    "action",
    [
        None,
        "",
        {},
        {"title": "text"},
        {
            "sections": [
                {
                    "title": "title",
                    "rows": [{"id": "200", "title": "row title"}],
                }
            ]
        },
    ],
)
def test_when_action_is_invalid__validation_error_is_raised(action):
    with pytest.raises(ValidationError):
        ListMessageBody(
            **{
                "from": "441134960000",
                "to": "38598451987",
                "content": {"body": {"text": "test"}, "action": action},
            }
        )


@pytest.mark.parametrize("title", [None, "", {}, get_random_string(21)])
def test_when_action_title_is_invalid__validation_error_is_raised(title):
    with pytest.raises(ValidationError):
        ListMessageBody(
            **{
                "from": "441134960000",
                "to": "38598451987",
                "content": {
                    "body": {"text": "test"},
                    "action": {
                        "title": title,
                        "sections": [
                            {
                                "title": "My title",
                                "rows": [
                                    {"id": "myId", "title": "T", "description": "Test"}
                                ],
                            }
                        ],
                    },
                },
            }
        )


@pytest.mark.parametrize(
    "sections",
    [
        None,
        "",
        {},
        [],
        [
            {
                "title": "My title",
                "rows": [{"id": "myId", "title": "T", "description": "Test"}],
            }
            for _ in range(11)
        ],
        [
            {"title": "", "rows": [{"id": "myId", "title": "T"}]},
            {"title": "Title 1", "rows": [{"id": "myId 2", "title": "T"}]},
        ],
        [
            {"title": None, "rows": [{"id": "myId", "title": "T"}]},
            {"title": "Title 1", "rows": [{"id": "myId 2", "title": "T"}]},
        ],
        [
            {"title": "Title 1", "rows": [{"id": "myId", "title": "T"}]},
            {"title": "Title 2", "rows": [{"id": "myId", "title": "T"}]},
        ],
    ],
)
def test_when_action_sections_is_invalid__validation_error_is_raised(sections):
    with pytest.raises(ValidationError):
        ListMessageBody(
            **{
                "from": "441134960000",
                "to": "38598451987",
                "content": {
                    "body": {"text": "test"},
                    "action": {"title": "TEST", "sections": sections},
                },
            }
        )


@pytest.mark.parametrize("sections_title", [{}, get_random_string(25)])
def test_when_sections_title_is_invalid__validation_error_is_raised(sections_title):
    with pytest.raises(ValidationError):
        ListMessageBody(
            **{
                "from": "441134960000",
                "to": "38598451987",
                "content": {
                    "body": {"text": "test"},
                    "action": {
                        "title": "TEST",
                        "sections": [
                            {
                                "title": sections_title,
                                "rows": [
                                    {"id": "myId", "title": "T", "description": "Test"}
                                ],
                            }
                        ],
                    },
                },
            }
        )


@pytest.mark.parametrize(
    "rows",
    [None, "", {}, [], [{}], [{"id": "12", "title": "T"}, {"id": "12", "title": "T"}]],
)
def test_when_sections_rows_is_invalid__validation_error_is_raised(rows):
    with pytest.raises(ValidationError):
        ListMessageBody(
            **{
                "from": "441134960000",
                "to": "38598451987",
                "content": {
                    "body": {"text": "test"},
                    "action": {
                        "title": "TEST",
                        "sections": [{"title": "My title", "rows": rows}],
                    },
                },
            }
        )


@pytest.mark.parametrize("row_id", [None, "", {}, get_random_string(201)])
def test_when_row_id_is_invalid__validation_error_is_raised(row_id):
    with pytest.raises(ValidationError):
        ListMessageBody(
            **{
                "from": "441134960000",
                "to": "38598451987",
                "content": {
                    "body": {"text": "test"},
                    "action": {
                        "title": "TEST",
                        "sections": [
                            {
                                "title": "My title",
                                "rows": [
                                    {"id": row_id, "title": "T", "description": "Test"}
                                ],
                            }
                        ],
                    },
                },
            }
        )


@pytest.mark.parametrize("title", [None, "", {}, get_random_string(25)])
def test_when_row_title_is_invalid__validation_error_is_raised(title):
    with pytest.raises(ValidationError):
        ListMessageBody(
            **{
                "from": "441134960000",
                "to": "38598451987",
                "content": {
                    "body": {"text": "test"},
                    "action": {
                        "title": "TEST",
                        "sections": [
                            {
                                "title": "My title",
                                "rows": [{"id": "123", "title": title}],
                            }
                        ],
                    },
                },
            }
        )


@pytest.mark.parametrize("description", [{}, get_random_string(73)])
def test_when_row_description_is_invalid__validation_error_is_raised(description):
    with pytest.raises(ValidationError):
        ListMessageBody(
            **{
                "from": "441134960000",
                "to": "38598451987",
                "content": {
                    "body": {"text": "test"},
                    "action": {
                        "title": "TEST",
                        "sections": [
                            {
                                "title": "My title",
                                "rows": [
                                    {
                                        "id": "123",
                                        "title": "title",
                                        "description": description,
                                    }
                                ],
                            }
                        ],
                    },
                },
            }
        )


@pytest.mark.parametrize("header_type", [None, "", {}, "TEST"])
def test_when_header_type_is_invalid__validation_error_is_raised(header_type):
    with pytest.raises(ValidationError):
        ListMessageBody(
            **{
                "from": "441134960000",
                "to": "38598451987",
                "content": {
                    "body": {"text": "test"},
                    "action": {
                        "title": "TEST",
                        "sections": [
                            {
                                "title": "My title",
                                "rows": [
                                    {
                                        "id": "123",
                                        "title": "title",
                                    }
                                ],
                            }
                        ],
                    },
                    "header": {"type": header_type, "text": "TEST"},
                },
            }
        )


@pytest.mark.parametrize("text", [None, "", {}, get_random_string(61)])
def test_when_header_text_is_invalid__validation_error_is_raised(text):
    with pytest.raises(ValidationError):
        ListMessageBody(
            **{
                "from": "441134960000",
                "to": "38598451987",
                "content": {
                    "body": {"text": "test"},
                    "action": {
                        "title": "TEST",
                        "sections": [
                            {
                                "title": "My title",
                                "rows": [
                                    {
                                        "id": "123",
                                        "title": "title",
                                    }
                                ],
                            }
                        ],
                    },
                    "header": {"type": "TEXT", "text": text},
                },
            }
        )


@pytest.mark.parametrize("text", [None, "", {}, get_random_string(61)])
def test_when_footer_text_is_invalid__validation_error_is_raised(text):
    with pytest.raises(ValidationError):
        ListMessageBody(
            **{
                "from": "441134960000",
                "to": "38598451987",
                "content": {
                    "body": {"text": "test"},
                    "action": {
                        "title": "TEST",
                        "sections": [
                            {
                                "title": "My title",
                                "rows": [
                                    {
                                        "id": "123",
                                        "title": "title",
                                    }
                                ],
                            }
                        ],
                    },
                    "header": {"type": "TEXT", "text": "TEXT"},
                    "footer": {"text": text},
                },
            }
        )


def test_when_input_data_is_valid__validation_error_is_not_raised():
    try:
        ListMessageBody(
            **{
                "from": "441134960000",
                "to": "38598451987",
                "messageId": "a28dd97c-1ffb-4fcf-99f1-0b557ed381da",
                "content": {
                    "body": {"text": "Body text"},
                    "action": {
                        "title": "Action title",
                        "sections": [
                            {
                                "title": "section title",
                                "rows": [
                                    {
                                        "id": "1",
                                        "title": "row title",
                                        "description": "row description",
                                    }
                                ],
                            }
                        ],
                    },
                    "header": {"type": "TEXT", "text": "header text"},
                    "footer": {"text": "footer text"},
                },
            }
        )
    except ValidationError:
        pytest.fail("Unexpected ValidationError raised")
