

from datetime import date, datetime  # Імпортуємо необхідні модулі




def get_days_from_today(date):  # Оголошуємо функцію, яка запитує дату та обчислює різницю між введеною та поточною.

    current_datetime = date.today()  # Визначаємо поточну дату




    try:   # Обробка можливих помилок вводу дати

        date_string = input( "Введіть дату y форматі: %Y.%m.%d")   # Введення користувачем дати

        datetime_object = datetime.strptime(date_string, "%Y.%m.%d").date()  # Форматування дати із строки в об'єкт

        new_date = (datetime_object - current_datetime).days    # Обчислення різниці дат

        print(f" Різниця між датами становить: {new_date} днів")  # Вивід кількості днів користувачу


    except ValueError: 
        print("Введіть дату y вірному форматі: %Y.%m.%d")    # Якщо формат введення дати невірний, то на екрані з'явиться відповідний запис




get_days_from_today(date)  # Виклик функції
