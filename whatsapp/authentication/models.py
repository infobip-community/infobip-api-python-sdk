from pydantic import AnyHttpUrl, BaseModel


class Authentication(BaseModel):
    base_url: AnyHttpUrl
    api_key: str
