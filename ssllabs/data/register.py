from dataclasses import dataclass
from typing import List

# Successful regristration call --> {"message":"User successfully registered","status":"success"}
# Email already in use --> {"errors":[{"field":"email","message":"Email already registered with us. Please use different email."}]}


@dataclass
class RegisterData:
    """Dataclass for info objects.

    See also: https://github.com/ssllabs/ssllabs-scan/blob/master/ssllabs-api-docs-v3.md#info
    """

    message: str
    """Registration message response"""

    status: str
    """Either 'success' or 'failure'"""
