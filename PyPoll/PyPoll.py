#PyPoll code for Python-Challenge Homework
#Emma Braden        due 6/30/2020
#Using election data, PyPoll.py creates values for each of the candidates and counts their occurrences in the set in order to determine their share of the votes across counties as well as the overall winner. The results are printed in the terminal and exported in a text file.

#import dependencies in order to read csv files
import csv
import os

#create file path and read the csv file
election_data = os.path.join("Resources","election_data.csv")
with open(election_data) as electionfile:
    csvreader = csv.reader(electionfile, delimiter=',')
    
#Create empty variables and lists
total_votes = 0
candidate_name = []
khan_count = 0
correy_count = 0
li_count = 0
otooley_count = 0

#Loop through rows in the dataset
with open(election_data) as electionfile:
    csvreader = csv.reader(electionfile, delimiter=',')
    if csv.Sniffer().has_header:
        next(csvreader)
    for row in csvreader:
#Total Number of Votes Cast
        total_votes += 1
#Put Candidate names in list and count total votes for each candidate
        if row[2] not in candidate_name:
            candidate_name.append(row[2])
        if row[2] == "Khan":
            khan_count +=1
        if row[2] == "Correy":
            correy_count +=1
        if row[2] == "Li":
            li_count +=1
        if row[2] == "O'Tooley":
            otooley_count +=1

#calculate percentages
khan_pct = (khan_count/total_votes)*100
correy_pct = (correy_count/total_votes)*100
li_pct = (li_count/total_votes)*100
otooley_pct = (otooley_count/total_votes)*100


#Election Winner using conditionals to determine candidate with popular vote
if khan_pct > 50:
    winner = "Khan"
elif correy_pct > 50:
    winner = "Correy"
elif li_pct > 50:
    winner = "Li"
elif otooley_pct > 50:
    winner = "O'Tooley"

#format variables for output
output = (
    f'\nElection Results\n'
    f'-----------------------\n'
    f'Total Votes: {total_votes}\n'
    f'-----------------------\n'
    f'Khan:{round(khan_pct,3)}% ({khan_count})\n'
    f'Correy:{round(correy_pct,3)}% ({correy_count})\n'
    f'Li:{round(li_pct,3)}% ({li_count})\n'
    f'OTooley:{round(otooley_pct,3)}% ({otooley_count})\n'
    f'-----------------------\n'
    f'Winner: {winner}\n'
    f'-----------------------\n')


#Print Election Analysis
print(output)

#Export Results as Text File
file = open("PyPoll_Ouput.txt","w+")
file.write(output)
file.close

