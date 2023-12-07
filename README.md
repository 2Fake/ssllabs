# ssllabs

This project implements the [Qualys SSL Labs](https://www.ssllabs.com/ssltest/) API in python. It uses [API version 3](https://github.com/ssllabs/ssllabs-scan/blob/master/ssllabs-api-docs-v3.md). All methods are async.

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

## Installing for usage

The Python Package Index takes care for you. Just use pip or your favorite package manager. Please take care of creating a virtual environment if needed.

```bash
python -m pip install ssllabs
```

## Installing for development

First, you need to get the sources.

```bash
git clone git@github.com:2Fake/ssllabs.git
```

Then you need to take care of the requirements. Please take care of creating a virtual environment if needed.

```bash
cd ssllabs
python -m pip install -e .[dev]
```

## High level usage

If you want to cover on the common usage cases, you can use our high level implementations that already take care of the recommended [protocol usage](https://github.com/ssllabs/ssllabs-scan/blob/master/ssllabs-api-docs-v3.md#protocol-usage) and [rate limits](https://github.com/ssllabs/ssllabs-scan/blob/master/ssllabs-api-docs-v3.md#access-rate-and-rate-limiting).

```python
import asyncio

from ssllabs import Ssllabs

async def analyze():
    ssllabs = Ssllabs()
    return await ssllabs.analyze(host="ssllabs.com")

asyncio.run(analyze())
```

This will give you a [Host object](https://github.com/ssllabs/ssllabs-scan/blob/master/ssllabs-api-docs-v3.md#host) as dataclass. This call runs quite long as it takes time to run all tests. You probably know that from using the [webinterface](https://www.ssllabs.com/ssltest).
