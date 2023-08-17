import subprocess
from datetime import datetime
from crontab import CronSlices
import os


def main():
    # Путь к файлу с расписанием
    schedule_file = os.path.expanduser("~/.planner/schedule.conf")

    # Проверка наличия директории
    if not os.path.exists(os.path.dirname(schedule_file)):
        os.makedirs(os.path.dirname(schedule_file))
        print('Создат пустой файл конфигурации')

    # Проверка наличия файла
    if not os.path.exists(schedule_file):
        with open(schedule_file, 'w') as file:
            file.write("# Ваш конфигурационный файл\n")

    # Чтение файла с расписанием
    # with open(schedule_file, 'r') as file:
    #     lines = file.readlines()

    # Получение текущего времени
    now = datetime.now()

    # Перебор строк в файлу с расписанием
    # for line in lines:
    #     if line.strip() and not line.startswith("#"):
    #         cron_time, script_path = line.strip().rsplit(' ', 1)
    #         cron_time = CronSlices(cron_time)
    #
    #         # Если текущее время совпадает с расписанием, запускаем скрипт
    #         if cron_time.match(now):
    #             subprocess.run(['python3', script_path])

    print(f"Checked schedule at {now.hour}:{now.minute}")


if __name__ == '__main__':
    main()
