AUTH_KEY_NEW = "overwrite_auth_key"

from pydantic_settings import BaseSettings
from pydantic import Field, BaseModel, AliasChoices
import os

os.environ["AUTH_KEY_NEW"] = AUTH_KEY_NEW

class Settings(BaseSettings):
    auth_key: str = Field(AliasChoices=["AUTH_KEY_NEW", "AUTH_KEY"])
    api_key: str = Field(...)
    
setting = Settings()

print(setting.auth_key, setting.api_key)