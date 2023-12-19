# ssllabs

This project implements the [Qualys SSL Labs](https://www.ssllabs.com/ssltest/) API in python. It uses [API version 3](https://github.com/ssllabs/ssllabs-scan/blob/master/ssllabs-api-docs-v3.md). All methods are async. However, it is not affiliated with or officially supported by SSL Labs.

## System requirements

Defining the system requirements with exact versions typically is difficult. But there is a tested environment:

* Linux
* Python 3.11.6
* pip 23.3.1
* dacite 1.8.1
* httpx 0.25.2

Other versions and even other operating systems might work. Feel free to tell us about your experience.

## Versioning

In our versioning we follow [Semantic Versioning](https://semver.org/).

## Installation

The Python Package Index takes care for you. Just use pip or your favorite package manager. Please take care of creating a virtual environment if needed.

```bash
python -m pip install ssllabs
```

## High level usage

If you want to cover on the common usage cases, you can use our high level implementations that already take care of the recommended [protocol usage](https://github.com/ssllabs/ssllabs-scan/blob/master/ssllabs-api-docs-v3.md#protocol-usage) and [rate limits](https://github.com/ssllabs/ssllabs-scan/blob/master/ssllabs-api-docs-v3.md#access-rate-and-rate-limiting). Please keep in mind, that you will be sending assessment requests to remote SSL Labs servers and that your information will be shared with them. Subject to the [terms and conditions](https://www.ssllabs.com/about/terms.html).

```python
import asyncio

from ssllabs import Ssllabs

async def analyze():
    ssllabs = Ssllabs()
    return await ssllabs.analyze(host="ssllabs.com")

asyncio.run(analyze())
```

This will give you a [Host object](https://github.com/ssllabs/ssllabs-scan/blob/master/ssllabs-api-docs-v3.md#host) as dataclass. This call runs quite long as it takes time to run all tests. You probably know that from using the [webinterface](https://www.ssllabs.com/ssltest).

> [!TIP]
> Please see our [documentation](https://2fake.github.io/ssllabs/) for further information and extended examples.
