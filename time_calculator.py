def add_time(start, duration, starting_day=""):
    # Split the start time into hours, minutes, and AM/PM indicator
    start_time, end = start.split()
    start_hour, start_minute = map(int, start_time.split(":"))

    # Convert the time to 24-hour clock format if end is PM
    if end == "PM":
        start_hour += 12

    # Split the duration into hours and minutes
    duration_hour, duration_minute = map(int, duration.split(":"))

    # Calculate the new hour and minute after adding the duration
    new_hour = start_hour + duration_hour
    new_minute = start_minute + duration_minute

    # Adjust the hour and minute if minutes exceed 60
    new_hour += new_minute // 60
    new_minute %= 60

    # Calculate the number of days to be added
    days_add = new_hour // 24

    # Find AM and PM and convert to 12-hour clock format
    if new_hour >= 12:
        end = "PM"
        new_hour -= 12
    else:
        end = "AM"
    if new_hour == 0:
        new_hour = 12

    # Calculate the day of the week if starting_day is provided
    if starting_day:
        starting_day = starting_day.lower().capitalize()
        week_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        starting_index = week_days.index(starting_day)
        new_day_index = (starting_index + days_add) % 7
        new_day = week_days[new_day_index]
        day_str = f", {new_day}"
    else:
        day_str = ""

    # Build the new time string
    if days_add == 0:
        days_later = ""
    elif days_add == 1:
        days_later = " (next day)"
    else:
        days_later = f" ({days_add} days later)"

    new_time = f"{new_hour:02d}:{new_minute:02d} {end}{day_str}{days_later}"
    return new_time

