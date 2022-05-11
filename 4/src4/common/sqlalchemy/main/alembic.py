from alembic.config import Config
from alembic.runtime.environment import EnvironmentContext
from alembic.script import ScriptDirectory
from sqlalchemy import MetaData
from sqlalchemy.engine import Engine
from sqlalchemy_utils import drop_database

from src4.common.sqlalchemy.main.settings.db_settings import DbSettings


class Alembic:
    def __init__(self, engine: Engine, db_settings: DbSettings, metadata: MetaData = None):
        self._engine = engine
        self._db_settings = db_settings
        self._metadata = metadata

    def migrate(self, migrations_dir):
        def _do_upgrade(revision, context):
            return alembic_script._upgrade_revs(alembic_script.get_heads(), revision)

        if not self._metadata:
            self._metadata = MetaData()
        alembic_cfg = Config()
        alembic_cfg.set_main_option("script_location", str(migrations_dir))
        alembic_script = ScriptDirectory.from_config(alembic_cfg)
        alembic_env = EnvironmentContext(alembic_cfg, alembic_script)
        conn = self._engine.connect()
        alembic_env.configure(connection=conn, target_metadata=self._metadata, fn=_do_upgrade)
        with alembic_env.begin_transaction():
            alembic_env.run_migrations()

    def drop_db(self):
        drop_database(self._db_settings.url)
