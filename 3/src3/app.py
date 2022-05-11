from dataclasses import dataclass
from pprint import pprint

from injector import inject

from src3.programmer.application.programmer_finder import ProgrammerFinder
from src3.programmer.domain.skill import Skill
from src3.programmer.infrastructure.store import store


@inject
@dataclass
class App:
    programmer_finder: ProgrammerFinder

    def __call__(self):
        print("Application State:")
        pprint(store)

        print("\n", "Find all programmers that know Python ...", "\n")
        result = self.programmer_finder(Skill.PYTHON)

        print("Operation Results:")
        pprint(result)
