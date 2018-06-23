from glob import glob
from xlrd import open_workbook

dataDirectory = 'Ontario2018GeneralElectionResults_raw'
dataFiles = glob(dataDirectory + '/*.xls')
dataFiles.sort()

def candidate_info(row):
    print('candidate_name:', row[7])
    print('party:', row[6])
    print('num_votes:', int(row[4]))
    print('percent_votes:', row[5])

sheet = open_workbook(dataFiles[0]).sheet_by_index(0);

print('Riding:', sheet.cell_value(12, 0))
print()
print('Winner:')
candidate_info(sheet.row_values(11))
print()
print('Other Candidates:')

for row_index in range(16, sheet.nrows, 3):
    candidate_info(sheet.row_values(row_index))
    print()

#for row_index in range(sheet.nrows):
#    for col_index in range(sheet.ncols):
#        cell = sheet.cell_value(row_index, col_index);
#        if cell != '':
#            print(row_index, col_index, cell)

# 12, 1 - Riding name
# 11, 3 - Plurality
# column 4 - votes
#        5 - %
#        6 - Party
#        7 - Candidate Name
# First row is 11, next is 16, next is 19, next is 22
