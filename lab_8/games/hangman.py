import random

def display_hangman(tries):
    stages = [
        """
           ------
           |    |
           |    O
           |   /|\\
           |   / \\
           |
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |   /
           |
        """,
        """
           ------
           |    |
           |    O
           |   /|
           |
           |
        """,
        """
           ------
           |    |
           |    O
           |    |
           |
           |
        """,
        """
           ------
           |    |
           |    O
           |
           |
           |
        """,
        """
           ------
           |    |
           |
           |
           |
           |
        """,
        """
           ------
           |
           |
           |
           |
           |
        """
    ]
    return stages[tries]

def hangman():
    words = ["python", "программирование", "виселица", "игра", "разработка"]
    word = random.choice(words)  # Загадать случайное слово
    word_completion = "_" * len(word)  # Скрытое слово
    guessed = False  # Угадано ли слово
    guessed_letters = []  # Угаданные буквы
    tries = 6  # Количество попыток

    print("Давайте играть в Виселицу!")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")

    while not guessed and tries > 0:
        guess = input("Угадайте букву: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Пожалуйста, введите одну букву.")
            continue

        if guess in guessed_letters:
            print("Вы уже угадывали эту букву. Попробуйте другую.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Хорошо! Буква есть в слове.")
            word_completion = "".join([letter if letter in guessed_letters else "_" for letter in word])
        else:
            print("Увы, такой буквы нет в слове.")
            tries -= 1

        print(display_hangman(tries))
        print(word_completion)
        print("\n")

        if "_" not in word_completion:
            guessed = True

    if guessed:
        print("Поздравляем! Вы угадали слово:", word)
    else:
        print("Вы проиграли. Загаданное слово было:", word)

if __name__ == "__main__":
    hangman()