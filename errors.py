#pylint:disable=missing-module-docstring


class TacticProcessingError(Exception):
    """ Base exception type for errors related to tactics
        and tactic processing.
    """


class MissingRequiredConfigError(TacticProcessingError):
    """ Exception is thrown if required configuration
        content is missing.
    """

    def __init__(self, config_key: str):
        super().__init__(f"Missing required configuration key '{config_key}'")
