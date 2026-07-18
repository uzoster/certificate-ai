import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATABASE_URL = "sqlite:///./certificate.db"

SECRET_KEY = "certificate_ai_secret"

ALGORITHM = "HS256"