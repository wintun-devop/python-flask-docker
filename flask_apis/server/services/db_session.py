from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from server_config import Config

write_engine = create_engine(Config.WRITE_DB_URI)
read_engine = create_engine(Config.READ_DB_URI)

WriteSession = scoped_session(sessionmaker(bind=write_engine))
ReadSession = scoped_session(sessionmaker(bind=read_engine))

def get_session(operation="read"):
    return WriteSession() if operation == "write" else ReadSession()