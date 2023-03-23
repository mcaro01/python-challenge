import os
import csv
#set path for file

election_data_csv =os.path.join("..", "Resources","election_data.csv")

votes_cast = 0
complete_list = []
count = 0
diana_vote = 0 
raymon_vote =0


#open and read CSV
with open(election_data_csv) as csv_file:
    csv_reader=csv.reader(csv_file,delimiter=",")
    next(csv_reader)
    for row in csv_reader:
        votes_cast = 1 + votes_cast
        if row[2] not in complete_list:
            complete_list.append(row[2])
        if row[2] == "Charles Casper Stockham":
            count = 1 + count
        elif row[2] == "Diana DeGette":
            diana_vote = 1 + diana_vote
        elif row[2] == "Raymon Anthony Doane":
            raymon_vote = 1 + raymon_vote
print(votes_cast)
#percentage = 
if count > diana_vote and raymon_vote > count:
    print(raymon_vote)
elif diana_vote > count and raymon_vote < diana_vote:
    print(diana_vote)
else:
    print(count)
print(Election Results)
print(--------------------)
print(Total Votes:)
print(---------------------)
print(Charles Casper Stockham)
print(Diana DeGrette:)
print(Raymon Anthony Doane)
print(-----------------------)
print(Winner: Diana DeGrette)



