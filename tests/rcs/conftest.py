from pydantic_factories import ModelFactory

from infobip_channels.rcs.Models.body.send_rcs import RcsMessageBody
from infobip_channels.rcs.Models.body.send_bulk_rcs import RcsMessageBodyList


class RcsMessageBodyFactory(ModelFactory):
    __model__ = RcsMessageBody

    @classmethod
    def build(cls, *args, **kwargs):
        """Needed because factory classes don't play well with custom validation."""
        return RcsMessageBody(
            **{
                "from": "myRcsSender",
                "to": "385977666618",
                "validityPeriod": 15,
                "validityPeriodTimeUnit": "MINUTES",
                "content": {
                    "text": "exampleText",
                    "suggestions": [
                        {
                            "text": "exampleText",
                            "postbackData": "examplePostbackData",
                            "type": "REPLY"
                        },
                        {
                            "text": "exampleText",
                            "postbackData": "examplePostbackData",
                            "url": "http://www.example.test",
                            "type": "OPEN_URL"
                        },
                        {
                            "text": "exampleText",
                            "postbackData": "examplePostbackData",
                            "phoneNumber": "385977666618",
                            "type": "DIAL_PHONE"
                        },
                        {
                            "text": "exampleText",
                            "postbackData": "examplePostbackData",
                            "latitude": 45.793418,
                            "longitude": 15.946297,
                            "label": "label",
                            "type": "SHOW_LOCATION"
                        },
                        {
                            "text": "exampleText",
                            "postbackData": "examplePostbackData",
                            "type": "REQUEST_LOCATION"
                        }
                    ],
                    "type": "TEXT"
                },
                "notifyUrl": "https://www.example.com/rcs",
                "callbackData": "Callback data",
                "messageId": "externalMessageId"
            }
        )


class RcsMessageBodyListFactory(ModelFactory):
    __model__ = RcsMessageBodyList

    @classmethod
    def build(cls, *args, **kwargs):
        """Needed because factory classes don't play well with custom validation."""
        return RcsMessageBodyList(
            **{
                "messages": [
                    {
                        "from": "myRcsSender1",
                        "to": "385977666618",
                        "validityPeriod": 15,
                        "validityPeriodTimeUnit": "MINUTES",
                        "content": {
                            "text": "exampleText1",
                            "suggestions": [
                                {
                                    "text": "exampleText1",
                                    "postbackData": "examplePostbackData",
                                    "type": "REPLY"
                                },
                                {
                                    "text": "exampleText1",
                                    "postbackData": "examplePostbackData",
                                    "url": "http://www.example.test",
                                    "type": "OPEN_URL"
                                },
                                {
                                    "text": "exampleText1",
                                    "postbackData": "examplePostbackData",
                                    "phoneNumber": "385977666618",
                                    "type": "DIAL_PHONE"
                                },
                                {
                                    "text": "exampleText1",
                                    "postbackData": "examplePostbackData",
                                    "latitude": 45.793418,
                                    "longitude": 15.946297,
                                    "label": "label",
                                    "type": "SHOW_LOCATION"
                                },
                                {
                                    "text": "exampleText1",
                                    "postbackData": "examplePostbackData",
                                    "type": "REQUEST_LOCATION"
                                }
                            ],
                            "type": "TEXT"
                        },
                        "notifyUrl": "https://www.example.com/rcs",
                        "callbackData": "Callback data",
                        "messageId": "externalMessageId"
                    },
                    {
                        "from": "myRcsSender2",
                        "to": "385977666618",
                        "validityPeriod": 15,
                        "validityPeriodTimeUnit": "MINUTES",
                        "content": {
                            "text": "exampleText2",
                            "suggestions": [
                                {
                                    "text": "exampleText2",
                                    "postbackData": "examplePostbackData",
                                    "type": "REPLY"
                                },
                                {
                                    "text": "exampleText2",
                                    "postbackData": "examplePostbackData",
                                    "url": "http://www.example.test",
                                    "type": "OPEN_URL"
                                },
                                {
                                    "text": "exampleText2",
                                    "postbackData": "examplePostbackData",
                                    "phoneNumber": "385977666618",
                                    "type": "DIAL_PHONE"
                                },
                                {
                                    "text": "exampleText2",
                                    "postbackData": "examplePostbackData",
                                    "latitude": 45.793418,
                                    "longitude": 15.946297,
                                    "label": "label",
                                    "type": "SHOW_LOCATION"
                                },
                                {
                                    "text": "exampleText2",
                                    "postbackData": "examplePostbackData",
                                    "type": "REQUEST_LOCATION"
                                }
                            ],
                            "type": "TEXT"
                        },
                        "notifyUrl": "https://www.example.com/rcs",
                        "callbackData": "Callback data",
                        "messageId": "externalMessageId"
                    }
                ]
            }
        )


