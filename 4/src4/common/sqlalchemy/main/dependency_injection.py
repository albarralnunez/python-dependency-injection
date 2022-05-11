from dataclasses import dataclass
from typing import Sequence, Type
from uuid import uuid4

from injector import Module, provider, singleton
from sqlalchemy import MetaData, create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy_utils import create_database, database_exists

from src4.common.injector_ext.main.module_types import CleanUp, CloseConnection, DBModuleT
from src4.common.injector_ext.main.request_scope import request
from src4.common.sqlalchemy.main.mapper import SqlAlchemyMapper
from src4.common.sqlalchemy.main.mapping import Mapping
from src4.common.sqlalchemy.main.settings.db_settings import DbSettings


@dataclass
class SqlAlchemyModule(Module, DBModuleT):
    settings: str
    mappings: Sequence[Type[Mapping]]

    @singleton
    @provider
    def db_settings(self) -> DbSettings:
        db_settings = DbSettings(self.settings)
        if db_settings.testing:
            db_settings.url = f"{db_settings.url}-{uuid4()[-8:]}"
        return db_settings

    @singleton
    @provider
    def engine(self, db_settings: DbSettings, metadata: MetaData) -> Engine:
        if not database_exists(db_settings.url):
            create_database(db_settings.url)
        engine = create_engine(db_settings.url)
        metadata.bind = engine
        mapper = SqlAlchemyMapper(mappings=self.mappings, metadata=metadata)
        mapper.load()
        return engine

    @provider
    def close_database(self, session: Session, engine: Engine) -> CloseConnection:
        session.close()
        engine.dispose()
        return CloseConnection()

    @provider
    def clean_up(self, metadata: MetaData, engine: Engine) -> CleanUp:
        for tbl in reversed(metadata.sorted_tables):
            engine.execute(tbl.delete())
        return CleanUp()

    @singleton
    @provider
    def metadata(self) -> MetaData:
        metadata = MetaData()
        return metadata

    @request
    @provider
    def session(self, engine: Engine) -> Session:
        session_factory = sessionmaker(bind=engine, autoflush=False)
        session: Session = session_factory()
        return session
