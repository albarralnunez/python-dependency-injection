from injector import Injector

from src3.app import App
from src3.programmer.application.programmer_finder import ProgrammerFinder
from src3.programmer.domain.programmer_repository import ProgrammerRepository
from src3.programmer.injector_module import ProgrammerModule

injector = Injector(modules=[ProgrammerModule()])
app = injector.get(App)
app()

message = "\nThe injector returned the same instance "

programmer_finder_1 = injector.get(ProgrammerFinder)
programmer_finder_2 = injector.get(ProgrammerFinder)
result = programmer_finder_1 is programmer_finder_2
print(f"{message} for ProgrammerFinder? {result}")

repository_1 = injector.get(ProgrammerRepository)
repository_2 = injector.get(ProgrammerRepository)
result = repository_1 is repository_2
print(f"{message} for ProgrammerRepository? {result}")


