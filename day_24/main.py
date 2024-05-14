# with open("/home/meatsack/Desktop/python_100_days/100_days_of_python/day_24/my_file.txt") as file:
#     contents = file.read()
#     print(contents)

with open("day_24\\my_file.txt", mode="a") as file:
    file.write("\n New text")
    
with open("day_24\\new_file.txt", mode="w") as file:
    file.write("\n New text")

with open("day_24\\file_with_name_in_it.txt", mode="w") as file:
    file.write("\n New name = John Doe")