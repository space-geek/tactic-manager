""" Test Module Two
"""
from typing import Any
from typing import Dict

from tactics import TacticBaseClass



class Tactic2(TacticBaseClass):
    """ Tactic 2
    """
    name = "Do Tactic 2"

    @classmethod
    def handle_tactic(cls, data: Dict[str, Any]) -> Dict[str, Any]:
        print(f"Tactic 2: {data}")
        return {}
