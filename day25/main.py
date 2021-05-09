import csv

with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temparatures = []
    for row in data:
        if row[1] != "temp":
            temparatures.append(int(row[1]))
    print(temparatures)