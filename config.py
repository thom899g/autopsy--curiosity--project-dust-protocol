"""
Configuration management for Project Dust Protocol
Uses Pydantic for validation and environment variable handling
"""
import os
from typing import Optional
from pydantic import BaseSettings, Field
from dotenv import load_dotenv

load_dotenv()

class ProtocolConfig(BaseSettings):
    """Project Dust Protocol Configuration"""
    
    # Firebase Configuration
    firebase_project_id: str = Field(..., env="FIREBASE_PROJECT_ID")
    firebase_private_key: str = Field(..., env="FIREBASE_PRIVATE_KEY")
    firebase_client_email: str = Field(..., env="FIREBASE_CLIENT_EMAIL")
    
    # AI Model Configuration (DeepSeek)
    deepseek_api_key: Optional[str] = Field(None, env="DEEPSEEK_API_KEY")
    deepseek_base_url: str = Field("https://api.deepseek.com/v1", env="DEEPSEEK_BASE_URL")
    
    # Protocol Behavior
    max_retries: int = Field(3, env="MAX_RETRIES")
    retry_delay: int = Field(5, env="RETRY_DELAY")
    batch_size: int = Field(10, env="BATCH_SIZE")
    
    # Database Paths
    dust_collection: str = Field("dust_protocol", env="DUST_COLLECTION")
    tasks_subcollection: str = Field("pending_tasks", env="TASKS_SUBCOLLECTION")
    
    # Logging
    log_level: str = Field("INFO", env="LOG_LEVEL")
    
    class Config:
        env_file = ".env"
        case_sensitive = False

# Global configuration instance
config = ProtocolConfig()