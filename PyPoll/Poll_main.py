
# coding: utf-8

# In[1]:


import os
import csv

AllCSVfiles = ["election_data_1", "election_data_2"]
for csvFile in AllCSVfiles:
    PollDataCSV = os.path.join("..","Documents/Resources",  csvFile + ".csv")
    
    votes = []
    candidates = []
    UniqueCandidates = []
    
    with open(PollDataCSV, 'r', encoding="UTF-8") as csvfile:
        PollData = csv.reader(csvfile, delimiter=",")
        
        next(PollData, None)

        for row in PollData:
            votes.append(row[0])
            candidates.append(row[2])
            
        for candidate in candidates:
            if candidate not in UniqueCandidates:
                UniqueCandidates.append(candidate)
        
        candidateCount = dict()
        for candidate in candidates:
            if candidate not in candidateCount:
                candidateCount[candidate] = 1
            else:
                candidateCount[candidate] +=1
        
            
        #Printing the outputs
        print("Election Results"+ "  (" + csvFile + ")")
        print("----------------------------")
        print("Total Votes: " + str(len(votes)))
        print("----------------------------")
        for candidate in candidateCount:
            print(candidates[candidates.index(candidate)] +": " + 
                  str(round(int(candidateCount[candidate])*100/int(len(votes)),2)) +"% ("+
                  str(candidateCount[candidate]) + ")")
        print("----------------------------")
        print("Winner: " + max(candidateCount, key=candidateCount.get))
        print("----------------------------")
        print("   ")
        print("   ")

