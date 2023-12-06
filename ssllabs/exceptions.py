"""Exceptions for the ssllabs module."""


class SsllabsOverloadedError(Exception):
    """The service is overloaded."""

    def __init__(self) -> None:
        """Initialize error."""
        super().__init__("The ssllabs.com service is overloaded. You should sleep for several minutes then try again.")


class SsllabsUnavailableError(Exception):
    """The service is not available."""

    def __init__(self) -> None:
        """Initialize error."""
        super().__init__("The ssllabs.com service is currently not available.")
