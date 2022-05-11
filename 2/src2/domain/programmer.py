from dataclasses import dataclass
from typing import Set
from src2.domain.skill import Skill


@dataclass
class Programmer:
    name: str
    skills: Set[Skill]
