def tic_tac_toe():
    board = [' ' for _ in range(9)]  # Инициализация пустого поля

    def print_board():
        print(f"{board[0]} | {board[1]} | {board[2]}")
        print("--+---+--")
        print(f"{board[3]} | {board[4]} | {board[5]}")
        print("--+---+--")
        print(f"{board[6]} | {board[7]} | {board[8]}")

    def check_winner():
        winning_combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Горизонтали
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Вертикали
            (0, 4, 8), (2, 4, 6)               # Диагонали
        ]
        for combo in winning_combinations:
            if board[combo[0]] == board[combo[1]] == board[combo[2]] != ' ':
                return board[combo[0]]
        return None

    current_player = 'X'
    for turn in range(9):
        print_board()
        move = int(input(f"Игрок {current_player}, выберите позицию (1-9): ")) - 1

        if move < 0 or move > 8 or board[move] != ' ':
            print("Некорректный ввод или позиция уже занята. Попробуйте снова.")
            continue

        board[move] = current_player
        winner = check_winner()
        if winner:
            print_board()
            print(f"Поздравляем! Игрок {winner} выиграл!")
            return

        current_player = 'O' if current_player == 'X' else 'X'

    print_board()
    print("Игра закончилась вничью!")