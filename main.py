import csv
import os
from tabulate import tabulate
import pandas as pd
import random
import json


def csv_check(path):
    csv_exists = os.path.exists(path)
    return csv_exists


def create_csv():
    with open('workouts.csv', 'w') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow(['Date', 'Name', 'Workouts'])


def csv_updater():
    workouts = ['legs', 'push', 'pull']
    df = pd.read_csv('workouts.csv')
    last_two_workouts = (df['Name'].iloc[-1], df['Name'].iloc[-2])
    for workout in workouts:
        if workout not in last_two_workouts:
            wod = workout
            print(f'The wod today is: {wod}')
    return wod


def write_to_csv(wod):
    f = open('exercises.json')
    data = json.load(f)
    for exercise in data['exercises']:
        if exercise['name'] == wod:
            print(exercise)


def data_tabulate():
    df = pd.read_csv('workouts.csv')
    data = tabulate(df, headers='keys', tablefmt='simple')


def main():
    # check csv file
    if not csv_check('workouts.csv'):
        create_csv()
    wod_today = csv_updater()
    write_to_csv(wod_today)
    data_tabulate()


if __name__ == '__main__':
    main()
