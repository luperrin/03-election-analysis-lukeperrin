import csv
import os

file_to_load = 'Resources/election_results.csv'
file_to_save = 'Resources/election_analysis.csv'

counties = ["Arapahoe","Denver","Jefferson"]
counties_dict = {}
counties_dict["Arapahoe"] = 422829
counties_dict["Jefferson"] = 432438
counties_dict["Denver"] = 463353

voting_data = []
voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
voting_data.append({"county":"Denver", "registered_voters": 463353})
voting_data.append({"county":"Jefferson", "registered_voters": 432438})



# candidate_votes = int(input("How many votes did the candidate get in the election? "))
# total_votes = int(input("What is the total number of votes in the election? "))
# message_to_candidate = (
#     f"You received {candidate_votes} number of votes. "
#     f"The total number of votes in the election was {total_votes}. "
#     f"You received {candidate_votes / total_votes * 100}% of the total votes.")
#
# print(message_to_candidate)

if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.")