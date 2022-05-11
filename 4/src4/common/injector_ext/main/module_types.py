from abc import ABCMeta, abstractmethod



class CloseConnection:
    ...


class CleanUp:
    ...


class DBModuleT(metaclass=ABCMeta):

    @abstractmethod
    def close_database(self) -> CloseConnection:
        ...

    @abstractmethod
    def clean_up(self) -> CleanUp:
        ...
