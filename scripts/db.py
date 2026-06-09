from sqlalchemy import create_engine
from config import DB_CONFIG

def get_engine():
    engine = create_engine(
        f"postgresql+psycopg2://{DB_CONFIG['user']}@"
        f"{DB_CONFIG['host']}:{DB_CONFIG['port']}/"
        f"{DB_CONFIG['database']}"
    )
    return engine