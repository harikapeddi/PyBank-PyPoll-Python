import os 
import csv

budget_data_csv = os.path.join("Resources", "budget_data.csv")
months = []
difference = []
result = []
values = []

with open(budget_data_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    header = next(csvreader)
    # print(header)

    

    # print(values)

    for row in csvreader:
        months.append(row[0])
        values.append(int(row[1]))
     

    for i in range(len(values)-1):
        difference.append(int(values[i+1]) - int(values[i]))
 
# print(months)

# print(values)
# print(type(values[0]))
# print(len(values))

# print(difference)
# print(max(difference))
# print(min(difference))


# difference.append(0)
# print(sum(values))
# print(int(sum(values)/len(values)))
sum_table = {m:d for m,d in zip(difference,months[1:]) }
# print(sum_table)
Total_Months = print(f'Total Months: {len(months)}')
Total_Value = print(f'Total: ${sum(values)}')
Avg_Change = print(f'Average Change: ${round(sum(difference)/len(difference),2)}')
Grt_Increase = print(f'Greatest Increase in Profits: {sum_table[max(sum_table)]} (${max(sum_table)})')
Grt_Decrease = print(f'Greatest Decrease in Profits: {sum_table[min(sum_table)]} (${min(sum_table)})')

output_path = os.path.join("Analysis", "output.txt")

with open(output_path, 'w') as textfile:

   textfile.write("Financial Analysis\n------------------------------------------"
   "\nTotal Months: " +str(len(months))+ "\nTotal: $"+str(sum(values))+"\nAverage Change: $"+str(round(sum(difference)/len(difference),2))+"\nGreatest Increase in Profits: "+str(sum_table[max(sum_table)])+" ($"+str(max(sum_table))+")\nGreatest Decrease in Profits: "+str(sum_table[min(sum_table)])+" ($"+str(min(sum_table))+")" )
   


    












      


