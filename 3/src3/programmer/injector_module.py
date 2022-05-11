from injector import Binder, Module, singleton

from src3.programmer.application.programmer_finder import ProgrammerFinder
from src3.programmer.domain.programmer_repository import ProgrammerRepository
from src3.programmer.infrastructure.programmer_repository import ProgrammerRepositoryInMemImpl


class ProgrammerModule(Module):

    def configure(self, binder: Binder) -> None:
        binder.bind(ProgrammerFinder, scope=singleton)
        binder.bind(ProgrammerRepository, ProgrammerRepositoryInMemImpl)