def get_rcs_body_send_message():
    return {
        "from": "myRcsSender",
        "to": "385977666618",
        "validityPeriod": 15,
        "validityPeriodTimeUnit": "MINUTES",
        "content": {
            "text": "exampleText",
            "suggestions": [
                {
                    "text": "exampleText",
                    "postbackData": "examplePostbackData",
                    "type": "REPLY"
                },
                {
                    "text": "exampleText",
                    "postbackData": "examplePostbackData",
                    "url": "http://www.example.test",
                    "type": "OPEN_URL"
                },
                {
                    "text": "exampleText",
                    "postbackData": "examplePostbackData",
                    "phoneNumber": "385977666618",
                    "type": "DIAL_PHONE"
                },
                {
                    "text": "exampleText",
                    "postbackData": "examplePostbackData",
                    "latitude": 45.793418,
                    "longitude": 15.946297,
                    "label": "label",
                    "type": "SHOW_LOCATION"
                },
                {
                    "text": "exampleText",
                    "postbackData": "examplePostbackData",
                    "type": "REQUEST_LOCATION"
                }
            ],
            "type": "TEXT"
        },
        "notifyUrl": "https://www.example.com/rcs",
        "callbackData": "Callback data",
        "messageId": "externalMessageId"
    }


def get_rcs_body_send_bulk_message():
    return {
        "messages": [
            {
                "from": "myRcsSender1",
                "to": "385977666618",
                "validityPeriod": 15,
                "validityPeriodTimeUnit": "MINUTES",
                "content": {
                    "text": "exampleText1",
                    "suggestions": [
                        {
                            "text": "exampleText1",
                            "postbackData": "examplePostbackData",
                            "type": "REPLY"
                        },
                        {
                            "text": "exampleText1",
                            "postbackData": "examplePostbackData",
                            "url": "http://www.example.test",
                            "type": "OPEN_URL"
                        },
                        {
                            "text": "exampleText1",
                            "postbackData": "examplePostbackData",
                            "phoneNumber": "385977666618",
                            "type": "DIAL_PHONE"
                        },
                        {
                            "text": "exampleText1",
                            "postbackData": "examplePostbackData",
                            "latitude": 45.793418,
                            "longitude": 15.946297,
                            "label": "label",
                            "type": "SHOW_LOCATION"
                        },
                        {
                            "text": "exampleText1",
                            "postbackData": "examplePostbackData",
                            "type": "REQUEST_LOCATION"
                        }
                    ],
                    "type": "TEXT"
                },
                "notifyUrl": "https://www.example.com/rcs",
                "callbackData": "Callback data",
                "messageId": "externalMessageId"
            },
            {
                "from": "myRcsSender2",
                "to": "385977666618",
                "validityPeriod": 15,
                "validityPeriodTimeUnit": "MINUTES",
                "content": {
                    "text": "exampleText2",
                    "suggestions": [
                        {
                            "text": "exampleText2",
                            "postbackData": "examplePostbackData",
                            "type": "REPLY"
                        },
                        {
                            "text": "exampleText2",
                            "postbackData": "examplePostbackData",
                            "url": "http://www.example.test",
                            "type": "OPEN_URL"
                        },
                        {
                            "text": "exampleText2",
                            "postbackData": "examplePostbackData",
                            "phoneNumber": "385977666618",
                            "type": "DIAL_PHONE"
                        },
                        {
                            "text": "exampleText2",
                            "postbackData": "examplePostbackData",
                            "latitude": 45.793418,
                            "longitude": 15.946297,
                            "label": "label",
                            "type": "SHOW_LOCATION"
                        },
                        {
                            "text": "exampleText2",
                            "postbackData": "examplePostbackData",
                            "type": "REQUEST_LOCATION"
                        }
                    ],
                    "type": "TEXT"
                },
                "notifyUrl": "https://www.example.com/rcs",
                "callbackData": "Callback data",
                "messageId": "externalMessageId"
            }
        ]
    }


def send_rcs_message_response():
    return {
        "messages": [
            {
                "to": "385977666618",
                "messageCount": 1,
                "messageId": "06df139a-7eb5-4a6e-902e-40e892210455",
                "status": {
                    "groupId": 1,
                    "groupName": "PENDING",
                    "id": 7,
                    "name": "PENDING_ENROUTE",
                    "description": "Message sent to next instance",
                    "action": "string"
                }
            }
        ]
    }


def send_rcs_bulk_message_response():
    return [
            {
                "messages": [
                    {
                        "to": "385977666618",
                        "messageCount": 1,
                        "messageId": "06df139a-7eb5-4a6e-902e-40e892210455",
                        "status": {
                            "groupId": 1,
                            "groupName": "PENDING",
                            "id": 7,
                            "name": "PENDING_ENROUTE",
                            "description": "Message sent to next instance",
                            "action": "string"
                        }
                    }
                ]
            },
            {
                "messages": [
                    {
                        "to": "385977666618",
                        "messageCount": 2,
                        "messageId": "06df139a-7eb5-4a6e-902e-40e892210455",
                        "status": {
                            "groupId": 1,
                            "groupName": "PENDING",
                            "id": 8,
                            "name": "PENDING_ENROUTE",
                            "description": "Message sent to next instance",
                            "action": "string"
                        }
                    }
                ]
            }
        ]



def rcs_error_response():
    return {
        "requestError": {
            "serviceException": {
                "messageId": "06df139a-7eb5-4a6e-902e-40e892210455",
                "text": "Bad request",
                "validationErrors": {
                    "request.message.content.media.file.url": [
                        "is not a valid url",
                    ]
                },
            }
        }
    }
