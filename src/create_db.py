import logging.config
from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
import sys



#logging.config.fileConfig(config.LOGGING_CONFIG)
logger = logging.getLogger(__name__)


Base = declarative_base()


class user_input(Base):
    """ Defines the data model for the table user_input"""
    __tablename__ = 'user_input'
    id = Column(String(100), primary_key=True, unique=True, nullable=False)
    age = Column(Integer, unique=False, nullable=False)
    overall = Column(Integer, unique=False, nullable=False)
    potential = Column(Integer, unique=False, nullable=False)
    position = Column(String(10), unique=False, nullable=False)
    wage = Column(Integer, unique=False, nullable=False)
    contract_expiry = Column(String(100), unique = False, nullable = True)
    international_reputation = Column(Integer, unique=False, nullable=False)



    def __repr__(self):
        player_repr = "<Player(id='%s', age='%d', overall='%d', potential='%d', position='%s'," \
                      " wage='%d', contract_expiry='%s',international_reputation='%d' )>"
        return player_repr % (self.id, self.age, self.overall, self.potential,
                              self.position, self.wage, self.contract_expiry, self.international_reputation)


def create_db_sql(args):
    """Creates a SQLITE database (based on configuration) with User inputs table.
    Returns: Optional user argument with sql engine
    """
    try:

        engine = create_engine(args.engine_string)
        logger.info("Creating sqlite database")

        #Base.metadata.drop_all(engine)
        Base.metadata.create_all(engine)
        logger.info("Database created with tables")
    except Exception as e:
        logger.error(e)
        sys.exit(1)


def create_db_rds(args):
    """
    Creates a RDS database (based on configuration) with User inputs table.

    :param args: User input with username and password credentials
    :return:
    """
    rds_config = args.config
    conn_type = rds_config["type"]
    host = rds_config["host"]
    port = rds_config["port"]
    database = rds_config["dbname"]
    user = args.user
    password = args.password
    engine_string = "{}://{}:{}@{}:{}/{}". \
        format(conn_type, user, password, host, port, database)
    try:

        engine = create_engine(engine_string)
        logger.info("Creating RDS database")
        #Base.metadata.drop_all(engine)
        Base.metadata.create_all(engine)
        logger.info("Database created with tables")
    except Exception as e:
        logger.error(e)
        sys.exit(1)


