def get_sum(num_one, num_two):

    try:
        return int(num_one)+int(num_two)
    except ValueError:
        return "Введен неверный тип данных"
    
a=get_sum("sd", 4)
print(a)