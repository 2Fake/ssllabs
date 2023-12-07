Advanced Usage
==============

Here are some examples of a more advanced usage of the library.

Print the grade of multiple servers
-----------------------------------

The following examples shows how to get the grade of multiple servers concurrently.

.. code-block:: python

   """Get grade of multiple servers."""
   from __future__ import annotations

   import asyncio

   from ssllabs import Ssllabs
   from ssllabs.data.host import HostData

   HOSTS = [
       "ssllabs.com",
       "www.ssllabs.com",
   ]


   async def analyze(hosts: list[str]) -> list[HostData]:
       """Analyze servers."""
       ssllabs = Ssllabs()
       if not await ssllabs.availability():
           raise
       return await asyncio.gather(*[ssllabs.analyze(host=host) for host in hosts])


   results = asyncio.run(analyze(HOSTS))
   for result in results:
       for endpoint in result.endpoints:
           if endpoint.grade:
               print(f"Grade of {result.host} ({endpoint.ipAddress}): {endpoint.grade}")
           else:
               print(endpoint.statusMessage)

Using an own HTTP client
------------------------

If you have special needs (e.g. what to use a proxy server), you can create an own HTTP client. Please read the `httpx documentation <https://www.python-httpx.org/advanced>`_ to find out which possibilities you have.

.. code-block:: python

   import asyncio

   from httpx import AsyncClient
   from ssllabs import Ssllabs
   from ssllabs.data.host import HostData

   async def analyze() -> HostData:
       async with AsyncClient(proxies="http://localhost:8030") as client:
           ssllabs = Ssllabs(client)
           return await ssllabs.analyze(host="ssllabs.com")

   asyncio.run(analyze())

Writing an own protocol client
------------------------------

If the high level methods do not match your use case, you can access each `API call <https://github.com/ssllabs/ssllabs-scan/blob/master/ssllabs-api-docs-v3.md#protocol-calls>`_ directly. However you have to take care of `rate limits <https://github.com/ssllabs/ssllabs-scan/blob/master/ssllabs-api-docs-v3.md#access-rate-and-rate-limiting>`_ your self. Classes are called like the API call without the leading get. The get method will query the API. It will take the parameters like in the documentation and return a dataclass representing the object, the API describes. Let's see an example using the analyze API call.

.. code-block:: python

   import asyncio

   from ssllabs.api import Analyze
   from ssllabs.data.host import HostData

   async def analyze_host() -> HostData:
       api = Analyze()
       host_object = await api.get(
           host="ssllabs.com",
           publish="on",
           startNew="off",
           fromCache="on",
           maxAge=24,
           all="done",
           ignoreMismatch="on"
       )
       return host_object

   asyncio.run(analyze_host())

One exception in the naming: the getEndpointData call is implemented in the Endpoint class to be able to better distinguish it from its EndpointData result object.

.. code-block:: python

   import asyncio

   from ssllabs.api import Endpoint
   from ssllabs.data.endpoint import EndpointData

   async def get_grade() -> EndpointData:
       api = Endpoint()
       endpoint = await api.get(host="ssllabs.com", s="64.41.200.100")
       return endpoint.grade

   asyncio.run(get_grade())

.. seealso::

   The `package overview <source/ssllabs.api.html>`_ provides all details about the API calls.

Exceptions
----------

Three types of exceptions may occur when the connection to SSL Labs' API is disrupted: `SsllabsUnavailableError <source/ssllabs.html#ssllabs.SsllabsUnavailableError>`_ arises when the servers are down, `SsllabsOverloadedError <source/ssllabs.html#ssllabs.SsllabsOverloadedError>`_ occurs if the service is overloaded in general or if you are using it too intensively. In all these cases, you are advised to wait for 15 to 30 minutes before attempting to connect again.

If you encounter an `EndpointError <source/ssllabs.html#ssllabs.EndpointError>`_ exception, it indicates that you have directly queried the `getEndpointData <https://github.com/ssllabs/ssllabs-scan/blob/master/ssllabs-api-docs-v3.md#retrieve-detailed-endpoint-information>`_ endpoint, but not all the necessary data is currently available. The accompanying message should provide guidance on how to address the issue.

If you get other exceptions during the execution of the library, please open an issue on `GitHub <https://github.com/2Fake/ssllabs/issues>`_.
