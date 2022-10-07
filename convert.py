import struct
import csv

with open("sport_food.csv", "r", encoding="cp1251") as sport_food_csv:
    sport_food = list(csv.reader(sport_food_csv))
    sport_food_count = len(sport_food)
with open("sport_food.bin", "wb") as sport_food_bin:
    p = struct.pack("I", sport_food_count - 1)
    sport_food_bin.write(p)
    for i in sport_food[1:]:
        p = struct.pack("100sHH", i[0].encode("utf8"), int(i[1]), int(i[2]))
        sport_food_bin.write(p)

"""
import csv                        
import struct
#Здесь через считывание в словарь, плюс количество товаров заранее не узнавали, добавляли и параллельно их считали
#затем с помощью seek(0) переставили курсор в начало и добавили количество товара

with open("sport_food.csv", encoding='windows-1251') as sport:
    with open("sport_food.bin", "wb") as sport_food:
        sp = csv.DictReader(sport)
        x = 0
        new = struct.pack("I", x)
        sport_food.write(new)
        for i in sp:
            prod = struct.pack("100sHH", i['Название'].encode(encoding="UTF-8"), int(i['Вес']), int(i['Стоимость']))
            sport_food.write(prod)
            x += 1
        sport_food.seek(0)
        new_2 = struct.pack("I", x)
        sport_food.write(new_2)
"""