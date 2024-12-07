import re


def filter_logs_time(start_time: str, end_time: str, input_file: str, output_file: str) -> None:
    """
    Фильтрует строки логов по заданному диапазону времени и записывает их в выходной файл.

    Parameters:
        start_time (str): Начальное время в формате 'YYYY-MM-DD HH:MM:SS,SSS'.
        end_time (str): Конечное время в формате 'YYYY-MM-DD HH:MM:SS,SSS'.
        input_file (str): Путь к входному файлу с логами.
        output_file (str): Путь к выходному файлу, куда будут записаны отфильтрованные логи.

    Returns:
        None: Функция ничего не возвращает, но записывает отфильтрованные логи в выходной файл.
    """
    # Регулярное выражение для поиска строк логов
    log_pattern = re.compile(r'^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3} - (.+)')

    # Создание выходного файла, если он не существует
    with open(output_file, 'w', encoding='utf-8') as outfile:
        # Чтение входного файла
        with open(input_file, 'r', encoding='utf-8') as infile:
            for line in infile:
                match = log_pattern.match(line)
                if match:
                    # Извлекаем временную метку
                    timestamp = line.split(' - ')[0]
                    # Проверяем, попадает ли временная метка в указанный диапазон
                    if start_time <= timestamp <= end_time:
                        outfile.write(line)
