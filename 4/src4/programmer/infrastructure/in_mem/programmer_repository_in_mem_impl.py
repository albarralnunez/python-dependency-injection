from typing import Any, Dict, List

from src4.programmer.domain.programmer import Programmer
from src4.programmer.domain.programmer_repository import ProgrammerRepository
from src4.programmer.domain.skill import Skill
from src4.programmer.infrastructure.in_mem.store import store


class ProgrammerRepositoryInMemImpl(ProgrammerRepository):
    store: Dict[str, Any]

    def find_programmers_with_a_skill(self, skill: Skill) -> List[Programmer]:
        print(f"Using in-mem repository")
        programmers: List[Programmer] = store["programmers"]
        result = filter(lambda x: skill in x.skills, programmers)
        return list(result)
