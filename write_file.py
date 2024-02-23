import json
import csv


def write_to_file(file_format):
    def decorator(func):
        def wrapper(*args, **kwargs):
            # Создаем строку с таблицей
            table = func(*args, **kwargs)
            if file_format == 'json':
                with open("processes_table.json", "w") as file:
                    json.dump(table, file)
                print('Таблица с информацией о процессах была успешно записана в файл "processes_table.json".')
            elif file_format == 'csv':
                with open("processes_table.csv", "w", newline='') as file:
                    csv_write = csv.writer(file)
                    header = table[0].keys()
                    csv_write.writerow(header)
                    for row in table:
                        csv_write.writerow(row.values())
                print('Таблица с информацией о процессах была успешно записана в файл "processes_table.csv".')
            else:
                print('Формат файла не поддерживается. Выберите "json" или "csv".')
            return table
        return wrapper
    return decorator
