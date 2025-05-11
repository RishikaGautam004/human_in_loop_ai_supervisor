import os

class Config:
    DEBUG = True
    DATABASE_URL = os.getenv("DATABASE_URL", "firebase")
    AI_MODEL = os.getenv("AI_MODEL", "default")

config = Config()