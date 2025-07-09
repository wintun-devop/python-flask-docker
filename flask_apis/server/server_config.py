class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    WRITE_DB_URI = "postgresql://user:pass@192.168.20.51/dbname"
    READ_DB_URI = "postgresql://user:pass@192.168.20.55/dbname"
    SECRET_KEY = "your-secret"
    JWT_SECRET_KEY = "your-jwt-secret"