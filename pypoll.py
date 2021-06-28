#data to retrieve

#1.Total number of votes cast 

#2 list of candidates who received votes

#3 total number of votes per candidate 

#4 % of votes each candidate won 

#5 winner of the election based on popular vote

#Add dependencies
import csv
import os

#assign a variable to load a file from a path
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:

# To do: read and analyze data here.

     # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    #Print the header row.
    headers = next(file_reader)
    print(headers)


    