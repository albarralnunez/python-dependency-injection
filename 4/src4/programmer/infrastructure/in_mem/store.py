from typing import Any, List

from src4.programmer.domain.programmer import Programmer
from src4.programmer.domain.skill import Skill

store: [str, List[Any]] = {
    "programmers": [
        Programmer(uuid="", name="Daniel", skills={Skill.PYTHON, Skill.SCALA}),
        Programmer(uuid="", name="Manuel", skills={Skill.SCALA, Skill.PHP})
    ]
}
