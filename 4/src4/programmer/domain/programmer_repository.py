import abc
from abc import ABC
from typing import List

from src4.programmer.domain.programmer import Programmer
from src4.programmer.domain.skill import Skill


class ProgrammerRepository(ABC):
    @abc.abstractmethod
    def find_programmers_with_a_skill(self, skill: Skill) -> List[Programmer]: ...
