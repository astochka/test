films = []

while True:
    cmd = input("Додати (+), Видалити (-), Показати (?), Вихід (x): ").strip()

    if cmd == "+":
        films.append(input("Назва фільму: ").strip())
    elif cmd == "-":
        film = input("Який фільм видалити? ").strip()
        if film in films:
            films.remove(film)
    elif cmd == "?":
        print("\n".join(films) if films else "Список порожній.")
    elif cmd == "x":
        break
    else:
        print("невірна команда,спробуй ще раз")