from dataclasses import dataclass
from typing import Set
from src3.programmer.domain.skill import Skill


@dataclass
class Programmer:
    name: str
    skills: Set[Skill]
