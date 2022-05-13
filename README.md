# Election_Analysis

## Overview of Election Audit

A Colorado Board of Elections employee has given me the following tasks to complete the election audit of a recent local congressional election:

1. Calculate the total number of votes cast 
2. Calculate that percentage of turnout by county and percentage of votes each candidate won.
3. Calculate the turnout by county and the number of votes each candidate won.
4. Determine the winner of the election based on popular vote.

## Resources

- Data source: election_results.csv
- Software: Python 3.10.4, VS Code 1.66.2

## Election-Audit Results

The election analysis shows that:

  - There were 369,711 votes cast in the election.
  - Turnout by county is:
    - Jefferson's turnout is 38,855 or 10.5% of the total turnout.
    - Denver's turnout is 306,055 or 82.8% of the total turnout.
    - Arapahoe's turnout is 24,801 or 6.7% of the total turnout.
  The county with the largest turnout is Denver

  - The candidate results are:
    - Charles Casper Stockham got 85,213 votes or 23.0% of the total votes cast.
    - Diana DeGette got 272,892 votes or 73.8% of the total votes cast.
    - Raymon Anthony Doane received 11,606 votes or 3.1% of the total votes cast.
  The winner of the election is Diana DeGette

## Election-Audit Summary:

It is possible to modify the script to use in state and federal elections, for which it's necessary:
1. to add to the dataset
  - a table mapping every county to a precinct
  - a table mapping every precinct to a state
  - join the tables on the precinct column
2. to left-join election_analysis.csv with the last table on the precinct column
3. to group-by the resulting table by state (for a state election) or sum it up (for a federal election).
