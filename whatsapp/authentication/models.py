from pydantic import AnyHttpUrl, BaseModel, constr


class Authentication(BaseModel):
    base_url: AnyHttpUrl
    api_key: constr(min_length=1)
