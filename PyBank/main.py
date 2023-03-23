import os
import csv
#set path for file

budget_data_csv =os.path.join("Resources","budget_data.csv")

#open and read CSV
with open(budget_data_csv) as csv_file:
    csv_reader=csv.reader(csv_file,delimiter=",")
    