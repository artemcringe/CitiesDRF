from datetime import time

from random import randrange, choice
from .models import *

cities = ['Москва', 'Санкт-Петербург', 'Новосибирск', 'Екатеринбург', 'Нижний Новгород', 'Казань', 'Челябинск',
          'Омск', 'Самара', 'Уфа', 'Красноярск', 'Пермь', 'Воронеж', 'Волгоград', 'Краснодар',
          'Саратов', 'Тюмень', 'Тольятти', 'Ижевск']

streets = ['площадь Горького', 'переулок Маяковского', 'улица Мира', 'проспект Московская', 'проезд Комсомольская',
           'площадь Советская', 'бульвар Кирова', 'улица Ленина', 'переулок Карла Маркса', 'площадь Горная',
           'проезд Мичурина', 'улица Лермонтова', 'площадь Фрунзе', 'переулок Садовая', 'площадь Октябрьская',
           'улица Коммунистическая', 'бульвар Свердлова', 'улица Пушкина', 'проезд Гагарина', 'проспект Красная']

shops = ["Ларисочка", "Пятерочка", "Вкусно и точка", "Вкусно и запятая", "Четверочка", "Копеечка", "Дикси", "Магнит",
         "Буря", "У Андрея", "Шашлычкофф", "Домашний", "У дома", "Рядом", "Дешевый", ]


def seed_cities():
    for city in cities:
        City.objects.create(city_name=city)
        print(f'Город {city} был сохранен')


def seed_streets():
    for city in cities:
        for street in streets:
            Street.objects.create(city=City.objects.filter(city_name=city).first(),
                                  street_name=street)
            print(f'Улица {street} для {city} сохранена')


def seed_shops():
    for city in cities:
        for j in range(randrange(20, 50)):
            Shop.objects.create(shop_name=choice(shops),
                                city=City.objects.filter(city_name=city).first(),
                                street=Street.objects.filter(street_name=choice(streets)).first(),
                                house_number=randrange(1, 100),
                                open=time(randrange(6, 10), 0),
                                close=time(randrange(16, 23), 0)
                                )
            print('есть')
