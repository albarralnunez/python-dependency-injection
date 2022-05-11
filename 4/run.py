from injector import Injector

from src4.app import App
from src4.common.sqlalchemy.main.dependency_injection import SqlAlchemyModule
from src4.programmer.infrastructure.sqlalchemy.programmer_mapper import ProgrammerTableMapping
from src4.programmer.injector_module import ProgrammerModule

injector = Injector(modules=[
    SqlAlchemyModule(mappings=[ProgrammerTableMapping], settings="db"),
    ProgrammerModule(),
])
app = injector.get(App)
app()
