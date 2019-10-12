# -*- coding: UTF-8 -*-
"""PyPoll Homework Solution."""

# Incorporated the csv module
import csv
import os

# Files to load
file_to_load = os.path.realpath("D:/Git/GWU-ARL-DATA-PT-09-2019-U-C/02-Homework/03-Python/Instructions/Part-2/PyPoll/Resources/election_data.csv")
file_to_output = "output.txt"

# Total Vote Counter
total_votes = 0

# Candidate Options and Vote Counters
candidate_options = []
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0

# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Read the header
    header = next(reader)

    # For each row...
    for row in reader:

        # Add to the total vote count
        total_votes = total_votes + 1

        # Extract the candidate name from each row
        candidate_name = row[2]

        # If the candidate does not match any existing candidate...
        # (In a way, our loop is "discovering" candidates as it goes)
        if candidate_name not in candidate_options:

            # Add it to the list of candidates in the running
            # HINT: Use the append function
            candidate_options.append(row[2])

            # And begin tracking that candidate's voter count
            # HINT: Initialize candidate_votes[candidate_name] to 0
            candidate_votes[candidate_name] = 0


        # Then add a vote to that candidate's count
        # HINT: candidate_votes[candidate_name] += 1
        candidate_votes[candidate_name] += 1

# Print the results and export the data to our text file
with open(file_to_output, "w") as txt_file:

    # Print the final vote count (to terminal)
    print(
            f"Election Results\n"
            f"-------------------------\n"
            f"Total Votes: {total_votes}\n"
            f"-------------------------")
    # HINT: Print out the value of total_votes

    # Save the final vote count to the text file
    # HINT: use txt_file.write(election_results)
    election_results = (
            f"Election Results\n"
            f"-------------------------\n"
            f"Total Votes: {total_votes}\n"
            f"-------------------------\n")
    txt_file.write(election_results)

    # Determine the winner by looping through the counts
    for candidate in candidate_votes:

        # Retrieve vote count and percentage
        votes = candidate_votes.get(candidate)
        vote_percentage = float(votes) / float(total_votes) * 100

        # Determine winning vote count and candidate
        if (votes > winning_count):
            winning_count = votes
            winning_candidate = candidate

        # Print each candidate's voter count and percentage (to terminal)
        voter_output = (f"{candidate}: {vote_percentage:.3f}% ({votes})\n")
        print(voter_output, end="")

        # Save each candidate's voter count and percentage to text file
        txt_file.write(voter_output)

    # Print the winning candidate (to terminal)
    print(
            f"-------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"-------------------------")

    # Save the winning candidate's name to the text file
    winner = (
            f"-------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"-------------------------")
    txt_file.write(winner)