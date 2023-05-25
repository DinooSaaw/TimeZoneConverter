from datetime import datetime
from time_zones import time_zone_mapping
import pytz

def validate_time_zone(time_zone):
    if time_zone.upper() not in time_zone_mapping.keys():
        raise ValueError("Invalid time zone entered.")

def get_source_time_zone():
    source_tz = input("Enter the source time zone (PST): ")
    validate_time_zone(source_tz)
    return time_zone_mapping[source_tz.upper()]

def get_target_time_zone():
    target_tz = input("Enter the target time zone (AEST): ")
    validate_time_zone(target_tz)
    return time_zone_mapping[target_tz.upper()]

def get_source_time():
    source_time_str = input("Enter the source time (9 am): ")
    try:
        return datetime.strptime(source_time_str, "%I %p")
    except ValueError as e:
        raise ValueError("Invalid time format entered.") from e

def calculate_time_difference(target_datetime):
    time_difference = target_datetime - datetime.now(pytz.timezone(target_tz))
    seconds = time_difference.total_seconds()
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    seconds = int(seconds % 60)
    return hours, minutes, seconds

# Prompt the user for the source time zone
try:
    source_tz = get_source_time_zone()
except ValueError as e:
    print("Error:", e)
    exit()

# Prompt the user for the source time
try:
    source_time = get_source_time()
except ValueError as e:
    print("Error:", e)
    exit()

# Prompt the user for the target time zone
try:
    target_tz = get_target_time_zone()
except ValueError as e:
    print("Error:", e)
    exit()

# Get the current date
current_date = datetime.now().date()

# Combine the current date with the source time
source_datetime = pytz.timezone(source_tz).localize(datetime.combine(current_date, source_time.time()))

# Convert the source time to the target time zone
target_datetime = source_datetime.astimezone(pytz.timezone(target_tz))

# Calculate the time difference until the target time
hours, minutes, seconds = calculate_time_difference(target_datetime)

# Print the converted time and the formatted time remaining
print("Converted time:", target_datetime.strftime("%Y-%m-%d %H:%M:%S"))
print(f"Time remaining until target time: {hours} Hours {minutes} Mins {seconds} Seconds")