import datetime as dt
from django.test import TestCase

from ..models import Record, City


class CityModelTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.city = City.objects.create(
            name='Саров'
        )
        cls.record = Record.objects.create(
            city=cls.city,
            date=dt.datetime.strptime('10.11.2021 07:00', "%d.%m.%Y %H:%M"),
            temperature=14.4,
            wind_direction=67.5,
            wind_speed=4,
            status='Осадки',
            precipitation=1.1
        )

    def test_verbose_name(self):
        field_verbose_record = {
            'city': 'Город',
            'date': 'Дата и время',
            'temperature': 'Температура',
            'wind_direction': 'Направление ветра в градусах',
            'wind_speed': 'Скорость ветра в м/с',
            'status': 'Погода',
            'precipitation': 'Атмосферные осадки в мм',
        }
        for field, expected_value in field_verbose_record.items():
            with self.subTest(field=field):
                self.assertEqual(
                    Record._meta.get_field(field).verbose_name, expected_value)