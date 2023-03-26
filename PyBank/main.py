#Import necessary dependancies
import os
import csv

#set path for file
budget_data_csv =os.path.join("Resources","budget_data.csv")

#Created variables for months, total profit, list that contains the changes, previous value to get change values,
#and greatest increase/decrease.
count = 0
net_profit = 0
changes = []  
prev = 0
greatest_increase = 0
greatest_decrease = 0


#open and read CSV
with open(budget_data_csv) as csv_file:
    csv_reader = csv.reader(csv_file,delimiter=",")
    next(csv_reader)
    for row in csv_reader:
        count = 1 + count
        #Calculated months

        net_profit = int(row[1]) + net_profit
        #Calculated net profit

        curr = int(row[1]) - prev
        prev = int(row[1])
        #Got values in order to get the change value

        changes.append(curr)
        #Added the values to the changes list

        if curr > greatest_increase:
            greatest_increase = curr
            date = row[0]
            #Getting the date and max change value

        if curr < greatest_decrease:
            greatest_decrease = curr
            dates = row[0]
            #Getting the date and min change value

    changes[0] = 0
    #First value had to be 0 because there was no previous value for the first row.

    avg = round(sum(changes)/(len(changes) - 1), 2)
    #Calculated average change.

output = open("output.txt", "a")

with open("output.txt", "w") as output:
    output.write("Financial Analysis" + "\n")
    output.write("--------------------" + "\n")
    output.write("Total Months: " + str(count) + "\n")
    output.write("Total: $" + str(net_profit) + "\n")
    output.write("Average Change: $" + str(avg) + "\n")
    output.write("Greatest Increase in Profits: " + date + " ($" + str(greatest_increase) + ")" + "\n")
    output.write("Greatest Decrease in Profits: " + dates + " ($" + str(greatest_decrease) + ")")

output.close()
#All of this creates a new file called output.txt and puts the necessary values in the file.

contents = open("output.txt", "r")
print(contents.read())
contents.close()

