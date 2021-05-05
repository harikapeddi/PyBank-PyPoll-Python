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

    for row in csvreader:
        candidates.append(row[2])
        if row[2] == "Li" :
            candidates_Li.append(row[0])
        elif row[2] == "Correy":
            Candidates_Correy.append(row[0])
        elif row[2] == "Khan":
            Candidates_Khan.append(row[0])
        elif row[2] == "O'Tooley":
            Candidates_Tooley.append(row[0])
    
    def maximum_votes(x):
        Khan = len(Candidates_Khan)
        Li = len(candidates_Li)
        Correy = len(Candidates_Correy)
        OTooley = len(Candidates_Tooley)
        if max(Khan, Li, Correy, OTooley) is Khan:
            x == "Khan"
        elif max(Khan, Li, Correy, OTooley) is Li:
            x == "Li"
        elif max(Khan, Li, Correy, OTooley) is Correy:
            x == "Correy"
        elif max(Khan, Li, Correy, OTooley) is OTooley:
            x == "O\'Tooley"     

# print(len(candidates_Li))
# print(len(Candidates_Correy))
# print(len(Candidates_Khan))
# print(len(Candidates_Tooley))
# print(f'{len(candidates_Li)+len(Candidates_Correy)+len(Candidates_Khan)+len(Candidates_Tooley)}')
# print(len(candidates))
# print(f'Khan: {len(Candidates_Khan)/len(candidates)*100} ({len(Candidates_Khan)})')
# print(f'Correy: {len(Candidates_Correy)/len(candidates)} ({len(Candidates_Correy)})')
# print(f'Li: {len(candidates_Li)/len(candidates)} ({len(candidates_Li)})')
# print(f'O\'Tooley: {len(Candidates_Tooley)/len(candidates)} ({len(Candidates_Tooley)})')
print(f'Winner: {maximum_votes(x)}')