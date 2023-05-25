# Time Zone Conversion Script

This is a Python script that allows you to convert time between different time zones and calculate the time remaining until a target time.

## Prerequisites

- Python 3.x
- pytz library (can be installed using `pip install pytz`)

## Usage

1. Clone the repository or download the script.

2. Open a terminal or command prompt and navigate to the directory where the script is located.

3. Run the script using the command `python time_zone_converter.py`.

4. Follow the prompts to enter the source time zone, source time, and target time zone.

5. The script will display the converted time in the target time zone and the time remaining until the target time in the format of "x Hours x Mins x Seconds".

## Customization

- The script uses a dictionary `time_zone_mapping` to map custom time zone abbreviations to pytz time zones. You can modify this dictionary to include additional time zones or modify the existing ones according to your needs.

## Error Handling

- The script includes error handling to handle potential errors and invalid inputs. It validates the user-entered time zones and time format to ensure accurate conversions.

- If an error occurs during user input, an error message will be displayed, and the script will exit.

## Acknowledgements

- The script utilizes the pytz library for time zone conversions. Visit the [pytz documentation](https://pypi.org/project/pytz/) for more information.
