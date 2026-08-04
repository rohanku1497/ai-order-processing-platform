from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # Application
    APP_NAME: str = "AI Order Processing Platform"
    APP_VERSION: str = "1.0.0"
    ENVIRONMENT: str = "development"

    # OpenAI
    OPENAI_API_KEY: str
    OPENAI_MODEL: str = "gpt-4.1-mini"

    # Database
    DATABASE_URL: str

    # Qdrant
    QDRANT_URL: str
    QDRANT_API_KEY: str = ""

    # AWS
    AWS_REGION: str
    S3_BUCKET_NAME: str
    AWS_ACCESS_KEY_ID: str
    AWS_SECRET_ACCESS_KEY: str

    # Logging
    LOG_LEVEL: str = "INFO"

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=True
    )


settings = Settings()