age=int(input("Введите Ваш возраст "))


def age_condition(age):
    if age < 7:
        return "Иди в сад"

    elif age < 18:
        return "Иди в школу"
    elif age < 24:
        return "Иди в Вуз"
    else:
        return "Иди работать"


what_to_do=age_condition(age)
print(what_to_do)


