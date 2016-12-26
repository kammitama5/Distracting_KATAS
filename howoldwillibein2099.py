def calculate_age(year_of_birth, current_year):
    age = current_year - year_of_birth
    if age == 0:
        return "You were born this very year!"
    elif age == -1:
        return "You will be born in {} year.".format(abs(age))
    elif age == 1:
        return "You are {} year old.".format(age)
    elif age > 0:
        return "You are {} years old.".format(age)
    else:
        return "You will be born in {} years.".format(abs(age))