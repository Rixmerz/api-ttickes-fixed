"""
core/config.py
Carga de variables de entorno y configuración central de la API.

DATABASE_URL y COLECCION son obligatorias y se leen desde .env (o variables
de entorno en producción). No hay credenciales hardcodeadas: el .env no se
commitea. Ver .env.example para el formato.
"""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # Requeridas — definir en .env. La URI debe incluir el nombre de la base
    # (…/<db>) porque database.py usa get_default_database().
    DATABASE_URL: str
    COLECCION: str

    # Opcionales con default (sobrescribir en producción vía .env).
    SECRET_KEY: str = "dev-secret-change-me"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


settings = Settings()
