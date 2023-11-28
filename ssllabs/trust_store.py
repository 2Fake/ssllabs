"""Trust Stores."""
from enum import IntEnum


class TrustStore(IntEnum):
    """Known trust stores."""

    MOZILLA = 1
    MACOS = 2
    ANDROID = 3
    JAVA = 4
    WINDOWS = 5
