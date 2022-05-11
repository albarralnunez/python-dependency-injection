from sqlalchemy import Column, JSON, Table, TypeDecorator
from sqlalchemy.sql.sqltypes import STRINGTYPE

from src4.common.sqlalchemy.main.mapping import Mapping
from src4.programmer.domain.programmer import Programmer
from src4.programmer.domain.skill import Skill


class SkillType(TypeDecorator):
    impl = JSON

    @property
    def value_object_type(self):
        return Skill

    @property
    def python_type(self):
        return str

    def process_literal_param(self, value, dialect):
        ...

    def process_bind_param(self, value, dialect):
        return [x.value for x in value]

    def process_result_value(self, value, dialect):
        return [self.value_object_type(x) for x in value]


class ProgrammerTableMapping(Mapping):
    @property
    def table(self):
        return Table(
            "programmer",
            self._metadata,
            Column("uuid", STRINGTYPE, primary_key=True),
            Column("name", STRINGTYPE, nullable=False),
            Column("skills", SkillType, nullable=True),
        )

    @property
    def entity(self):
        return Programmer
