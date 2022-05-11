from dataclasses import dataclass
from typing import Set

from src4.common.shared.domain.aggregate import AggregateRoot
from src4.programmer.domain.skill import Skill


@dataclass
class Programmer(AggregateRoot):
    uuid: str
    name: str
    skills: Set[Skill]
