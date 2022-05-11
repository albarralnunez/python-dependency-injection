from dataclasses import dataclass
from typing import List

from injector import inject
from sqlalchemy.orm import Session

from src4.common.sqlalchemy.main.sqlalchemy_client import SqlalchemyClient
from src4.programmer.domain.programmer import Programmer
from src4.programmer.domain.programmer_repository import ProgrammerRepository
from src4.programmer.domain.skill import Skill


@inject
@dataclass
class ProgrammerRepositorySqlAlchemyImpl(ProgrammerRepository):
    session: Session

    def __post_init__(self):
        self.sqlalchemy_client = SqlalchemyClient(session=self.session, aggregate=Programmer)

    def find_programmers_with_a_skill(self, skill: Skill) -> List[Programmer]:
        print(f"Using sqlalchemy repository")
        programmers: List[Programmer] = self.sqlalchemy_client.all()
        result = filter(lambda x: skill in x.skills, programmers)
        return list(result)
