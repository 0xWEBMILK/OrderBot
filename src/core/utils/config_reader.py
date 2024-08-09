from pydantic import SecretStr, BaseModel
from decouple import config
from enum import Enum


# Logs settings
class ModeEnum(str, Enum):
    DEVELOPMENT = "dev"
    PRODUCTION = "prod"


class LoggingRenderer(str, Enum):
    JSON = "json"
    CONSOLE = "console"


class LoggingSettings(BaseModel):

    level: str = "INFO"
    format: str = "%Y-%m-%d %H:%M:%S"
    is_utc: bool = False

    renderer: LoggingRenderer = LoggingRenderer.JSON
    log_unhandled: bool = False

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'
        env_prefix = "LOGGING_"


# Main settings
class MainSettings(BaseModel):

    # Telegram
    token: SecretStr = SecretStr(config('TOKEN'))

    # Saves file
    file_path: SecretStr = SecretStr(config('DUMP_PATH'))
    file_name: SecretStr = SecretStr(config('DUMP_NAME'))


    # .env path
    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


# Exporting the settings
main_settings = MainSettings()
log_settings = LoggingSettings()