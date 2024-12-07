import os
from typing import List
from log_filter import (
    filter_logs_time,
)


def create_output_directory(directory: str) -> None:
    """
    Создает директорию для выходных файлов, если она не существует.

    Parameters:
        directory (str): Путь к директории для выходных файлов.
    """
    os.makedirs(directory, exist_ok=True)


def filter_logs_by_time(input_file: str, output_file: str, start_time: str, end_time: str) -> None:
    """
    Фильтрует логи по времени и сохраняет результат в выходной файл.

    Parameters:
        input_file (str): Путь к входному файлу с логами.
        output_file (str): Путь к выходному файлу для записи отфильтрованных логов.
        start_time (str): Начальное время для фильтрации.
        end_time (str): Конечное время для фильтрации.
    """
    filter_logs_time(start_time, end_time, input_file, output_file)
    print(f"Фильтрация по времени завершена. Отфильтрованные логи сохранены в '{output_file}'.")


def main() -> None:
    input_file = 'logs.txt'                   # Имя входного файла с логами
    output_directory = 'output'               # Директория для выходных файлов

    create_output_directory(output_directory)

    print("-----------------")

    # Фильтрация по времени
    start_time = '2024-12-07 19:09:20,000'  # Начальное время
    end_time = '2024-12-07 19:09:40,000'    # Конечное время
    output_file1 = os.path.join(output_directory, 'filtered_logs1.txt')
    filter_logs_by_time(input_file, output_file1, start_time, end_time)

    print("-----------------")


if __name__ == "__main__":
    main()
