marks=[{'school_class': '4a', 'scores': [5,5,5,5,5]}, {'school_class': '5a', 'scores': [5,4,4,5,2]}, {'school_class': '5a', 'scores': [5,4,4,5,2]}]
sum_for_school=0
for dicts in marks:
    sum_for_class=0
    for score in dicts["scores"]:
        sum_for_class = sum_for_class + score
    middle_for_class = sum_for_class/len(dicts["scores"])
    print ("Средняя оценка в " + str(dicts["school_class"]) + " " + str(middle_for_class))
    sum_for_school = sum_for_school + middle_for_class
middle_for_school = sum_for_school/len(marks)   
print ("Средняя оценка в школе " + str(middle_for_school))