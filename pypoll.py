#Add dependencies
import csv
import os
#assign a variable to load a file from a path
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")
#Initialize total vote counter
total_votes = 0 

#declare a new list for candidate names 
candidate_options = []
#declare cadidates votes dictionary
candidate_votes = {}

# Track the winning candidate, vote count, and percentage.
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
     # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    #Read the header row.
    headers = next(file_reader)
    
    #Print each row in the csv file
    for row in file_reader:
        #Add to the total vote count 
        total_votes += 1

        
        # get the candidate name for each row. 
        candidate_name = row[2]
    
        #If the candidate does not match any existing candidate
        if candidate_name not in candidate_options:
            #Add name to the list of candidates
            candidate_options.append(candidate_name)

            # Begin tracking that candidate's vote count
            candidate_votes[candidate_name] = 0

         # Add a vote to that candidate's count 
        candidate_votes[candidate_name] += 1

#save the results to your text file.
with open(file_to_save, "w") as text_file:
    #Print the final vote count to the terminal
    election_results = (
        f"\nElection Results\n"
        f"-------------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------------\n")
    print(election_results, end="")
        #save the final vote count to the text file 
    text_file.write(election_results)

    # Determine the percentage of votes for each candidate by looping through the counts.
    # Iterate through the candidate list.
    for candidate_name in candidate_votes:
     # 2. Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]
        # 3. Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100

        candidate_results= (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        # Print each candidate, their voter count, and percentage to the terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        text_file.write(candidate_results)

        # Determine winning vote count and candidate
        # 1. Determine if the votes are greater than the winning count.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
            # 2. If true then set winning_count = votes and winning_percent =
            # vote_percentage.
        winning_count = votes
        winning_percentage = vote_percentage
            # 3. Set the winning_candidate equal to the candidate's name.
        winning_candidate = candidate_name

    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
        # Save the winning candidate's name to the text file.
    
    print(winning_candidate_summary)
    text_file.write(winning_candidate_summary)



    