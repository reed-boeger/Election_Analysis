# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("Analysis", "election_analysis.txt")

#initialize total_votes to 0
total_votes = 0
#initialize a candidate list
candidate_options=[]
#empty dictionary to hold candidate votes
candidate_votes={}
# Open the election results and read the file.
# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#read the data
with open(file_to_load) as election_data:

    # To do: read and analyze the data here.
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    #read file headers
    headers = next(file_reader)
    #print(headers)
    #iterate across all rows
    for row in file_reader:
        #sum total votes of all rows
        total_votes += 1 
        #assign candiate_name to name in 3rd column of current row
        candidate_name=row[2]
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1

 #calculating vote percentages       
for candidate_name in candidate_votes:
    votes = candidate_votes[candidate_name]
    vote_percentage = float((votes / total_votes) * 100)
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        winning_count = votes
        winning_percentage = vote_percentage
        winning_candidate = candidate_name
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
#summary of winner
winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
    
print(winning_candidate_summary)
    
