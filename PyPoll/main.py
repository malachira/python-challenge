import os
import csv
import sys

"""
------- PyPoll--------
In this challenge, you are tasked with helping a small, rural town modernize its vote-counting 
process. (Up until now, Uncle Cleetus had been trustfully tallying them one-by-one, but unfortunately,
his concentration isn't what it used to be.)You will be given two sets of poll data 
(`election_data_1.csv` and `election_data_2.csv`). Each dataset is composed of three
columns: `Voter ID`, `County`, and `Candidate`. Your task is to create a Python script that
analyzes the votes and calculates each of the following:
"""

#create filepath
filepath = os.path.join("raw_data","election_data_2.csv")

#init list
total_votes = 0
candidates = {}

#open file for reading
with open(filepath, newline="") as election_results:

    election_data = csv.reader(election_results, delimiter=",")

    #ignore header
    next(election_data,None)

    #iterate through each entry
    for row in election_data:

        #count voters
        total_votes += 1

        #add candidates  & the votes they got to a dictionary
        if row[2] in candidates.keys():
            candidates[row[2]][0] += 1   #add votes
        else:
            candidates[row[2]] = [1,0]  #create an entry for candidate with a list for storing total vo
                                        # percentage of votes

    #calculate percentage of votes per candidate & save it in the second list entry
    for key in candidates.keys():
        candidates[key][1] = (candidates[key][0]/total_votes) * 100
    
    #print results

    print(f"\nElection Results ({filepath})")
    print("----------------------------")
    print(f"Total Votes: {total_votes}")
    print("----------------------------")
     #calculate percentage of votes per candidate & save it in the second list entry
    for key in candidates.keys():
        candidates[key][1] = round((candidates[key][0]/total_votes) * 100,2)
        print(f"{key}: {candidates[key][1]}% ({candidates[key][0]})")
    print("----------------------------")
    print(f"Winner: {max(candidates, key=candidates.get)}")
    print("----------------------------")

    #print the same results to a text file
    sys.stdout = open("PyPoll_output.txt", "w")

    print(f"\nElection Results ({filepath})")
    print("----------------------------")
    print(f"Total Votes: {total_votes}")
    print("----------------------------")
     #calculate percentage of votes per candidate & save it in the second list entry
    for key in candidates.keys():
        print(f"{key}: {candidates[key][1]}% ({candidates[key][0]})")
    print("----------------------------")
    print(f"Winner: {max(candidates, key=candidates.get)}")
    print("----------------------------")



