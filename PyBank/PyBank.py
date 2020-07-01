#PyPoll Homework 
# import dependencies
import csv
import os

# define data path
budget_data = os.path.join("Resources","budget_data.csv")

# Read the csv and create variables
with open(budget_data) as budgetfile:
    reader = csv.reader(budgetfile, delimiter=',')


    csv_header = next(reader)
    profits_losses = []
    months = []
    net_total = []
    profit_change = []

#Here a for loop loops through the rows, adding to the profits, months, and total variables
    for row in reader:

        profits_losses.append(float(row[1]))
        months.append(row[0])
        net_total = sum(profits_losses)
# Another for loop goes through the profits and losses creating a variable for the difference between each consecutive month

    for i in range(1,len(profits_losses)):
        profit_change.append(profits_losses[i] - profits_losses[i-1])
        avg_profit_change = sum(profit_change)/len(months)

#Creating a variable for the max and min change and the months they occurred
        max_profit_change = max(profit_change)

        min_profit_change = min(profit_change)

        max_profit_change_date = str(months[profit_change.index(max(profit_change))])
        min_profit_change_date = str(months[profit_change.index(min(profit_change))])

#Writing for Financial Analysis
output = (
    f'\nFinancial Analysis\n'
    f'-----------------------\n'
    f'Total Months: {len(months)}\n'
    f'Total: ${round(net_total)}\n'
    f'Average Change: ${round(avg_profit_change)}\n'
    f'Greatest Increase in Profits: {max_profit_change_date} (${max_profit_change})\n'
    f'Greatest Decrease in Profits: {min_profit_change_date} (${min_profit_change})\n')

#Print Output to terminal
print(output)

#Export Output to a text file
file = open("PyBank_Ouput.txt","w+")
file.write(output)
file.close
#PyBank_Output = os.path.join("Analysis")
#with open(PyBank_Output) as txt_file:
    #PyBank_Output.write(output)
#PyBank_Output.close
