from day import Day
from gift import Gift
import random

class Controller:
    @staticmethod
    def set_days(start=1, end=25) -> list:
        days = []
        for i in range(start, end):
            day = Day()
            day.set_value(i)
            days.append(day)
        return days
    
    def validate_value(func):
        def wrapper(days, value, *args, **kwargs):
            if days[value-1].value == 0:
                raise ValueError("this day is already selected")
            return func(days, value, *args, **kwargs)
        return wrapper
        
    @staticmethod
    @validate_value
    def change_day_to_selected(days: list, value: int) -> None:
        days[value-1].select()
        return days

    @staticmethod
    def get_a_gift(days: list, value: int) -> None:
        days[value-1].gift = random.choice(Gift.GIFTS)
        return random.choice(Gift.GIFTS)