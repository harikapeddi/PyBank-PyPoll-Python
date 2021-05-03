import os 
import csv
import datetime
import math

budget_data_csv = os.path.join("Resources", "budget_data.csv")


months = []

difference = []

result = []



with open(budget_data_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    header = next(csvreader)
    print(header)
    values = []
    difference = []
    # difference.append(0)

    print(values)

    for row in csvreader:
        months.append(row[0])
        values.append(int(row[1]))

    for i in range(len(values)-1):
        difference.append(int(values[i+1]) - int(values[i]))

    
    

# print(months)
# # print(len(months))
print(type(values[0]))
# # print(len(values))

print(difference)
print(max(difference))
print(min(difference))
print(sum(difference)/len(difference))
print(sum(values))
print(int(sum(values)/len(values)))
sum_table = {m:d for m,d in zip(months[1:], difference)}
print(sum_table)







      


