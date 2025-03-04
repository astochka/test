phone_book = {"іван": "123-456-789", "марія": "987-654-321"}

while True:
    cmd = input("1-Додати, 2-Знайти, 3-Видалити, 4-Вийти: ")

    if cmd == '1':
        phone_book[input("Ім'я: ")] = input("Телефон: ")
    elif cmd == '2':
        print(phone_book.get(input("Ім'я: "), "Не знайдено"))
    elif cmd == '3':
        del phone_book[input("Ім'я: ")]  # Видаляємо без перевірки
    elif cmd == '4':
        break





