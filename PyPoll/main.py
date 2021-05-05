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
    
    
    K = len(Candidates_Khan)
    L = len(candidates_Li)
    C = len(Candidates_Correy)
    O = len(Candidates_Tooley)
    
    def max_votes(K, L, C, O):
        if max(K, L, C, O)==K:
            Winner = "Khan"
        elif max(K, L, C, O)==L:
            Winner = "Li"
        elif max(K, L, C, O)==C:
            Winner = "Correy"
        else: 
            Winner = "O\'Tooley"
        return Winner    

        

# print(len(candidates_Li))
# print(len(Candidates_Correy))
# print(len(Candidates_Khan))
# print(len(Candidates_Tooley))
# print(f'{len(candidates_Li)+len(Candidates_Correy)+len(Candidates_Khan)+len(Candidates_Tooley)}')
# print(len(candidates))
print(f'Khan: {round((len(Candidates_Khan)/len(candidates)*100), 4)} % ({len(Candidates_Khan)})')
# print(f'Correy: {round((len(Candidates_Correy)/len(candidates)*100), 3)} % ({len(Candidates_Correy)})')
# print(f'Li: {round((len(candidates_Li)/len(candidates)*100),3)}% ({len(candidates_Li)})')
# print(f'O\'Tooley: {round((len(Candidates_Tooley)/len(candidates)*100), 3)} % ({len(Candidates_Tooley)})')
# print(f'Winner: {max_votes(K, L, C, O)}')

print(f'{round((len(Candidates_Khan)/len(candidates)*100), 2)}')