#Import necessary dependancies
import os
import csv

#set path for file
election_data_csv = os.path.join("Resources","election_data.csv")

#Created variables for the total votes, votes per candidate and a candidate list.
votes_cast = 0
complete_list = []
count = 0
diana_vote = 0 
raymon_vote = 0

#open and read CSV
with open(election_data_csv) as csv_file:
    csv_reader=csv.reader(csv_file,delimiter=",")
    next(csv_reader)
    for row in csv_reader:
        votes_cast = 1 + votes_cast
        #Getting the total votes

        if row[2] not in complete_list:
            complete_list.append(row[2])
            #This code each unique candidate.

        if row[2] == "Charles Casper Stockham":
            count = 1 + count
        elif row[2] == "Diana DeGette":
            diana_vote = 1 + diana_vote
        elif row[2] == "Raymon Anthony Doane":
            raymon_vote = 1 + raymon_vote
        #This if/elif block is to count the votes for each candidate

percentage_c = round((count/votes_cast)*100, 3)
percentage_d = round((diana_vote/votes_cast)*100, 3)
percentage_r = round((raymon_vote/votes_cast)*100, 3)
#These pieces of code shows the percentage of votes cast for each candidate

if count > diana_vote and raymon_vote > count:
    result = "Charles Casper Stockham"
elif diana_vote > count and raymon_vote < diana_vote:
    result = "Diana DeGrette"
else:
    result = "Raymon Anthony Doane"
#This if/elif block gives the winner of the election

output = open("output.txt", "a")

with open("output.txt", "w") as output:
    output.write("Election Results" + "\n")
    output.write("--------------------" + "\n")
    output.write("Total Votes: " + str(votes_cast) + "\n")
    output.write("---------------------" + "\n")
    output.write("Charles Casper Stockham: " + str(percentage_c) + "% " + "(" + str(count) + ")" + "\n")
    output.write("Diana DeGrette: " + str(percentage_d) + "% " + "(" + str(diana_vote) + ")" + "\n")
    output.write("Raymon Anthony Doane: " + str(percentage_r) + "% " + "(" + str(raymon_vote) + ")" + "\n")
    output.write("-----------------------" + "\n")
    output.write("Winner: " + result)

output.close()
#All of this creates a new file called output.txt and puts the necessary values in the file.

contents = open("output.txt", "r")
print(contents.read())
contents.close()
#This reads output.txt and prints it to the terminal