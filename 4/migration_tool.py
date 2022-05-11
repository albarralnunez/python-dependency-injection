from pathlib import Path

from src4.common.sqlalchemy.main.alembic import Alembic


def get_dir(file_path: Path) -> Path:
    return file_path.resolve().parent


def migrate(alembic: Alembic):
    migrations_dir = get_dir(Path(__file__)) / Path("migrations")
    alembic.migrate(migrations_dir)
