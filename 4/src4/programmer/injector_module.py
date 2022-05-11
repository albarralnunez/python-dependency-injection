from injector import Binder, Module

from src4.programmer.application.programmer_finder import ProgrammerFinder
from src4.programmer.domain.programmer_repository import ProgrammerRepository
from src4.programmer.infrastructure.in_mem.programmer_repository_in_mem_impl import ProgrammerRepositoryInMemImpl
from src4.programmer.infrastructure.sqlalchemy.programmer_repository_sqlalchemy_impl import \
    ProgrammerRepositorySqlAlchemyImpl


class ProgrammerModule(Module):

    def configure(self, binder: Binder) -> None:
        binder.bind(ProgrammerFinder)
        # binder.bind(ProgrammerRepository, ProgrammerRepositoryInMemImpl)
        binder.bind(ProgrammerRepository, ProgrammerRepositorySqlAlchemyImpl)
