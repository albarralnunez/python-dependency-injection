from typing import List, Sequence, Type, Union

from sqlalchemy import MetaData
from sqlalchemy.orm import Mapper

from src4.common.sqlalchemy.main.mapping import Mapping


class SqlAlchemyMapper:
    def __init__(self, mappings: Sequence[Type[Mapping]], metadata: MetaData):
        self._mappings = [mapping(metadata) for mapping in mappings]
        self._mappers: Union[List[Mapper], None] = None

    def load(self):
        self._mappers = [mapping.create() for mapping in self._mappings]
