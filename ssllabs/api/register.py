import httpx
from dacite import from_dict

from ..data.register import RegisterData
from ._api import _Api

SSLLABS_URL = f"https://api.ssllabs.com/api/v{4}/"


class Register(_Api):
    """General information about the ssllabs API.

    See also: https://github.com/ssllabs/ssllabs-scan/blob/master/ssllabs-api-docs-v3.md#check-ssl-labs-availability
    """

    async def register(self, first_name, last_name, email, organization) -> RegisterData:
        """Get information.

        :raises httpx.ConnectTimeout: SSL Labs Servers don't respond.
        :raises httpx.HTTPStatusError: A client or server error response occured.
        :raises httpx.ReadTimeout: SSL Labs Servers don't respond.
        """
        async with httpx.AsyncClient() as client:
            r = await client.post(
                f"{SSLLABS_URL}register",
                headers={"Content-Type": "application/json"},
                json={"firstName": first_name, "lastName": last_name, "email": email, "organization": organization},
            )

        r.raise_for_status()
        return from_dict(data_class=RegisterData, data=r.json())


# {"message":"User successfully registered","status":"success"}
# {"errors":[{"field":"email","message":"Email already registered with us. Please use different email."}]}
