from datetime import datetime

def calculate_age(birth_date):
    today = datetime.now()
    age = today.year - birth_date.year

    # Check if birthday hasn't occurred this year
    if today.month < birth_date.month or (today.month == birth_date.month and today.day < birth_date.day):
        age -= 1

    return age

# Get user input
year = int(input("Enter birth year: "))
month = int(input("Enter birth month (1-12): "))
day = int(input("Enter birth day: "))

# Create birth_date object
birth_date = datetime(year, month, day)

# Calculate and print age
age = calculate_age(birth_date)
print(f"Your age is: {age} years")