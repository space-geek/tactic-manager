""" Test Module 1
"""
from typing import Any
from typing import Dict

from tactics import TacticBaseClass



class Tactic1(TacticBaseClass):
    """ Tactic 1
    """
    name = "Do Tactic 1"

    @classmethod
    def handle_tactic(cls, data: Dict[str, Any]) -> Dict[str, Any]:
        print(f"Tactic 1: {data}")
        return {}


class Tactic3(TacticBaseClass):
    """ Tactic 3
    """
    name = "Do Tactic 3"

    @classmethod
    def handle_tactic(cls, data: Dict[str, Any]) -> Dict[str, Any]:
        print(f"Tactic 3: {data}")
        return {}
