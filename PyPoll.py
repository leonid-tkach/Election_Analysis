import csv
import os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Open the election results and read the file
with open(file_to_load) as election_data:
  # To do: perform analysis.
  print(election_data)


# The data we need to retrieve.
# 1. The total number of votes cast 
# 2. A complete list of candidates who received votes.
# 3. That percentage of votes each candidate won.
# 4. The total number of votes each candidate won.
# 5. No winner of the election based on popular vote.

# Import the datetime class from the datetime module.
# import datetime as dt

