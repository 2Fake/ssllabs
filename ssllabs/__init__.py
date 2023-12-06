"""Qualys SSL Labs API in Python."""
from importlib.metadata import PackageNotFoundError, version

from .exceptions import SsllabsOverloadedError, SsllabsUnavailableError
from .ssllabs import Ssllabs
from .trust_store import TrustStore

__license__ = "MIT"

try:
    __version__ = version("ssllabs")
except PackageNotFoundError:
    # package is not installed
    __version__ = "0.0.0"

__all__ = ["Ssllabs", "SsllabsOverloadedError", "SsllabsUnavailableError", "TrustStore", "__license__", "__version__"]
