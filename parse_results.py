from glob import glob
from xlrd import open_workbook
import csv

dataDirectory = 'Ontario2018GeneralElectionResults_raw'
dataFiles = glob(dataDirectory + '/*.xls')
dataFiles.sort()

header = ['Candidate Name',
          'Riding',
          'Party',
          'Votes Count',
          'Votes Percent',
          'Elected',
          'Win Margin Count',
          'Win Margin Percent']

def candidate_info(row, riding):
    return [row[7], # candidate name
            riding, # riding
            row[6], # party
            int(row[4]), # votes count
            row[5], # votes percent
            False, # elected (default)
            '', # win margin count (default)
            ''] # win margin percent (default)

def total_votes(sheet):
    return sum([x for x in sheet.col_values(4) if isinstance(x, float)]);


with open('candidates.csv', 'w', newline='') as csvfile:
    output = csv.writer(csvfile, quoting=csv.QUOTE_MINIMAL)
    output.writerow(header)

    for dataFile in dataFiles:
        sheet = open_workbook(dataFile).sheet_by_index(0);
        riding = sheet.cell_value(12, 0)

        winner = candidate_info(sheet.row_values(11), riding)
        winner[5] = True
        winner[6] = sheet.cell_value(11, 3)
        winner[7] = round(100*sheet.cell_value(11, 3)/total_votes(sheet), 1)
        output.writerow(winner)

        for row_index in range(16, sheet.nrows, 3):
            output.writerow(candidate_info(sheet.row_values(row_index), riding))
