#pylint:disable=missing-module-docstring
from abc import ABC
from abc import ABCMeta
from abc import abstractmethod
from typing import Any
from typing import Dict
from typing import List



class TacticBaseClass(ABC):
    """ Base class for tactic implementations.
    """
    __metaclass__ = ABCMeta

    def __init_subclass__(cls, **kwargs) -> None:
        required_attr: List[str] = [
            'name',
        ]
        for attr in required_attr:
            if not hasattr(cls, attr):
                raise NotImplementedError(f"Class is missing required '{attr}' attribute.")
        return super().__init_subclass__(**kwargs)

    @classmethod
    @abstractmethod
    def handle_tactic(cls, data: Dict[str, Any]) -> Dict[str, Any]:
        """ Handler function to handle the tactic given the provided input
            data set.

        Args:
            data (Dict[str, Any]): TODO

        Returns:
            Dict[str, Any]: TODO
        """
