import random
import os

def init_game():
    """Инициализация игровой доски."""
    board = [[0] * 4 for _ in range(4)]
    add_new_tile(board)
    add_new_tile(board)
    return board

def add_new_tile(board):
    """Добавление новой плитки (2 или 4) на доску."""
    x, y = random.randint(0, 3), random.randint(0, 3)
    while board[x][y] != 0:
        x, y = random.randint(0, 3), random.randint(0, 3)
    board[x][y] = random.choice([2, 4])

def print_board(board):
    """Вывод игровой доски на экран."""
    os.system('cls' if os.name == 'nt' else 'clear')
    for row in board:
        print("\t".join(str(num) if num != 0 else "." for num in row))
        print()

def slide_and_merge(row):
    """Сдвиг и объединение плиток в строке."""
    new_row = [num for num in row if num != 0]
    merged_row = []
    skip = False

    for i in range(len(new_row)):
        if skip:
            skip = False
            continue
        if i < len(new_row) - 1 and new_row[i] == new_row[i + 1]:
            merged_row.append(new_row[i] * 2)
            skip = True
        else:
            merged_row.append(new_row[i])

    merged_row += [0] * (len(row) - len(merged_row))
    return merged_row

def move(board, direction):
    """Перемещение плиток в заданном направлении."""
    if direction in ('w', 's'):
        board = [list(row) for row in zip(*board)]  # Транспонируем для вертикального движения

    if direction in ('s', 'd'):
        board = [row[::-1] for row in board]  # Реверсируем строки для движения вниз и вправо

    new_board = []
    for row in board:
        new_row = slide_and_merge(row)
        new_board.append(new_row)

    if direction in ('s', 'd'):
        new_board = [row[::-1] for row in new_board]  # Реверсируем обратно

    if direction in ('w', 's'):
        new_board = [list(row) for row in zip(*new_board)]  # Транспонируем обратно

    return new_board

def is_game_over(board):
    """Проверка, закончилась ли игра."""
    for row in board:
        if 2048 in row:
            print("Поздравляем! Вы выиграли!")
            return True
        if 0 in row:
            return False
    for i in range(4):
        for j in range(3):
            if board[i][j] == board[i][j + 1] or board[j][i] == board[j + 1][i]:
                return False
    print("Игра окончена! Попробуйте еще раз.")
    return True

def game_2048():
    """Основная функция игры 2048."""
    board = init_game()
    while True:
        print_board(board)
        move_input = input("Введите направление (w/a/s/d для вверх/влево/вниз/вправо, q для выхода): ").lower()

        if move_input in ('w', 'a', 's', 'd'):
            new_board = move(board, move_input)
            if new_board != board:
                board = new_board
                add_new_tile(board)
            if is_game_over(board):
                break
        elif move_input == 'q':
            print("Вы вышли из игры.")
            break
        else:
            print("Неверный ввод! Пожалуйста, используйте w/a/s/d или q.")

if __name__ == "__main__":
    game_2048()