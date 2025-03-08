from random import uniform

target = round(uniform(1, 10), 2)
print("Відгадай число від 1 до 10 (з точністю до двох знаків). Введи 'я лох,здаюся', щоб побачити відповідь.")

while True:
    guess = input("Твоє число: ")

    if guess.lower() == "я лох,здаюся":
        print(f"Ти здався! Загадане число було: {target}")
        break

    try:
        guess = round(float(guess), 2)
        if guess == target:
            print("Вітаю! Ти вгадав!")
            break
        print("Більше!" if guess < target else "Менше!")
    except ValueError:
        print("Введи правильне число або 'здаюся'!")