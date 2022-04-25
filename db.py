import os
import databases
import sqlalchemy

DATABASE = "postgresql"
USER = os.environ["POSTGRES_USER"]
PASSWORD = os.environ["POSTGRES_PASSWORD"]
HOST = os.environ["POSTGRES_HOST"]
DB_NAME = os.environ["POSTGRES_DB"]

DATABASE_URL = "{}://{}:{}@postgres/{}".format(DATABASE,
                                               USER,
                                               PASSWORD,
                                               DB_NAME)


# databases
database = databases.Database(DATABASE_URL)

ECHO_LOG = False

engine = sqlalchemy.create_engine(DATABASE_URL, echo=ECHO_LOG)

metadata = sqlalchemy.MetaData()
