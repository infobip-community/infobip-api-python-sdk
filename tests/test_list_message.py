import pytest
from pydantic.error_wrappers import ValidationError

from tests.conftest import ListMessageBodyFactory, get_random_string
from whatsapp.models.core import MessageBody


def test_list_message_body__is_an_instance_of_message_body():
    assert isinstance(ListMessageBodyFactory.build(), MessageBody) is True


@pytest.mark.parametrize("content", [None, "", {}])
def test_when_content_is_invalid__validation_error_is_raised(content):
    with pytest.raises(ValidationError):
        ListMessageBodyFactory.build(**{"content": content})


@pytest.mark.parametrize("body", [None, "", {}])
def test_when_body_is_invalid__validation_error_is_raised(body):
    with pytest.raises(ValidationError):
        ListMessageBodyFactory.build(**{"content": {"body": body}})


@pytest.mark.parametrize("text", [None, "", {}, get_random_string(1025)])
def test_when_body_text_is_invalid__validation_error_is_raised(text):
    with pytest.raises(ValidationError):
        ListMessageBodyFactory.build(**{"content": {"body": {"text": text}}})


@pytest.mark.parametrize("action", [None, "", {}])
def test_when_action_is_invalid__validation_error_is_raised(action):
    with pytest.raises(ValidationError):
        ListMessageBodyFactory.build(
            **{"content": {"body": {"text": "test"}, "action": action}}
        )


@pytest.mark.parametrize(
    "sections",
    [
        None,
        "",
        {},
        [
            {
                "title": "My title",
                "rows": [{"id": "myId", "title": "T", "description": "Test"}],
            },
            {
                "title": "My title",
                "rows": [{"id": "myId", "title": "T", "description": "Test"}],
            },
            {
                "title": "My title",
                "rows": [{"id": "myId", "title": "T", "description": "Test"}],
            },
            {
                "title": "My title",
                "rows": [{"id": "myId", "title": "T", "description": "Test"}],
            },
            {
                "title": "My title",
                "rows": [{"id": "myId", "title": "T", "description": "Test"}],
            },
            {
                "title": "My title",
                "rows": [{"id": "myId", "title": "T", "description": "Test"}],
            },
            {
                "title": "My title",
                "rows": [{"id": "myId", "title": "T", "description": "Test"}],
            },
            {
                "title": "My title",
                "rows": [{"id": "myId", "title": "T", "description": "Test"}],
            },
            {
                "title": "My title",
                "rows": [{"id": "myId", "title": "T", "description": "Test"}],
            },
            {
                "title": "My title",
                "rows": [{"id": "myId", "title": "T", "description": "Test"}],
            },
            {
                "title": "My title",
                "rows": [{"id": "myId", "title": "T", "description": "Test"}],
            },
        ],
    ],
)
def test_when_action_sections_is_invalid__validation_error_is_raised(sections):
    with pytest.raises(ValidationError):
        ListMessageBodyFactory.build(
            **{
                "content": {
                    "body": {"text": "test"},
                    "action": {"title": "TEST", "sections": sections},
                }
            }
        )


@pytest.mark.parametrize("title", [None, "", {}])
def test_when_action_title_is_invalid__validation_error_is_raised(title):
    with pytest.raises(ValidationError):
        ListMessageBodyFactory.build(
            **{
                "content": {
                    "body": {"text": "Test"},
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
                }
            }
        )


@pytest.mark.parametrize("sections_id", [None, "", {}, get_random_string(201)])
def test_when_sections_id_is_invalid__validation_error_is_raised(sections_id):
    with pytest.raises(ValidationError):
        ListMessageBodyFactory.build(
            **{
                "content": {
                    "body": {"text": "test"},
                    "action": {
                        "title": "TEST",
                        "sections": [
                            {
                                "title": "My title",
                                "rows": [
                                    {
                                        "id": sections_id,
                                        "title": "TEST",
                                    }
                                ],
                            }
                        ],
                    },
                }
            }
        )


@pytest.mark.parametrize("rows", [None, "", {}])
def test_when_sections_rows_is_invalid__validation_error_is_raised(rows):
    with pytest.raises(ValidationError):
        ListMessageBodyFactory.build(
            **{
                "content": {
                    "body": {"text": "test"},
                    "action": {
                        "title": "TEST",
                        "sections": [{"title": "My title", "rows": rows}],
                    },
                }
            }
        )


@pytest.mark.parametrize("sections_title", [None, "", {}, get_random_string(25)])
def test_when_sections_title_is_invalid__validation_error_is_raised(sections_title):
    with pytest.raises(ValidationError):
        ListMessageBodyFactory.build(
            **{
                "content": {
                    "body": {"text": "test"},
                    "action": {
                        "title": "TEST",
                        "sections": [
                            {
                                "title": "My title",
                                "rows": [
                                    {
                                        "id": "1",
                                        "title": sections_title,
                                    }
                                ],
                            }
                        ],
                    },
                }
            }
        )


@pytest.mark.parametrize("header_type", [None, "", {}, "TEST"])
def test_when_header_type_is_invalid__validation_error_is_raised(header_type):
    with pytest.raises(ValidationError):
        ListMessageBodyFactory.build(
            **{
                "content": {
                    "body": {"text": "test"},
                    "action": {
                        "title": "TEST",
                        "sections": [
                            {
                                "title": "My title",
                                "rows": [
                                    {
                                        "id": "1",
                                        "title": "TEST",
                                    }
                                ],
                            }
                        ],
                    },
                    "header": {"type": header_type, "text": "TEST"},
                }
            }
        )


@pytest.mark.parametrize("text", [None, "", {}, get_random_string(61)])
def test_when_header_text_is_invalid__validation_error_is_raised(text):
    with pytest.raises(ValidationError):
        ListMessageBodyFactory.build(
            **{
                "content": {
                    "body": {"text": "test"},
                    "action": {
                        "title": "TEST",
                        "sections": [
                            {
                                "title": "My title",
                                "rows": [
                                    {
                                        "id": "1",
                                        "title": "TEST",
                                    }
                                ],
                            }
                        ],
                    },
                    "header": {"type": "TEXT", "text": text},
                }
            }
        )


@pytest.mark.parametrize("text", [None, "", {}, get_random_string(61)])
def test_when_footer_text_is_invalid__validation_error_is_raised(text):
    with pytest.raises(ValidationError):
        ListMessageBodyFactory.build(
            **{
                "content": {
                    "body": {"text": "test"},
                    "action": {
                        "title": "TEST",
                        "sections": [
                            {
                                "title": "My title",
                                "rows": [
                                    {
                                        "id": "1",
                                        "title": "TEST",
                                    }
                                ],
                            }
                        ],
                    },
                    "header": {"type": "TEXT", "text": "TEST"},
                    "footer": {"text": text},
                }
            }
        )
