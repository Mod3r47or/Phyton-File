# Пропишите нужные импорты
from datetime import datetime, timedelta

def get_weekday_name(weekday_number):
    if weekday_number == 0:
        return 'понедельник'
    elif weekday_number == 1:
        return 'вторник'
    elif weekday_number == 2:
        return 'среда'
    elif weekday_number == 3:
        return 'четверг'
    elif weekday_number == 4:
        return 'пятница'
    elif weekday_number == 5:
        return 'суббота'
    elif weekday_number == 6:
        return 'воскресенье'
    else:
        return 'неизвестный день'

def get_day_after_tomorrow(date_string):
    # Напишите код функции.
    date_today = datetime.strptime(date_string, '%Y-%m-%d')
    day_week_today = get_weekday_name(date_today.weekday())
    

    date_after_tomorrow = date_today + timedelta(days=2)
    day_week_after_tomorrow = get_weekday_name(date_after_tomorrow.weekday())
    
    print('Сегодня', date_today.strftime('%Y-%m-%d'), day_week_today, 'а послезавтра будет', day_week_after_tomorrow)

# Проверьте работу программы, можете подставить свои значения.
get_day_after_tomorrow('2024-01-01')
get_day_after_tomorrow('2024-01-02')
get_day_after_tomorrow('2024-01-03')
get_day_after_tomorrow('2024-01-04')
get_day_after_tomorrow('2024-01-05')
get_day_after_tomorrow('2024-01-06')