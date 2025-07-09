from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from server.server_config import Config

write_engine = create_engine(Config.SQLALCHEMY_BINDS["write"])
read_engine = create_engine(Config.SQLALCHEMY_BINDS["read"])

WriteSession = scoped_session(sessionmaker(bind=write_engine))
ReadSession = scoped_session(sessionmaker(bind=read_engine))

db_read_session = WriteSession()
db_write_session = ReadSession()

def get_session(operation="read"):
    return WriteSession() if operation == "write" else ReadSession()


