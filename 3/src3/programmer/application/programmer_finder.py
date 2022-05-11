from dataclasses import dataclass
from typing import List

from injector import inject

from src3.programmer.domain.programmer_repository import ProgrammerRepository

from src3.programmer.domain.programmer import Programmer
from src3.programmer.domain.skill import Skill


@inject
@dataclass
class ProgrammerFinder:
    programmer_repository: ProgrammerRepository

    def __call__(self, skill: Skill) -> List[Programmer]:
        programmers: List[Programmer] = self.programmer_repository.find_programmers_with_a_skill(skill)
        return programmers
