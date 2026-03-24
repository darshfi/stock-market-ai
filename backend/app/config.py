"""
Configuration Management for Stock Market AI Assistant

This module handles all application settings including:
- Environment variables
- API keys
- Database configuration
- Application settings

Uses Pydantic Settings for validation and type safety.
"""

from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field, field_validator
from typing import List
import secrets


class Settings(BaseSettings):
    """
    Application Settings
    
    All settings are loaded from environment variables (.env file).
    Pydantic validates types and required fields automatically.
    """
    
    # ============================================
    # Application Settings
    # ============================================
    
    app_name: str = Field(
        default="Stock Market AI",
        description="Name of the application"
    )
    
    app_env: str = Field(
        default="development",
        description="Environment: development, production, testing"
    )
    
    debug: bool = Field(
        default=True,
        description="Enable debug mode (detailed error messages)"
    )
    
    # Secret key for JWT tokens and encryption
    # Generate with: openssl rand -hex 32
    secret_key: str = Field(
        default_factory=lambda: secrets.token_urlsafe(32),
        description="Secret key for security (auto-generated if not provided)"
    )
    
    # ============================================
    # Server Configuration
    # ============================================
    
    host: str = Field(
        default="0.0.0.0",
        description="Server host address"
    )
    
    port: int = Field(
        default=8000,
        description="Server port"
    )
    
    # ============================================
    # Database Configuration
    # ============================================
    
    database_url: str = Field(
        default="sqlite:///./data/stock_market.db",
        description="Database connection URL"
    )
    
    # ============================================
    # AI Service - Google Gemini
    # ============================================
    
    gemini_api_key: str = Field(
        ...,  # ... means this field is REQUIRED
        description="Google Gemini API key (REQUIRED)"
    )
    
    gemini_model: str = Field(
        default="gemini-1.5-flash",
        description="Gemini model to use"
    )
    
    gemini_temperature: float = Field(
        default=0.7,
        ge=0.0,  # Greater than or equal to 0
        le=2.0,  # Less than or equal to 2
        description="Temperature for AI responses (0-2, lower = more focused)"
    )
    
    gemini_max_tokens: int = Field(
        default=2048,
        gt=0,
        description="Maximum tokens in AI response"
    )
    
    # ============================================
    # Stock Market APIs
    # ============================================
    
    alpha_vantage_key: str = Field(
        ...,  # REQUIRED
        description="Alpha Vantage API key (REQUIRED)"
    )
    
    # NewsAPI is optional
    news_api_key: str = Field(
        default="",
        description="NewsAPI key (optional)"
    )
    
    # ============================================
    # News Scraping Settings
    # ============================================
    
    scrape_interval_minutes: int = Field(
        default=5,
        ge=1,
        le=60,
        description="How often to scrape news (in minutes)"
    )
    
    user_agent: str = Field(
        default="Mozilla/5.0 (compatible; StockBot/1.0)",
        description="User agent for web scraping"
    )
    
    max_news_age_hours: int = Field(
        default=24,
        ge=1,
        description="Maximum age of news to keep (in hours)"
    )
    
    # ============================================
    # CORS Settings (Cross-Origin Resource Sharing)
    # ============================================
    
    allowed_origins: List[str] = Field(
        default=["http://localhost:3000", "http://localhost:5173"],
        description="Allowed origins for CORS"
    )
    
    # ============================================
    # Rate Limiting
    # ============================================
    
    rate_limit_per_minute: int = Field(
        default=30,
        ge=1,
        description="Maximum API requests per minute per user"
    )
    
    # ============================================
    # Pydantic Settings Configuration
    # ============================================
    
    model_config = SettingsConfigDict(
        env_file=".env",           # Load from .env file
        env_file_encoding="utf-8", # UTF-8 encoding
        case_sensitive=False,      # GEMINI_API_KEY = gemini_api_key
        extra="ignore"             # Ignore extra fields in .env
    )
    
    # ============================================
    # Validators (Pydantic V2 style)
    # ============================================
    
    @field_validator("app_env")
    @classmethod
    def validate_environment(cls, v: str) -> str:
        """Ensure environment is valid"""
        allowed = ["development", "production", "testing"]
        if v.lower() not in allowed:
            raise ValueError(f"app_env must be one of: {allowed}")
        return v.lower()
    
    @field_validator("database_url")
    @classmethod
    def validate_database_url(cls, v: str) -> str:
        """Ensure database URL is properly formatted"""
        if not v.startswith(("sqlite://", "postgresql://", "mysql://")):
            raise ValueError("database_url must start with sqlite://, postgresql://, or mysql://")
        return v
    
    @field_validator("gemini_api_key", "alpha_vantage_key")
    @classmethod
    def validate_api_keys(cls, v: str) -> str:
        """Ensure API keys are not empty"""
        if not v or v.strip() == "":
            field_name = cls.model_fields.get(v, "API key")
            raise ValueError(f"API key cannot be empty. Please add it to your .env file")
        return v.strip()
    
    @field_validator("allowed_origins", mode="before")
    @classmethod
    def parse_allowed_origins(cls, v):
        """Parse ALLOWED_ORIGINS from comma-separated string or list"""
        if isinstance(v, str):
            # Split by comma and strip whitespace
            return [origin.strip() for origin in v.split(",") if origin.strip()]
        return v
    
    # ============================================
    # Helper Properties
    # ============================================
    
    @property
    def is_development(self) -> bool:
        """Check if running in development mode"""
        return self.app_env == "development"
    
    @property
    def is_production(self) -> bool:
        """Check if running in production mode"""
        return self.app_env == "production"
    
    @property
    def database_path(self) -> str:
        """Get database file path (for SQLite only)"""
        if self.database_url.startswith("sqlite:///"):
            return self.database_url.replace("sqlite:///", "")
        return ""
    
    def get_cors_config(self) -> dict:
        """Get CORS configuration for FastAPI"""
        return {
            "allow_origins": self.allowed_origins,
            "allow_credentials": True,
            "allow_methods": ["*"],
            "allow_headers": ["*"],
        }


