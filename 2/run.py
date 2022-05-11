from pprint import pprint

from src2.application.programmer_finder import ProgrammerFinder
from src2.domain.skill import Skill
from src2.infrastructure.programmer_repository import ProgrammerRepositoryInMemImpl
from src2.infrastructure.store import store

print("Application State:")
pprint(store)

programmer_repository = ProgrammerRepositoryInMemImpl()

print("\n", "Find all programmers that know Python ...", "\n")
programmer_finder = ProgrammerFinder(programmer_repository=programmer_repository)
result = programmer_finder(Skill.PYTHON)

print("Operation Results:")
pprint(result)
