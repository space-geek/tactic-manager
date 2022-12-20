#pylint:disable=missing-class-docstring
#pylint:disable=missing-function-docstring
#pylint:disable=missing-module-docstring
import inspect
import json
from pathlib import Path
import pkgutil
from typing import Any
from typing import Dict
from typing import List
from typing import Type

from errors import MissingRequiredConfigError, TacticProcessingError
from tactics import TacticBaseClass

_CONFIG_FILEPATH:Path = Path.joinpath(Path.cwd(), "config.json")



def main() -> None:

    # Parse tactic definitions:
    tactics_by_name: Dict[str, Type[TacticBaseClass]] = {
        x.name: x for x in _import_tactic_classes()
    }

    # Load and validate the config:
    config_data: Dict[str, Any] = _load_and_validate_config()

    # Apply the tactic(s):
    if not config_data['tactics_to_apply']:
        print("No tactics to apply; nothing to do. Stopping.")
        return
    tactics_to_apply: List[Dict[str, Any]] = config_data['tactics_to_apply']
    print(f"Applying {len(tactics_to_apply)} tactic(s)...")
    for tactic_config in tactics_to_apply:
        name = tactic_config['name']
        if name not in tactics_by_name:
            print(f"Unsupported tactic '{name}' encountered. Skipping.")
            continue
        print(f"Applying tactic '{name}' to the plan...", end='')
        #TODO apply tactic
        print("done.")


def _import_tactic_classes() -> List[Type[TacticBaseClass]]:
    """ TODO: Function docstring

    """
    tactic_classes: List[Type[TacticBaseClass]] = []
    tactics_module = inspect.getmodule(TacticBaseClass)
    if not tactics_module:
        raise TacticProcessingError()
    for importer, module_name, _ in pkgutil.iter_modules(tactics_module.__path__):
        print(f"Loading tactics from submodule \"{module_name}\"...", end='')
        class_members = inspect.getmembers(
            importer.find_module(module_name).load_module(module_name),
            predicate=lambda x, n=module_name: inspect.isclass(x) and x.__module__ == n,
        )
        tactic_classes.extend(x for _, x in class_members if x.__base__ == TacticBaseClass)
        print("complete.")
    print(f"Imported {len(tactic_classes)} tactic(s): {list(x.name for x in tactic_classes)}")
    return tactic_classes


def _load_and_validate_config() -> Dict[str, Any]:
    """ TODO: Function docstring
    """

    # Load the config data from file:
    with open(_CONFIG_FILEPATH.absolute(), mode='r', encoding='utf-8') as f:
        config_data: Dict[str, Any] = json.load(f)

    # Validate that the required configuration entries are present:
    for attr in [
        'plan_uuid',
        'tactics_to_apply',
    ]:
        if attr not in config_data:
            raise MissingRequiredConfigError(attr)
    for tactic_config in config_data["tactics_to_apply"]:
        for attr in [
            'name',
        ]:
            if attr not in tactic_config:
                raise MissingRequiredConfigError(attr)

    return config_data


if __name__ == "__main__":
    main()
