import csv
import os

# The data we need to retrieve
file_to_load = 'Resources/election_results.csv'

# Initialize a total vote counter.
total_votes = 0
# Candidate options and candidate votes
candidate_options = []
# 1. Declare the empty dictionary.
candidate_votes = {}
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read and print the header row.
    headers = next(file_reader)
    for row in file_reader:
        candidate_name = row[2]
        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

           # Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1


        # 2. Add to the total vote count.
        total_votes += 1




# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# Determine the percentage of votes for each candidate by looping through the counts.
# 1. Iterate through the candidate list.
for candidate_name in candidate_votes:
# 2. Retrieve vote count of a candidate.
    votes = candidate_votes[candidate_name]
# 3. Calculate the percentage of votes.
    vote_percentage = round((float(votes) / float(total_votes) * 100), 1)
# 4. Print the candidate name and percentage of votes.
    print(f"{candidate_name}: received {vote_percentage:.1f}% of the vote ({votes:,})\n")



# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote
# Determine if the votes is greater than the winning count.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        # If true then set winning_count = votes and winning_percent =
        # vote_percentage.
        winning_count = votes
        winning_percentage = vote_percentage
        # And, set the winning_candidate equal to the candidate's name.
        winning_candidate = candidate_name
winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)

file_to_save = 'Analysis/election_analysis.csv'
# with open(file_to_save, "w") as txt_file:
#
#     # Print the final vote count (to terminal)
#     election_results = (
#         f"\nElection Results\n"
#         f"-------------------------\n"
#         f"Total Votes: {total_votes:,}\n"
#         f"-------------------------\n\n"
#         f"County Votes:\n")
#     print(election_results, end="")
#     txt_file.write(election_results)
election_data.close()