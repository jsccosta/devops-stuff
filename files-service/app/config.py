import os

def get_database_url():
    return "postgresql://root:root@localhost/silastech"
    # return "postgresql://root:root@silas-database-srv/silastech"


class Config:
    # DB_USER = os.getenv("DB_USER", "root")
    # DB_PASSWORD = os.getenv("DB_PASSWORD", "root")
    # # DB_HOST = os.getenv("DB_HOST", "localhost:5432")
    # DB_HOST = os.getenv("DB_HOST", get_database_url())
    # DB_NAME = os.getenv("DB_NAME", "silastech")
    # DB_CONFIG = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
    DB_CONFIG = get_database_url()

config = Config
