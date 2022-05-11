from pprint import pprint

from src1.application.programmer_finder import ProgrammerFinder
from src1.domain.skill import Skill
from src1.infrastructure.store import store

print("Application State:")
pprint(store)

print("\n", "Find all programmers that know Python ...", "\n")
programmer_finder = ProgrammerFinder()
result = programmer_finder(Skill.PYTHON)

print("Operation Results:")
pprint(result)
