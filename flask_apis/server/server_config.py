import os
from dotenv import load_dotenv

#to get to ensure from .env
load_dotenv(override=True)

# server secret(app secret) key and jwt secret key
SERVER_SECRET=os.getenv("APP_SECRET_KEY")
JWT_SECRET=os.getenv("JWT_SECRET_KEY")


# getting data from env
db_name=os.getenv("DB_NAME")
db_user=os.getenv("DB_USER")
db_password=os.getenv("DB_PASSWORD")
db_host_write=os.getenv("DB_HOST_WRITE")
db_host_read=os.getenv("DB_HOST_READ")

#API Base Path
api_base_path=os.getenv("API_BASE_PATH")

class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # WRITE_DB_URI = "postgresql://user:pass@192.168.20.51/dbname"
    # READ_DB_URI = "postgresql://user:pass@192.168.20.55/dbname"
    SQLALCHEMY_DATABASE_URI = f"postgresql://{db_user}:{db_password}@{db_host_write}/{db_name}"
    SQLALCHEMY_BINDS ={
    'write': f"postgresql://{db_user}:{db_password}@{db_host_write}/{db_name}",
    'read': f"postgresql://{db_user}:{db_password}@{db_host_read}/{db_name}"
    }
    SECRET_KEY = SERVER_SECRET
    JWT_SECRET_KEY = JWT_SECRET