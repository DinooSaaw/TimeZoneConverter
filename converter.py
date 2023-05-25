from datetime import datetime
import pytz

# Prompt the user for the source time zone
source_tz = input("Enter the source time zone: ")

# Prompt the user for the source time
source_time_str = input("Enter the source time (e.g., 9 am): ")
source_time = datetime.strptime(source_time_str, "%I %p")

# Prompt the user for the target time zone
target_tz = input("Enter the target time zone: ")

# Define a dictionary to map custom time zone identifiers to pytz time zones
time_zone_mapping = {
    'PST': 'America/Los_Angeles',
    'EST': 'America/New_York',
    'CST': 'America/Chicago',
    'MST': 'America/Denver',
    'HST': 'Pacific/Honolulu',
    'AKST': 'America/Anchorage',
    'AEST': 'Australia/Sydney',
    'ACST': 'Australia/Adelaide',
    'AWST': 'Australia/Perth',
    'CET': 'Europe/Paris',
    'IST': 'Asia/Kolkata',
    # Add more time zones as needed
}

# Convert the source time zone to the corresponding pytz time zone
source_tz = time_zone_mapping.get(source_tz.upper(), source_tz)
target_tz = time_zone_mapping.get(target_tz.upper(), target_tz)

# Get the current date
current_date = datetime.now().date()

# Combine the current date with the source time
source_datetime = pytz.timezone(source_tz).localize(datetime.combine(current_date, source_time.time()))

# Convert the source time to the target time zone
target_datetime = source_datetime.astimezone(pytz.timezone(target_tz))

# Calculate the time difference until the target time
time_difference = target_datetime - datetime.now(pytz.timezone(target_tz))

# Print the converted time and the time remaining
print("Converted time:", target_datetime.strftime("%Y-%m-%d %H:%M:%S"))
print("Time remaining until target time:", time_difference)
