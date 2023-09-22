def add_time(start, duration, day=None):

  #Get well-formatted start and duration time
  start_time = start.split()
  time, meridian = start_time[0], start_time[1]
  start_hour, start_minute = map(int, time.split(":"))
  duration_hours, duration_minutes = map(int, duration.split(":"))

  #time_modifier
  if meridian == "PM":
    start_hour += 12  #To convert to 24 hour clock system

  #work in unified time in minutes
  total_minutes = start_hour * 60 + start_minute + duration_hours * 60 + duration_minutes

  #new_time
  new_hour = total_minutes // 60 % 24  #gets full hours
  new_minute = total_minutes % 60  #Gets total minutes remaining after full hours

  #Determine meridian and handle midnight
  if new_hour >= 12:
    new_meridian = "PM"
    if new_hour > 12:
      new_hour -= 12
  else:
    new_meridian = "AM"
    if new_hour == 0:  #midnight
      new_hour = 12

  #determining days passed
  days_passed = total_minutes // 1440  #divide total_minutes with total minutes in a day

  days_of_week = [
      "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday",
      "Saturday"
  ]

  if day:
    day = day.title()
    day_index = days_of_week.index(day)
  else:
    day_index = None

  #Get new day
  new_day_index = (day_index +
                   days_passed) % 7 if day_index is not None else None

  result = f"{new_hour}:{new_minute:02} {new_meridian}"
  if new_day_index is not None:
    result += f", {days_of_week[new_day_index]}"

  if days_passed == 1:
    result += " (next day)"
  elif days_passed > 1:
    result += f" ({days_passed} days later)"

  return result
