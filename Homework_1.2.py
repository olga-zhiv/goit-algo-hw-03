
import random     # Імпортуємо необхідний модуль


def get_numbers_ticket(min, max, quantity):     # Оголошуємо функцію, для отримання випадкових чисел




    if min < 1 or max > 1000:    # Мінімальне число не повинно бути менше 0, а максимальне більше 1000, в іншому випадку виводиться порожній список
        return [] 
    

    if min > max:     # Мінімальне число повинно бути не більше максимального
        return []
    

    if quantity < 1 or quantity > (max - min + 1):    # Кількість випадкових чисел не повинна бути менше від min, і не більше max
        return []
    



    numbers = random.sample(range(min, max + 1), quantity)    # Створення ипадкових чисел

    return sorted(numbers)     # Повернення відсортованого списку





ticket = get_numbers_ticket(1, 1000, 6)     # Виклик функції get_numbers_ticke

print("Ваші лотерейні числа:", ticket)
