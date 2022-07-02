import numpy
import pandas
import finta
import csv
import os
from pathlib import Path

companies = {}

for files in os.listdir('/Users/kevinzhou/Documents/share_prices'):
    f = os.path.join('/Users/kevinzhou/Documents/share_prices', files)
    with open(f) as cur_file:
        cur_data = []
        csv_reader = csv.reader(cur_file, delimiter=',')
        next(cur_file)
        for row in csv_reader:
            cur_data.append(row)
        companies["{}".format(Path(f).stem)] = cur_data

change_data = []

for cur_company1 in companies:
    counter = 0
    total = 0
    for cur_company2 in companies:
        for i in range(min(len(companies[cur_company2]), len(companies[cur_company1])) - 2):
            #if not isinstance(float(companies[cur_company2][i+1][1]), str):
                #print(cur_company2, companies[cur_company2][i+1][1])
            if companies[cur_company1][i+1][1] == 'null' or companies[cur_company1][i][1] == 'null' \
                or companies[cur_company2][i+2][1] =='null' or companies[cur_company2][i+1][1] == 'null':
                    continue
            diff1 = float(companies[cur_company1][i+1][1]) - float(companies[cur_company1][i][1])
            diff2 = float(companies[cur_company2][i+2][1]) - float(companies[cur_company2][i+1][1])
            if diff1 < 0 and diff2 < 0:
               counter += 1
            if diff1 > 0 and diff2 > 0:
               counter += 1
            total += 1
        rate = int(1000*float(counter/total))
        change_data.append([cur_company1, cur_company2, counter, total])
        print(f"{cur_company1}, {cur_company2}, {counter}, {total}, {rate}")

for row in change_data:
    # print(row)
    pass


def getMyPosition():
    com_rate = 0.005 #0.0050 * totalDollarVolumeTraded
    positions = []

    return positions

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
