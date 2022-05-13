# -*- coding: UTF-8 -*-
"""PyPoll Homework Challenge Solution."""

# Add our dependencies.
import csv
import os

# Add a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Add a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

county_options = []
county_votes = {}
# Candidate Options and candidate votes.
candidate_options = []
candidate_votes = {}

# 1: Create a county list and county votes dictionary.

with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    next(file_reader)
    for row in file_reader:
        total_votes += 1
        if row[1] not in county_options:
            county_options.append(row[1])
            county_votes[row[1]] = 0
        county_votes[row[1]] += 1
        if row[2] not in candidate_options:
            candidate_options.append(row[2])
            candidate_votes[row[2]] = 0
        candidate_votes[row[2]] += 1

election_results = (
    f"\nElection Results\n"
    f"-------------------------\n"
    f"Total Votes: {total_votes:,}\n"
    f"-------------------------\n\n"
    f"County Votes:\n")

largest_turnout_county = ""
largest_turnout_count = 0
largest_turnout_percentage = 0

for county_name in county_votes:
    turnout = county_votes[county_name]
    turnout_percentage = float(turnout) / float(total_votes) * 100
    county_results = (f"{county_name}: {turnout_percentage:.1f}% ({turnout:,})\n")
    election_results = election_results + county_results
    if (turnout > largest_turnout_count) and (turnout_percentage > largest_turnout_percentage):
        largest_turnout_count = turnout
        largest_turnout_percentage = turnout_percentage
        largest_turnout_county = county_name
    
election_results = election_results + (
    f"-------------------------\n"
    f"Largest Turnout County: {largest_turnout_county}\n"
    f"-------------------------\n\n"
    f"Candidate Votes:\n")

winning_candidate = ""
winning_count = 0
winning_percentage = 0

for candidate_name in candidate_votes:
    votes = candidate_votes[candidate_name]
    vote_percentage = float(votes) / float(total_votes) * 100
    candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
    election_results = election_results + candidate_results
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        winning_count = votes
        winning_percentage = vote_percentage
        winning_candidate = candidate_name

election_results = election_results + (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")

print(election_results, end="")

with open(file_to_save, "w") as txt_file:
    txt_file.write(election_results)
