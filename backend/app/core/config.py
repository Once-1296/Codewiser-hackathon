"""Application configuration and environment settings."""

from __future__ import annotations

from functools import lru_cache

from pydantic import BaseModel, Field


class Settings(BaseModel):
    """Application settings with sensible development defaults."""

    app_name: str = Field(default="Cognitive-Aware Study Planner")
    app_version: str = Field(default="0.1.0")
    environment: str = Field(default="development")
    database_url: str = Field(default="sqlite:///./study_planner.db")


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    """Return a cached application settings object."""

    return Settings()

