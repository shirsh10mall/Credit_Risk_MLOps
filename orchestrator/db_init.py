# orchestrator/db_init.py
import os
import time

from sqlalchemy import create_engine, text

POSTGRES_USER = os.getenv("POSTGRES_USER", "postgres")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "postgres")
POSTGRES_HOST = os.getenv("POSTGRES_HOST", "postgres")
POSTGRES_PORT = os.getenv("POSTGRES_PORT", "5432")

# Role we want to ensure exists
APP_USER = os.getenv("APP_USER", "mlops_user")
APP_PASSWORD = os.getenv("APP_PASSWORD", "mlops_pass")

# Databases owned by APP_USER
DATABASES = ["raw_data_db", "processed_data_db", "mlflow_tracking_db"]

# Connect as admin (default "postgres" user) to postgres system db
admin_engine = create_engine(
    f"postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/postgres",
    echo=True,
)


def ensure_user(conn):
    """Ensure application user exists with correct password."""
    result = conn.execute(
        text("SELECT 1 FROM pg_roles WHERE rolname = :name"),
        {"name": APP_USER},
    ).first()

    if not result:
        print(f"✅ Creating role: {APP_USER}")
        conn.execute(
            text(f"CREATE USER {APP_USER} WITH PASSWORD :pwd"), {"pwd": APP_PASSWORD}
        )
    else:
        print(f"⚡ Role {APP_USER} already exists, updating password")
        conn.execute(
            text(f"ALTER USER {APP_USER} WITH PASSWORD :pwd"), {"pwd": APP_PASSWORD}
        )


def ensure_databases(conn):
    """Ensure databases exist and are owned by APP_USER."""
    for db in DATABASES:
        result = conn.execute(
            text("SELECT 1 FROM pg_database WHERE datname = :name"),
            {"name": db},
        ).first()

        if not result:
            print(f"✅ Creating database: {db}")
            conn.execute(text(f"CREATE DATABASE {db} OWNER {APP_USER}"))
        else:
            print(f"⚡ Database {db} already exists, ensuring ownership")
            conn.execute(text(f"ALTER DATABASE {db} OWNER TO {APP_USER}"))


def init_postgres():
    with admin_engine.connect() as conn:
        conn = conn.execution_options(isolation_level="AUTOCOMMIT")
        ensure_user(conn)
        ensure_databases(conn)


if __name__ == "__main__":
    for i in range(10):
        try:
            init_postgres()
            break
        except Exception as e:
            print(f"⏳ Waiting for Postgres... ({i + 1}/10) - {e}")
            time.sleep(5)
