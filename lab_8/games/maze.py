def maze():
    maze_layout = [
        "#########",
        "#       #",
        "# ##### #",
        "# #   # #",
        "# # # # #",
        "#   #   #",
        "#########"
    ]

    player_pos = [1, 1]  # Начальная позиция игрока
    exit_pos = [5, 7]    # Позиция выхода

    def print_maze():
        for i in range(len(maze_layout)):
            row = list(maze_layout[i])
            if player_pos[0] == i:
                row[player_pos[1]] = 'P'  # Отображаем игрока
            print("".join(row))

    while True:
        print_maze()

        if player_pos == exit_pos:
            print("Поздравляю! Вы нашли выход!")
            break

        move = input("Введите ваше движение (W - вверх, S - вниз, A - влево, D - вправо): ").lower()

        if move == "w":  # Вверх
            new_pos = [player_pos[0] - 1, player_pos[1]]
        elif move == "s":  # Вниз
            new_pos = [player_pos[0] + 1, player_pos[1]]
        elif move == "a":  # Влево
            new_pos = [player_pos[0], player_pos[1] - 1]
        elif move == "d":  # Вправо
            new_pos = [player_pos[0], player_pos[1] + 1]
        else:
            print("Неверное движение! Попробуйте снова.")
            continue

        # Проверяем, можно ли переместиться на новую позицию
        if maze_layout[new_pos[0]][new_pos[1]] == ' ':
            player_pos = new_pos
        else:
            print("Вы не можете пройти через стену!")