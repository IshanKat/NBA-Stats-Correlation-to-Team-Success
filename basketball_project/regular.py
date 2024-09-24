import scipy.stats as stats
import numpy as np

# Key to go from team name to abbreviation
legend = {
    "Atlanta Hawks": "ATL",
    "Boston Celtics": "BOS",
    "Charlotte Hornets": "CHA",
    "Chicago Bulls": "CHI",
    "Cleveland Cavaliers": "CLE",
    "Dallas Mavericks": "DAL",
    "Denver Nuggets": "DEN",
    "Detroit Pistons": "DET",
    "Golden State Warriors": "GSW",
    "Houston Rockets": "HOU",
    "Indiana Pacers": "IND",
    "Los Angeles Clippers": "LAC",
    "Los Angeles Lakers": "LAL",
    "Memphis Grizzlies": "MEM",
    "Miami Heat": "MIA",
    "Milwaukee Bucks": "MIL",
    "Minnesota Timberwolves": "MIN",
    "New Orleans Pelicans": "NOP",
    "New York Knicks": "NYK",
    "Brooklyn Nets": "BKN",
    "Oklahoma City Thunder": "OKC",
    "Orlando Magic": "ORL",
    "Philadelphia 76ers": "PHI",
    "Phoenix Suns": "PHO",
    "Portland Trail Blazers": "POR",
    "Sacramento Kings": "SAC",
    "San Antonio Spurs": "SAS",
    "Toronto Raptors": "TOR",
    "Utah Jazz": "UTH",
    "Washington Wizards": "WAS",
    "Seattle SuperSonics": "OKC",
    "Washington Bullets": "WAS",
    "Vancouver Grizzlies": "MEM",
    "LA Clippers": "LAC",
    "Charlotte Bobcats": "CHA",
    "New Orleans Hornets": "NOP",
    "New Jersey Nets": "BKN",
    "New Orleans/Oklahoma City Hornets": "NOP"
}

# Get final placements of each team
year = input("Enter season year: \n")
f = open(f"standings/{str(year)}.txt", "r")
lines = f.readlines()

ranking = []
count = 0
for line in lines:
    ranking.append(line.rstrip("\n"))
    count += 1


# print(ranking)

print("Enter ranking order: ")
order = {}
for i in range(len(ranking)):
    team = input()
    team = legend[team]
    order[team] = i+1

# print(order)

dataset = np.array([[0, 0], 
                    [0, 0],
                    [0, 0],
                    [0, 0],])

count = 1
for line in ranking:
    rank = order[line]
    row = -1
    col = -1
    if (rank <= 4):
        row = 0
    elif (rank <= 8):
        row = 1
    elif (rank <= 12):
        row = 2
    elif (rank <= 16):
        row = 3
    else:
        continue

    if (count <= 4):
        col = 0
    elif (count <= 16):
        col = 1
    else:
        continue

    dataset[row][col] += 1
    count += 1

# print(dataset)
  
# Calculate chi-square
X2 = stats.chi2_contingency(dataset, correction=False)[0]
N = np.sum(dataset)
minimum_dimension = min(dataset.shape)-1
  
# Calculate Cramer's V
V = np.sqrt((X2/N) / minimum_dimension)

# Print results
cout = open("cresult.txt", "a")
vout = open("vresult.txt", "a");

cout.write(str(X2) + "\n")
vout.write(str(V) + "\n")