from abc import abstractmethod
from datetime import datetime

from sqlalchemy import DateTime, Text, TypeDecorator


class ValueObjectAbstractType(TypeDecorator):
    @property
    @abstractmethod
    def value_object_type(self):
        raise NotImplementedError


class ValueObjectStrType(ValueObjectAbstractType):
    impl = Text

    @property
    def value_object_type(self):
        return str

    @property
    def python_type(self):
        return str

    def process_literal_param(self, value, dialect):
        ...

    def process_bind_param(self, value, dialect):
        return value.value

    def process_result_value(self, value, dialect):
        return self.value_object_type(value)


class ValueObjectDateType(ValueObjectAbstractType):
    impl = DateTime

    @property
    def value_object_type(self):
        return datetime

    @property
    def python_type(self):
        return datetime

    def process_literal_param(self, value, dialect):
        ...

    def process_bind_param(self, value, dialect):
        return value.value

    def process_result_value(self, value, dialect):
        return self.value_object_type(value)
