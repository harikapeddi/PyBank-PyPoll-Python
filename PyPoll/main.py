import os 
import csv

candidates = []
voter_id = []
names = []
candidates_Li = []
Candidates_Correy = []
Candidates_Khan = []
Candidates_Tooley = []

election_data_csv = os.path.join("Resources", "election_data.csv")

with open(election_data_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    header = next(csvreader)

    # for row in csvreader:
    #     candidates.append(row[2])
    
    for row in csvreader:
        if row[2] == "Li" :
            candidates_Li.append(row[0])
        elif row[2] == "Correy":
            Candidates_Correy.append(row[0])
        elif row[2] == "Khan":
            Candidates_Khan.append(row[0])
        elif row[2] == "O'Tooley":
            Candidates_Tooley.append(row[0])
    

# # print(len(candidates_Li))
# # print(len(Candidates_Correy))
# # print(len(Candidates_Khan))
# # print(len(Candidates_Tooley))
print(len(candidates_Li)+(len(Candidates_Correy)+len(Candidates_Khan)+len(Candidates_Tooley)) 
# #("bmbnmbnm"