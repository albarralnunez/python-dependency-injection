from typing import List

from src1.domain.programmer import Programmer
from src1.domain.skill import Skill
from src1.infrastructure.programmer_repository import ProgrammerRepository


class ProgrammerFinder:

    def __call__(self, skill: Skill) -> List[Programmer]:
        programmer_repository = ProgrammerRepository()
        programmers: List[Programmer] = programmer_repository.find_programmers_with_a_skill(skill)
        return programmers
