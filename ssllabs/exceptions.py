"""Exceptions for the ssllabs module."""
from __future__ import annotations


class EndpointError(Exception):
    """The Endpoint API raised errors."""

    def __init__(self, messages: list[dict[str, str]]) -> None:
        """Initialize error."""
        super().__init__(messages[0]["message"])


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
