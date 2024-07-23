# with open("weather_data.csv") as file:
#     for line in file:
#         weather = line.strip()
#         print(weather)
import pandas
# import csv
#
# with open("weather_data.csv") as data_file:
#     # Create a csv reader
#     data = csv.reader(data_file)
#
#     # Skip the first row(header)
#     next(data)
#     temperatures = []
#     for row in data:
#         temperatures.append(int(row[1]))
#
# print(temperatures)

import pandas as pd

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240521.csv")

gray_count = len(data[data["Primary Fur Color"] == "Gray"])
red_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_count = len(data[data["Primary Fur Color"] == "Black"])

squirrel_count = {
    "Fur Color": ["gray", "red", "black"],
    "Count": [gray_count, red_count, black_count]
}

data_dict = pandas.DataFrame(squirrel_count)
print(data_dict)
data_dict.to_csv("squirrel_count.csv")

# data = pd.read_csv("weather_data.csv")
# temp_list = data["temp"].to_list()
# print(temp_list)
# print(int(sum(temp_list) / len(temp_list)))
# print(data["temp"].mean())
# print(data["temp"].max())
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.min()])
#
# temp_monday = data[data.day == "Monday"]
# fahrenheit_series = temp_monday.temp * 9/5 + 32
# print(fahrenheit_series)
#
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
#
# data_frame = pandas.DataFrame(data_dict)
# print(data_frame)
#
# data_frame.to_csv("newdata.csv")

#
# with open("file1.txt") as file1:
#     numbers1 = [int(line.strip()) for line in file1.readlines()]
#
# with open("file2.txt") as file2:
#     numbers2 = [int(line.strip()) for line in file2.readlines()]
#
# result = [numb for numb in numbers1 if numb in numbers2]