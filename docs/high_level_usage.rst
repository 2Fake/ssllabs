High Level Usage
================

.. mdinclude:: ../README.md
   :start-line: 44
   :end-line: 46

Analyzing a host
----------------

.. mdinclude:: ../README.md
   :start-line: 47
   :end-line: 61

If you don't need a fresh result on every run, you can allow using SSL Labs' cache. This will speed up the tests if there are cached results. The maximum cache validity can be set in full hour steps.

.. code-block:: python

   import asyncio

   from ssllabs import Ssllabs

   async def analyze():
       ssllabs = Ssllabs()
       return await ssllabs.analyze(host="ssllabs.com", from_cache=True, max_age=1)

   asyncio.run(analyze())

Last but not least you can specify if you want to publish your results on the `SSL Labs website <https://www.ssllabs.com/ssltest/>`_ and to proceed with the analysis even if the certificate doesn't match the hostname.

.. code-block:: python

   import asyncio

   from ssllabs import Ssllabs

   async def analyze():
       ssllabs = Ssllabs()
       return await ssllabs.analyze(host="ssllabs.com", publish=True, ignore_mismatch=True)

   asyncio.run(analyze())

By default, results are not published, the assessment will not continue if the certificate doesn't match the hostname and the cache is not used.

Check availability of the SSL Labs servers
------------------------------------------

.. code-block:: python

   import asyncio

   from ssllabs import Ssllabs

   async def availability():
       ssllabs = Ssllabs()
       return await ssllabs.availability()

   asyncio.run(availability())

This will give you True if the servers are up and running, otherwise False. It will also report False if you exceeded your rate limits.

Retrieve API information
------------------------

.. code-block:: python

   import asyncio

   from ssllabs import Ssllabs

   async def info():
       ssllabs = Ssllabs()
       return await ssllabs.info()

   asyncio.run(info())

This will give you an `Info object <https://github.com/ssllabs/ssllabs-scan/blob/master/ssllabs-api-docs-v3.md#info>`_ as dataclass.

Retrieve root certificates
--------------------------

.. code-block:: python

   import asyncio

   from ssllabs import Ssllabs, TrustStore

   async def root_certs():
       ssllabs = Ssllabs()
       return await ssllabs.root_certs(trust_store=TrustStore.MOZILLA)

   asyncio.run(root_certs())

This will give you a string containing the latest root certificates used for trust validation. By default it used the certificates provided by Mozilla. You can choose a differently store by changing trust_store to one of the supported trust stores.

Supported trust stores are:

* MOZILLA
* MACOS
* ANDROID
* JAVA
* WINDOWS

Retrieve known status codes
---------------------------

.. code-block:: python

   import asyncio

   from ssllabs import Ssllabs

   async def status_codes():
       ssllabs = Ssllabs()
       return await ssllabs.status_codes()

   asyncio.run(status_codes())

This will give you a `StatusCodes object <https://github.com/ssllabs/ssllabs-scan/blob/master/ssllabs-api-docs-v3.md#statuscodes>`_ as dataclass.
