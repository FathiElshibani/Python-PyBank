
# coding: utf-8

# In[1]:


import os
import csv

AllCSVfiles = ["budget_data_1", "budget_data_2"]
for csvFile in AllCSVfiles:
    BankDataCSV = os.path.join("..","Documents/Resources",  csvFile + ".csv")
    
    months = []
    revenue = []
    revenueChange = []
    
    with open(BankDataCSV, 'r', encoding="UTF-8") as csvfile:
        BankData = csv.reader(csvfile, delimiter=",")
        
        next(BankData, None)

        for row in BankData:
            months.append(row[0])
            revenue.append(int(row[1]))
            
            
        for i in range(0, (len(revenue)-1)):
            revenueChange.append(revenue[i + 1] - revenue[i])
            AVG_Change = sum(revenueChange)/(len(revenueChange))
            
        #Printing the outputs
        print("Financial Analysis" + "  (" + csvFile + ")")
        print("---------------------------------")
        print("Total Months: " + str(len(months)))
        print("Averge Revenue Change: " + str(AVG_Change) )
        print("Total Revenue: " + str(sum(revenue)))
        print("Greatest Increase in Revenue: " + 
              months[revenueChange.index(max(revenueChange)) +1] + 
              " ($" + str(max(revenueChange)) + ")" ) 
        print("Greatest Decrease in Revenue: " + 
              months[revenueChange.index(min(revenueChange)) +1] + 
              " ($" + str(min(revenueChange)) + ")" ) 
        print("       ")
        print("       ")

