
#1 
# open the weather data csv and save it as data (raw text lines in list)
# with open("./weather_data .csv") as file:
#     data = file.readlines()
#
# print(data)

#2 
# import csv
#
# open the weather data csv and save it as data (splits commas in text lines. Add temperatures to a list)
# with open("./weather_data .csv") as file:
#     data = csv.reader(file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

#3 
# import pandas

#open the weather data csv and save it as data ([['day', 'temp', 'condition'], [...], [...]])
# data = pandas.read_csv("weather_data .csv")

# Convert date to dictionary
# data_dict = data.to_dict()

# Find average temp
# temp_list = data["temp"].to_list()
# average_temp = sum(temp_list)/len(temp_list)

# Use api to find max
# max_temp = data["temp"].max()
# print(max_temp)

# Get data in row
# highest_temp_row = (data[data.temp == max_temp])
# print(highest_temp_row)

# Get data in row and convert to fahrenheit
# monday = data[data.day == "Monday"]
# monday_temp = (monday.temp[0] *9/5) +32
# print(monday_temp)

# Create a data frame from scratch
# data_dict = {
#     "students": ["Amy","James","Angela"],
#     "scores": [76, 56, 65]
# }
#
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")

# Challenge: Figure out how many of each primary fur colors there are from the csv file and display in new csv
import pandas
new_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240929.csv")
primary_fur_colors = new_data["Primary Fur Color"]
colors = primary_fur_colors.unique()
count = primary_fur_colors.value_counts()
keys= colors.tolist()
values = count.to_list()

data_dict = {
      "Primary Fur Color": [keys[1],keys[2],keys[3]],
    "count": [values[0],values[1],values[2]]

  }

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")


