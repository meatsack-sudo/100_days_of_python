# # list_of_data = []

# # with open("day_25_start\\weather_data.csv", mode="r") as data:
# #     for datapoint in data.readlines():
# #         list_of_data.append(datapoint.strip())

# # print(list_of_data)

# # import csv
# # with open("day_25_start\\weather_data.csv", mode="r") as data_file:
# #     data = csv.DictReader(data_file)
# #     for row in data:
# #         print(row["temp"])

# # import csv
# # with open("day_25_start\\weather_data.csv", mode="r") as data_file:
# #     data = csv.reader(data_file)
# #     temperatures = []
# #     for row in data:
# #         if row[1] != "temp":
# #             temperatures.append(int(row[1]))
# # print(temperatures)

import pandas
data = pandas.read_csv("day_25_start\\weather_data.csv")

# # # print(data["temp"])

# # data_dict = data.to_dict()
# # print(data_dict)

# # temp_list = data["temp"].to_list()
# # print(temp_list)

# # # average_temp = sum(temp_list)/len(temp_list)

# # # print(int(average_temp))

# # average_temp = data["temp"].mean()
# # temp_max = data["temp"].max()

# # print(average_temp)
# # print(temp_max)

# #Get Data in Columns
# # print(data["condition"])
# # print(data.condition)

#Get Data in row
print(data[data.day == "Monday"])
print(data[data.temp == data["temp"].max()])

# # monday = data[data.day == "Monday"]
# # print(monday.condition)

# # converttemp = (monday.temp[0] * 9/5) + 32

# # print(converttemp)

# #Create a dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")

#import pandas
#data = pandas.read_csv("day_25_start\\2018_squirrel_data.csv")

#My solution to challengge
# black = 0
# cinnamon = 0
# gray = 0

# print(data["Primary Fur Color"])

# for index, lines in data.iterrows():
#     if lines["Primary Fur Color"] == "Black":
#         black += 1
#     elif lines["Primary Fur Color"] == "Gray":
#         gray += 1
#     elif lines["Primary Fur Color"] == "Cinnamon":
#         cinnamon += 1
#     else:
#         pass

# print(black, cinnamon, gray)

# data_dict = {
#     "fur_color": ["grey", "red", "black"],
#     "count": [gray, cinnamon, black]
# }
# new_data = pandas.DataFrame(data_dict)
# new_data.to_csv("day_25_start\\fur_colors.csv")

#Instructor solution to challenge
#grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
#red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
#black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
#print(grey_squirrels_count)
#print(red_squirrels_count)
#print(black_squirrels_count)

#data_dict = {
#    "Fur Color": ["Gray", "Cinnamon", "Black"],
#    "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
#}

#df = pandas.DataFrame(data_dict)
#df.to_csv("day_25_start\\fur_colors.csv")
