# with open("/home/meatsack/Desktop/python_100_days/100_days_of_python/day_24/my_file.txt") as file:
#     contents = file.read()
#     print(contents)

with open("/home/meatsack/Desktop/python_100_days/100_days_of_python/day_24/my_file.txt", mode="a") as file:
    file.write("\n New text")
    
with open("/home/meatsack/Desktop/python_100_days/100_days_of_python/day_24/new_file.txt", mode="w") as file:
    file.write("\n New text")