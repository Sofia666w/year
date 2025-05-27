def get_age(year, month, day):
    from datetime import date
    today = date.today()
    age = today.year - year
    if today.month < month or (today.month == month and today.day < day):
        age = age - 1
    return age

print(get_age(1990, 5, 28))
