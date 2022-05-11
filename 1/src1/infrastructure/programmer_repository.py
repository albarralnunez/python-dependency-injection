from typing import Any, Dict, List

from src1.domain.programmer import Programmer
from src1.domain.skill import Skill
from src1.infrastructure.store import store


class ProgrammerRepository:
    store: Dict[str, Any]

    def find_programmers_with_a_skill(self, skill: Skill) -> List[Programmer]:
        programmers: List[Programmer] = store["programmers"]
        result = filter(lambda x: skill in x.skills, programmers)
        return list(result)
