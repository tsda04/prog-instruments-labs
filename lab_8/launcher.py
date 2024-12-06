import importlib


class GameLauncher:

    def __init__(self):
        """Инициализация игрового лаунчера с доступными играми."""
        self.games = {
            "Угадай число": "games.guess_the_number",
            "Крестики-нолики": "games.tic_tac_toe",
            "Виселица": "games.hangman",
            "2048": "games.game_2048",
            "Лабиринт": "games.maze"
        }

    def display_games(self):
        """Отображение доступных игр."""
        print("Доступные игры:")
        for game in self.games.keys():
            print(f"- {game}")

    def launch_game(self, selected_game):
        """Запуск выбранной игры."""
        game_module_name = self.games.get(selected_game)

        if game_module_name:
            game_module = importlib.import_module(game_module_name)
            game_module_function = getattr(game_module, selected_game.replace(" ", "_").lower())
            game_module_function()
        else:
            print("Извините, такой игры нет. Пожалуйста, выберите из списка.")

    def run(self):
        """Основной игровой процесс."""
        while True:
            self.display_games()
            selected_game = input(
                "Введите название игры, в которую хотите поиграть (или 'выход' для завершения): "
            )

            if selected_game.lower() == "выход":
                print("Спасибо за игру! До свидания!")
                break

            self.launch_game(selected_game)


if __name__ == "__main__":
    game_launcher = GameLauncher()
    game_launcher.run()
