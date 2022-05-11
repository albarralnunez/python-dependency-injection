from abc import ABC
from typing import List

from src2.domain.programmer import Programmer
from src2.domain.skill import Skill


class ProgrammerRepository(ABC):

    def find_programmers_with_a_skill(self, skill: Skill) -> List[Programmer]: ...

