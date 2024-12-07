import random
import os


class Game2048:
    def __init__(self):
        self.board = self.init_game()

    def init_game(self):
        """Инициализация игровой доски."""
        board = [[0] * 4 for _ in range(4)]
        self.add_new_tile(board)
        self.add_new_tile(board)
        return board

    def add_new_tile(self, board):
        """Добавление новой плитки (2 или 4) на доску."""
        x, y = random.randint(0, 3), random.randint(0, 3)
        while board[x][y] != 0:
            x, y = random.randint(0, 3), random.randint(0, 3)
        board[x][y] = random.choice([2, 4])

    def print_board(self):
        """Вывод игровой доски на экран."""
        os.system("cls" if os.name == "nt" else "clear")
        for row in self.board:
            print("\t".join(str(num) if num != 0 else "." for num in row))
            print()

    def slide_and_merge(self, row):
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

    def move(self, direction):
        """Перемещение плиток в заданном направлении."""
        board = self.board
        if direction in ("w", "s"):
            board = [list(row) for row in zip(*board)]  # Транспонируем для вертикального движения

        if direction in ("s", "d"):
            board = [row[::-1] for row in board]  # Реверсируем строки для движения вниз и вправо

        new_board = []
        for row in board:
            new_row = self.slide_and_merge(row)
            new_board.append(new_row)

        if direction in ("s", "d"):
            new_board = [row[::-1] for row in new_board]  # Реверсируем обратно

        if direction in ("w", "s"):
            new_board = [list(row) for row in zip(*new_board)]  # Транспонируем обратно

        return new_board

    def is_game_over(self):
        """Проверка, закончилась ли игра."""
        for row in self.board:
            if 2048 in row:
                print("Поздравляем! Вы выиграли!")
                return True
            if 0 in row:
                return False
        for i in range(4):
            for j in range(3):
                if (self.board[i][j] == self.board[i][j + 1] or
                        self.board[j][i] == self.board[j + 1][i]):
                    return False
        print("Игра окончена! Попробуйте еще раз.")
        return True

    def play(self):
        """Основная функция игры 2048."""
        while True:
            self.print_board()
            move_input = input(
                "Введите направление (w/a/s/d для вверх/влево/вниз/вправо, q для выхода): "
            ).lower()

            if move_input in ("w", "a", "s", "d"):
                new_board = self.move(move_input)
                if new_board != self.board:
                    self.board = new_board
                    self.add_new_tile(self.board)
                if self.is_game_over():
                    break
            elif move_input == "q":
                print("Вы вышли из игры.")
                break
            else:
                print("Неверный ввод! Пожалуйста, используйте w/a/s/d или q.")


def game_2048():
    game = Game2048()
    game.play()
