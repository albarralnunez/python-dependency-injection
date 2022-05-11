from abc import ABCMeta
from asyncio import Future
from typing import Type, List

from sqlalchemy.orm import Query, Session

from src4.common.shared.domain.aggregate import AggregateRoot


class SqlalchemyClient(metaclass=ABCMeta):

    def __init__(self, session: Session, aggregate: Type[AggregateRoot]):
        self._session = session
        self._aggregate = aggregate

    @property
    def aggregate(self):
        return self._aggregate

    @property
    def _query(self) -> Query:
        return self._session.query(self.aggregate)

    def persist(self, entity: AggregateRoot):
        self._session.add(entity)
        self._session.flush()

    def delete(self, entity: AggregateRoot):
        self._session.delete(entity)

    def all(self) -> List[AggregateRoot]:
        return self._query.all()
