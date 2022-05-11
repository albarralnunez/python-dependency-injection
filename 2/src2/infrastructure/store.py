from typing import Any, List

from src2.domain.programmer import Programmer
from src2.domain.skill import Skill

store: [str, List[Any]] = {
    "programmers": [
        Programmer(name="Daniel", skills={Skill.PYTHON, Skill.SCALA}),
        Programmer(name="Manuel", skills={Skill.SCALA, Skill.PHP})
    ]
}
