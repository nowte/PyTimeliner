<class>
<h1><p align="center">
  PyTimeliner
</p></h1>

<p align="center"><a href="https://github.com/nowte/PyTimeliner/issues"><img alt="Issues open" src="https://img.shields.io/github/issues-raw/nowte/PyTimeliner?style=for-the-badge" height="20"/></a>
<a href="https://github.com/nowte/PyTimeliner/"><img alt="Last commit" src="https://img.shields.io/github/last-commit/nowte/PyTimeliner?style=for-the-badge" height="20"/></a>
<a href="https://github.com/nowte/PyTimeliner/blob/main/LICENSE"><img alt="License" src="https://img.shields.io/github/license/nowte/PyTimeliner?style=for-the-badge" height="20"/></a>
<a href="https://github.com/nowte/PyTimeliner/releases"><img alt="Latest version" src="https://img.shields.io/github/v/tag/nowte/PyTimeliner?label=Latest%20Version&style=for-the-badge" height="20"/></a>
<a href="https://pypi.org/project/PyTimeliner/"><img alt="PyPI Version" src="https://img.shields.io/pypi/v/PyTimeliner?style=for-the-badge" height="20"/></a>

**PyTimeliner** is a Python package for working with time-based functions such as formatting, time calculations, and multilingual time expressions. This package provides various tools for handling date and time calculations in multiple languages. [PyPi Link](https://pypi.org/project/pytimeliner/)

## Features

- Format and humanize time expressions
- Perform date and time calculations
- Get time expressions in different languages
- Useful for applications requiring time-based utilities in various languages

## Installation

### Using `setup.py`

First, clone the repository and navigate to the project directory. Then, install the package with:

```bash
pip install -e .
```

This package uses googletrans for translation support. If you are using requirements.txt, make sure it contains:

```bash
googletrans==4.0.0-rc1
```

## Usage
Using PyTimeliner, you can perform time calculations, format times, and translate time expressions.

### Example Usage
```bash
from pytimeliner.timeliner import TimeLiner
from datetime import datetime

# English timeline
timeliner = TimeLiner(language='en')
print(timeliner.format_time(datetime.now()))
print(timeliner.time_since(datetime(2023, 1, 1, 12, 0, 0)))
timeliner.set_language('es')
print(timeliner.time_since(datetime(2023, 1, 1, 12, 0, 0)))
```

## Output
```bash
2024-10-29 12:34:56
"298 days ago"        # English
"hace 298 días"       # Spanish (translated)
```

## Development
To contribute to this project, please follow the [GitHub Repository](https://github.com/nowte/PyTimeliner) and create a fork. Make sure you have the following in requirements.txt:
```bash
googletrans==4.0.0-rc1
```

You can install the requirements with:

```bash
pip install -r requirements.txt
```

## Running Tests
To run tests, use the tests folder which contains test files:

```bash
python -m unittest discover -s tests
```
## Contributing
If you want to contribute, feel free to open an issue or submit a pull request. All contributions are welcome!
