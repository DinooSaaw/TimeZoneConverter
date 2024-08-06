from datetime import datetime, timedelta
import pytz
from time_zones import time_zone_mapping

def validate_time_zone(time_zone: str) -> None:
    """Validate the time zone."""
    if not isinstance(time_zone, str):
        raise ValueError("Time zone must be a string.")
    time_zone = time_zone.strip().upper()
    if time_zone not in time_zone_mapping:
        raise ValueError("Invalid time zone entered.")

def get_time_zone(prompt: str) -> str:
    """Get the time zone from the user."""
    while True:
        time_zone = input(prompt) or 'PST'
        try:
            validate_time_zone(time_zone)
            return time_zone_mapping[time_zone]
        except ValueError as e:
            print("Error:", e)

def get_source_time() -> datetime:
    """Get the source time from the user."""
    while True:
        source_time_str = input("Enter the source time (e.g., 9 am): ") or '9 am'
        try:
            return datetime.strptime(source_time_str, "%I %p")
        except ValueError as e:
            print("Error:", e)

def calculate_time_difference(target_datetime: datetime, target_tz: str) -> tuple:
    """Calculate the time difference until the target time."""
    time_difference = target_datetime - datetime.now(pytz.timezone(target_tz))
    if time_difference.total_seconds() < 0:
        raise ValueError("Target time is in the past.")
    seconds = time_difference.total_seconds()
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    seconds = int(seconds % 60)
    return hours, minutes, seconds

while True:
    try:
        # Prompt the user for the source time zone
        source_tz = get_time_zone("Enter the source time zone (e.g., PST): ")

        # Prompt the user for the source time
        source_time = get_source_time()

        # Prompt the user for the target time zone
        target_tz = get_time_zone("Enter the target time zone (e.g., AEST): ")

        # Get the current date
        current_date = datetime.now().date()

        # Combine the current date with the source time
        source_datetime = pytz.timezone(source_tz).localize(datetime.combine(current_date, source_time.time()))

        # Convert the source time to the target time zone
        target_datetime = source_datetime.astimezone(pytz.timezone(target_tz))

        # Calculate the time difference until the target time
        hours, minutes, seconds = calculate_time_difference(target_datetime, target_tz)

        # Print the converted time and the formatted time remaining
        converted_time = target_datetime.strftime("%H:%M:%S")
        print("Converted time:", converted_time)
        print(f"Time remaining until target time: {hours} Hours {minutes} Mins {seconds} Seconds")
        
        # Prompt the user if they want to convert again
        choice = input("Do you want to convert again? (y/n): ")
        if choice.lower() != 'y':
            break

    except ValueError as e:
        print("Error:", e)
        continue