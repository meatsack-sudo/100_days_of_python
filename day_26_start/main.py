#List comprehension
# numbers = [1, 2, 3]
# new_numbers = [n + 1 for n in numbers]
# #print(new_numbers)

# name = "Angela"
# letters_list = [letter for letter in name]
# #print(letters_list)

# new_range = [number * 2 for number in range(1, 5)]
# #print(new_range)

# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# new_names = [name for name in names if len(name) < 5]
# new_names2 = [name.upper() for name in names if len(name) > 5]
#print(new_names2)

#Dictionary Comprehension
#new_dict = {new_key:new_value for(key, value) in dict.items() if test}
import pandas
import random

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
student_score = {student:random.randint(1, 100) for student in names}
print(student_score)

student_data_frame = pandas.DataFrame(student_score)
for (key, value) in student_data_frame.items():
    print(value)

for (index, row) in student_data_frame.iterrows():
    print(index)
    print(row)
    print(row.student)
    print(row.score)
    if row.student == "Angela":
        print(row.score)


passed_students = {student:score for (student, score) in student_score.items() if score > 50}
print(passed_students)

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
result = result = {word:len(word) for word in sentence.split()}
print(result)

weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}
weather_f = {day:(temp * 9/5) + 32 for (day, temp) in weather_c.items()}
print(weather_f)