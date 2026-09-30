from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Agent Space"
    app_env: str = "development"
    secret_key: str = "change-this-secret-key"
    database_url: str = "sqlite:///./agent_space.db"
    openai_api_key: str = ""
    jwt_algorithm: str = "HS256"
    jwt_expire_minutes: int = 120

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
