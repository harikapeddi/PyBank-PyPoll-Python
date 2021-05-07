import os 
import csv
import sortedcontainers
from sortedcontainers import SortedDict

candidates = []
voter_id = []
names = []
candidates_Li = []
Candidates_Correy = []
Candidates_Khan = []
Candidates_Tooley = []
candidates_votes= []
percentages = []
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
    
#     def max_votes(K, L, C, O):
#         if max(K, L, C, O)==K:
#             Winner = "Khan"
#         elif max(K, L, C, O)==L:
#             Winner = "Li"
#         elif max(K, L, C, O)==C:
#             Winner = "Correy"
#         else: 
#             Winner = "O\'Tooley"
#         return Winner

# print(f'{max_votes(K, L, C, O)}') 
# # print(len(candidates_Li))
# # print(len(Candidates_Correy))
# # print(len(Candidates_Khan))
# # print(len(Candidates_Tooley))
# # print(f'{len(candidates_Li)+len(Candidates_Correy)+len(Candidates_Khan)+len(Candidates_Tooley)}')
# # print(f'Total Votes: {len(candidates)}')
# # print(f'Khan: {"{:.3%}".format(len(Candidates_Khan)/len(candidates))} % ({len(Candidates_Khan)})')
# # print(f'Correy: {"{:.3%}".format(len(Candidates_Correy)/len(candidates))} % ({len(Candidates_Correy)})')
# # print(f'Li: {"{:.3%}".format(len(candidates_Li)/len(candidates))}% ({len(candidates_Li)})')
# # print(f'O\'Tooley: {"{:.3%}".format(len(Candidates_Tooley)/len(candidates))} % ({len(Candidates_Tooley)})')
# # print(f'Winner: {max_votes(K, L, C, O)}')
condensed_candidates = set(candidates)
# print(*condensed_candidates)
# print(condensed_candidates)
values = [ C, K, L, O ]

for x in values:
    percentages.append('{:.3%}'.format(x/len(candidates)))

# print(percentages)

# print(values)

candidates_votes = {k:[v,y] for k,v,y in zip(values,sorted(condensed_candidates),percentages)}
print(candidates_votes)

# print(f'{candidates_votes[max(candidates_votes[1])]}')
# print(f'Winner: {candidates_votes[max(candidates_votes)[0]]}')
print(candidates_votes[max(candidates_votes)][0])
for k,v in sorted(candidates_votes):
    print(k, v[0])