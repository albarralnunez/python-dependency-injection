from typing import Any, Dict, List

from src2.domain.programmer import Programmer
from src2.domain.programmer_repository import ProgrammerRepository
from src2.domain.skill import Skill
from src2.infrastructure.store import store


class ProgrammerRepositoryInMemImpl(ProgrammerRepository):
    store: Dict[str, Any]

    def find_programmers_with_a_skill(self, skill: Skill) -> List[Programmer]:
        programmers: List[Programmer] = store["programmers"]
        result = filter(lambda x: skill in x.skills, programmers)
        return list(result)
