

from datetime import date, datetime  # Імпортуємо необхідні модулі




def get_days_from_today(date):  # Оголошуємо функцію, яка запитує дату та обчислює різницю між введеною та поточною.

    current_datetime = date.today()  # Визначаємо поточну дату




    try:   # Обробка можливих помилок вводу дати

        datetime_object = datetime.strptime(date_string, "%Y.%m.%d").date()  # Форматування дати із строки в об'єкт

        new_date = (datetime_object - current_datetime).days    # Обчислення різниці дат

        return new_date  # Повернення кількості днів


    except ValueError: 
        print("Введіть дату y вірному форматі: %Y.%m.%d")    # Якщо формат введення дати невірний, то на екрані з'явиться відповідний запис




days = get_days_from_today("2025.03.29")  # Виклик функції
print(days)
