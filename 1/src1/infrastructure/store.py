from typing import Any, List

from src1.domain.programmer import Programmer
from src1.domain.skill import Skill

store: [str, List[Any]] = {
    "programmers": [
        Programmer(name="Daniel", skills={Skill.PYTHON, Skill.SCALA}),
        Programmer(name="Manuel", skills={Skill.SCALA, Skill.PHP})
    ]
}
