#! /usr/bin/env python3

from datetime import datetime, timedelta
import argparse

EXERCISE_LOGS_FILE_PATH = "."


def summarize_by_day():
    days = {}

    with open(f'{EXERCISE_LOGS_FILE_PATH}/exercise_logs.csv') as f:
        for line in f.readlines():
            parts = line.split(",")
            day = parts[0]
            minutes = int(parts[1])

            day_sum = days.get(day, 0)
            days[day] = day_sum + minutes


        for day in days.keys():
            print(f'{day}: {days[day]}')


def summarize_by_week():
    weeks = {}

    with open(f'{EXERCISE_LOGS_FILE_PATH}/exercise_logs.csv') as f:
        for line in f.readlines():
            parts = line.split(",")
            day = parts[0]
            minutes = int(parts[1])

            day_datetime = datetime.strptime(day, "%Y-%m-%d")
            week_number = day_datetime.isocalendar()[1]

            week_sum = weeks.get(week_number, 0)
            weeks[week_number] = week_sum + minutes

        for week in weeks.keys():
            print(f"Week {week}:", weeks[week])


def run():
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", action="store_true", help="summarize by day")
    args = parser.parse_args()

    if args.d:
        summarize_by_day()
    else:
        summarize_by_week()


if __name__ == '__main__':
    run()

