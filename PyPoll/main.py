import os 
import csv
khancount = 0
correycount = 0
otooleycount = 0
licount = 0

election_data_csv = os.path.join("Resources", "election_data.csv")

with open(election_data_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    # print(header)

    for row in csvreader:
        if row[2]=="Khan":
            khancount+=1
        elif row[2]=="Correy":
            correycount+=1
        elif row[2]=="Li":
            licount+=1
        elif row[2]=="O\'Tooley":
            otooleycount+=1


candidates = ["Khan", "Li", "Correy", "O\'Tooley"]
votes = [khancount, licount, correycount, otooleycount]
Total_count = khancount+correycount+licount+otooleycount

percent_count = []
for x in votes:
    percent_count.append('{:.3%}'.format(x/Total_count))


summary_list = {k:[v,y] for k,v,y in zip(candidates, votes, percent_count)}

new_list = dict(sorted(summary_list.items(), key=lambda item:item[1], reverse=True))
itemmaxval = max(new_list.items(), key=lambda item:item[1])

out_list=[]

def sorted_dict(x):
    for key, value in x.items():
        y = "{}: {} ({})".format(key, value[1], value[0])
        out_list.append(y)
    
sorted_dict(new_list)
print("Election Results")
print(f'Total Votes: {Total_count}')
print('\n'.join(out_list))
print(f'Winner: {itemmaxval[0]}')

output_path = os.path.join("Analysis", "output.txt")

with open(output_path, 'w') as textfile:

    textfile.write("Election Results\n--------------------------\nTotal Votes: "+str(Total_count)+"\n--------------------------\n")
    textfile.write('\n'.join(out_list))
    textfile.write("\n--------------------------\nWinner: "+str(itemmaxval[0])+"\n--------------------------")
    