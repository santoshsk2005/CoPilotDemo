import datetime

# Calculate the number of seconds in a year
seconds_in_minute = 60
minutes_in_hour = 60
hours_in_day = 24
# Ask the user to input a year
try:
    year = int(input("Enter a year: "))
except ValueError:
    year = datetime.datetime.now().year
    print(f"Invalid input. Using the current year: {year}")

# Determine if the year is a leap year
is_leap_year = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# Calculate the number of seconds in the year
days_in_year = 366 if is_leap_year else 365
seconds_in_year = seconds_in_minute * minutes_in_hour * hours_in_day * days_in_year

print(f"The year {year} is {'a leap year' if is_leap_year else 'not a leap year'}.")
print(f"The number of seconds in the year {year} is: {seconds_in_year}")