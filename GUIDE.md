# PyTimeliner User Guide
PyTimeliner is a Python library that provides tools for working with dates, times, and multilingual time expressions. You can easily format dates, calculate time differences, and get translated time-related information in various languages.

- Table of Contents
  - Installation
  - Getting Started
  - Core Features
    - Formatting Dates
    - Time Calculations
    - Human-Readable Time Since Calculations
    - Multilingual Time Expressions
  - Advanced Usage
  - Troubleshooting
## 1. Installation
To install PyTimeliner, clone the repository and install the package:
```bash
git clone https://github.com/nowte/PyTimeliner.git
cd PyTimeliner
pip install -e .
```

Ensure that `googletrans` is in your `requirements.txt` if you plan to use multilingual support:
```bash
googletrans==4.0.0-rc1
```

Or install it directly:

```bash
pip install googletrans==4.0.0-rc1
```

## 2. Getting Started
To begin using `pytimeliner`, import the `TimeLiner` class and initialize it with the desired language. The default language is English (`en`), but you can change it later.
```bash
from pytimeliner.timeliner import TimeLiner

# Initialize with English
timeliner = TimeLiner(language='en')

# Or set language to Spanish
timeliner.set_language('es')
```

## 3. Core Features
##### Formatting Dates
You can format dates using the `format_time` function, which takes a `datetime` object and an optional format string.

```bash
from datetime import datetime

# Example: Format the current date and time
formatted_time = timeliner.format_time(datetime.now(), "%Y-%m-%d %H:%M:%S")
print(formatted_time)  # Output: "2024-10-29 12:34:56"
```

Time Calculations
The `add_time` and `subtract_time` functions allow you to manipulate `datetime` objects by adding or subtracting specific durations.

```bash
# Add 2 days and 3 hours to a specific date
future_date = timeliner.add_time(datetime(2024, 10, 29), days=2, hours=3)
print(future_date)  # Output: datetime object adjusted by 2 days and 3 hours

# Subtract 1 day and 2 hours
past_date = timeliner.subtract_time(datetime(2024, 10, 29), days=1, hours=2)
print(past_date)  # Output: datetime object adjusted by -1 day and -2 hours
```

#####  Human-Readable Time Since Calculations
The `time_since` function provides a human-readable string representing the time that has passed since a given date. It returns results in the form “X days ago,” “Y hours ago,” etc.
```bash
# Calculate the time since a specific date
past_date = datetime(2023, 1, 1, 12, 0, 0)
time_ago = timeliner.time_since(past_date)
print(time_ago)  # Output: "298 days ago"
```

##### Multilingual Time Expressions
To display time expressions in a specific language, use `set_language` to set the language, and `time_since` will automatically return the translated text.
```bash
# Change language to Spanish and display time since in Spanish
timeliner.set_language('es')
time_ago_es = timeliner.time_since(past_date)
print(time_ago_es)  # Output: "hace 298 días"
```
Supported languages include English (`en`), Spanish (`es`), French (`fr`), German (`de`), and more. Language codes are standard ISO language codes.

## 4. Advanced Usage
##### Getting a Range of Dates
The `get_date_range` function generates a list of dates between a start and end date, with optional intervals.
```bash
from datetime import datetime

# Get all dates from 2024-01-01 to 2024-01-05
dates = timeliner.get_date_range(datetime(2024, 1, 1), datetime(2024, 1, 5))
for date in dates:
    print(date)
# Output: 
# 2024-01-01
# 2024-01-02
# 2024-01-03
# 2024-01-04
# 2024-01-05
```
##### Custom Translations
If a translation fails, `translate_time_info` will return the original English text. This can occur if Google Translate is temporarily unavailable. To troubleshoot, retry the translation or ensure you have the latest version of `googletrans`.

### 5. Troubleshooting
##### Common Issues
Translation Not Working: Make sure `googletrans` is correctly installed. Verify that `googletrans==4.0.0-rc1` is in your environment.

Invalid Dates or Formats: Confirm that all date inputs are valid `datetime` objects. Invalid formats may cause unexpected results.

API Errors: Google Translate may experience temporary outages. Retry if translations fail.

With this guide, you should have everything you need to get started with `pytimeliner!` For more detailed inquiries or bug reporting, visit the [GitHub Repository.](https://www.github.com/nowte/PyTimeliner)