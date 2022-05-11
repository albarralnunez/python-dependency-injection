from dataclasses import dataclass
from typing import List

from src2.domain.programmer_repository import ProgrammerRepository

from src2.domain.programmer import Programmer
from src2.domain.skill import Skill


@dataclass
class ProgrammerFinder:
    programmer_repository: ProgrammerRepository

    def __call__(self, skill: Skill) -> List[Programmer]:
        programmers: List[Programmer] = self.programmer_repository.find_programmers_with_a_skill(skill)
        return programmers
