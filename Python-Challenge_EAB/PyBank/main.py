#PyBank code

import csv
import os

budget_data = os.path.join("Resources","budget_data.csv")
with open(budget_data) as budgetfile:
    csvreader = csv.reader(budgetfile, delimiter=',')
    #Check csv file
    #print(csvreader)
    #csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

#Total Number of Votes Cast


#Complete List of Candidates


#Percentage of votes for each Candidate


#Total Number of votes for each Candidate


#Election Winner


#Print Election Analysis


#Export Results as Text File

