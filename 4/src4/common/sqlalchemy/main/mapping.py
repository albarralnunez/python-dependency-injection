import logging
from typing import Union

from sqlalchemy import MetaData, Table
from sqlalchemy.exc import ArgumentError
from sqlalchemy.orm import Mapper, mapper

logger = logging.getLogger(__name__)


class Mapping:
    def __init__(self, metadata: MetaData):
        self._metadata = metadata

    @property
    def table(self) -> Table:
        raise NotImplementedError

    @property
    def entity(self):
        raise NotImplementedError

    def create(self) -> Union[Mapper, None]:
        try:
            return mapper(self.entity, self.table)
        except ArgumentError:
            logger.error(f"{self.entity.__class__.__name__} already mapped")
        return None
