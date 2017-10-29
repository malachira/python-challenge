
import os
import csv

""" PyBank
    --------------------
    In this challenge, you are tasked with creating a Python script for analyzing the financial records 
    of your company. You will be given two sets of revenue data (`budget_data_1.csv` and `budget_data_2.csv`).
    Each dataset is composed of two columns: `Date` and `Revenue`. (Thankfully, your company has rather lax 
    standards for accounting so the records are simple.)

"""

print("\nChoose File to Analyze:\n(1)budget_data_1.csv\n(2)budget_data_2.csv\n")
file_select = input("Enter selection : ")

#create filepath
if file_select == "1":
    filepath = os.path.join("raw_data","budget_data_1.csv")
elif file_select == "2":
    filepath = os.path.join("raw_data","budget_data_2.csv")
else:
    print("Not a valid selection")
    exit()

#init list
total_revenue = 0
total_months = 0
max_revenue_chng = {}
min_revenue_chng = {}
revenue_chng = {}

#open file for reading
with open(filepath, newline="") as budget_data_file:

    budget_data = csv.reader(budget_data_file, delimiter=",")

    #ignore header
    next(budget_data,None)

    #iterate through each entry
    for row in budget_data:

        month_revenue = int(row[1])

        #add revenue
        total_revenue += month_revenue

        #add months
        total_months += 1

        #ignore revenue change calculation for the 1st month entry
        if total_months == 1:
            prev_month = month_revenue
        else:
            #store revenue change as a dictionary with month as key
            revenue_chng[row[0]] = month_revenue - prev_month
            prev_month = month_revenue

    #find average change in revenue between months over the entire period
    avg_revenue_chng = sum(revenue_chng.values())/len(revenue_chng.keys())

    #find the greatest increase in revenue (date and amount) over the entire period
    max_key = max(revenue_chng, key=revenue_chng.get)
    max_revenue_chng[max_key] = revenue_chng[max_key]
    
     #find the greatest decrease in revenue (date and amount) over the entire period
    min_key = min(revenue_chng, key=revenue_chng.get)
    min_revenue_chng[min_key] = revenue_chng[min_key]

    #print results

    print(f"\nFinancial Analysis ({filepath})")
    print("----------------------------")

    print(f"Total Months: {total_months}")
    print(f"Total Revenue: ${total_revenue}")
    print(f"Average Revenue Change: ${avg_revenue_chng}")
    print(f"Greatest Increase in Revenue: {max_key} (${revenue_chng[max_key]})")
    print(f"Greatest Decrease in Revenue: {min_key} (${revenue_chng[min_key]})\n")




