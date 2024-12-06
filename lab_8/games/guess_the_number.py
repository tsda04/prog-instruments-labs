import random

def guess_the_number():
    print("Добро пожаловать в игру 'Угадай число'!")
    number_to_guess = random.randint(-100, 100)  # Изменено на диапазон от -100 до 100
    attempts = 0

    while True:
        guess = input("Введите число от -100 до 100 (или 'выход' для завершения игры): ")
        if guess.lower() == 'выход':
            print("Вы вышли из игры.")
            break

        attempts += 1
        try:
            guess = int(guess)
        except ValueError:
            print("Пожалуйста, введите корректное число.")
            continue

        # Проверка на близость
        difference = abs(number_to_guess - guess)

        if difference == 0:
            print(f"Поздравляем! Вы угадали число {number_to_guess} за {attempts} попыток.")
            break
        elif difference <= 5:
            print("Очень горячо! Вы очень близки к правильному числу.")
        elif difference <= 10:
            print("Горячо! Вы близки к правильному числу.")
        elif difference <= 20:
            print("Тепло. Вы находитесь в пределах 20.")
        elif guess < number_to_guess:
            print("Слишком маленькое число. Попробуйте снова.")
        elif guess > number_to_guess:
            print("Слишком большое число. Попробуйте снова.")
        else:
            print("Вы далеко от правильного ответа. Попробуйте снова.")