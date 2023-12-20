# import csv
#
#
# with open('weather_data.csv', 'r') as f:
#     data = csv.reader(f)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#
# print(temperatures)

# import pandas
#
# data = pandas.read_csv("weather_data.csv")
# temp = data[data.day == "Monday"].temp
# temp = temp * 1.8 + 32
# print(temp)


import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
furs = data["Primary Fur Color"].dropna().unique()
count = [len(data[data["Primary Fur Color"] == fur]) for fur in furs]
new_data = pandas.DataFrame({"Fur Color": furs, "Count": count})
print(new_data)
