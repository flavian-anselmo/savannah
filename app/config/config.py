from pydantic import BaseSettings

class Settings(BaseSettings):
    database_host: str 
    database_password:str
    database_name:str 
    database_username: str 
    secret_key:str 
    algorithm:str 
    twilio_account_sid:str
    twilio_auth_token:str
    class Config:
        env_file = ".env"

settings:Settings = Settings()