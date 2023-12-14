# ssllabs Unittests

The unittests are based on pytest.

## System requirements

Defining the system requirements with exact versions typically is difficult. But there is a tested environment:

* Linux
* Python 3.11.6
* pytest 7.4.3
* pytest-asyncio 0.21.1
* pytest-httpx 0.27.0

## Running the tests

Install the extra requirements and start pytest.

```bash
python -m pip install -e .[test]
pytest
```
