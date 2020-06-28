#PyPoll code

import csv
import os

election_data = os.path.join("Resources","election_data.csv")
with open(election_data) as electionfile:
    csvreader = csv.reader(electionfile, delimiter=',')
    #Check csv file
    #print(csvreader)
    #csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

#Total Months in Dataset


#Net Total "Profits/Losses"


#Average Changes "Profits/Losses"


#Date and Amount of Greatest increase


#Date and Amount of Greatest increase


#Print Financial Analysis


#Export Results as Text File
