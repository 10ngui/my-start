import csv

def sort_csv(input_csv, output_csv, sort_column):
    # Читаем CSV-файл
    with open(input_csv, 'r', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file)
        header = next(csv_reader)  # Сохраняем заголовок

        # Считываем данные и сортируем их по указанному столбцу
        sorted_data = sorted(csv_reader, key=lambda x: x[header.index(sort_column)])

    # Записываем отсортированные данные в новый CSV-файл
    with open(output_csv, 'w', newline='', encoding='utf-8') as sorted_csv_file:
        csv_writer = csv.writer(sorted_csv_file)

        # Записываем заголовок
        csv_writer.writerow(header)

        # Записываем отсортированные данные
        csv_writer.writerows(sorted_data)

    print(f"Сортировка завершена. Результат сохранен в {output_csv}")

# Укажите путь к вашему исходному CSV-файлу и желаемому имени для отсортированного файла
input_csv_path = 'результат.csv'
output_csv_name = 'отсортированный_результат.csv'

# Укажите столбец, по которому нужно сортировать
sort_column_name = 'identity'

# Вызываем функцию для сортировки
sort_csv(input_csv_path, output_csv_name, sort_column_name)