# ============================================
# Create Settings Instance
# ============================================

# This will be imported by other modules
# It automatically loads from .env file when created
settings = Settings()


# ============================================
# Helper Function for Testing
# ============================================

def print_settings_info():
    """
    Print non-sensitive settings info (for debugging)
    NEVER print API keys or secrets!
    """
    print("=" * 50)
    print("Stock Market AI - Configuration")
    print("=" * 50)
    print(f"App Name: {settings.app_name}")
    print(f"Environment: {settings.app_env}")
    print(f"Debug Mode: {settings.debug}")
    print(f"Host: {settings.host}:{settings.port}")
    print(f"Database: {settings.database_url}")
    print(f"Gemini Model: {settings.gemini_model}")
    print(f"Gemini API Key: {'✓ Set' if settings.gemini_api_key else '✗ Missing'}")
    print(f"Alpha Vantage Key: {'✓ Set' if settings.alpha_vantage_key else '✗ Missing'}")
    print(f"NewsAPI Key: {'✓ Set' if settings.news_api_key else '✗ Optional'}")
    print(f"Scrape Interval: {settings.scrape_interval_minutes} minutes")
    print(f"CORS Origins: {', '.join(settings.allowed_origins)}")
    print("=" * 50)


# ============================================
# Test Configuration (when run directly)
# ============================================

if __name__ == "__main__":
    """
    Test the configuration by running:
    python -m app.config
    
    This will load .env and print settings (safely)
    """
    try:
        print_settings_info()
        print("\n✅ Configuration loaded successfully!")
        
        # Test helper properties
        print(f"\nIs Development? {settings.is_development}")
        print(f"Is Production? {settings.is_production}")
        
        if settings.database_path:
            print(f"Database Path: {settings.database_path}")
        
    except Exception as e:
        print(f"\n❌ Configuration Error: {e}")
        print("\nPlease check your .env file and ensure all required fields are set.")
        exit(1)