"""
Ideas to add:
    - Sudden death
    - determining the winner
    - player base
        - players with different abilities
        -
"""

# Welcome to Jux's penalty shootout (Premier League 2019/20)
import random as r
import time

penaltiesTakenHome = []
penaltiesTakenAway = []
homeScore = 0
awayScore = 0
gameStart = False
teamList = [
    "Arsenal",
    "Aston Villa",
    "Bournemouth",
    "Brighton & Hove Albion",
    "Burnley",
    "Chelsea",
    "Crystal Palace",
    "Everton",
    "Leicester City",
    "Liverpool",
    "Manchester City",
    "Manchester United",
    "Newcastle United",
    "Norwich City",
    "Sheffield United",
    "Southampton",
    "Tottenham Hotspur",
    "Watford",
    "West Ham United",
    "Wolverhampton Wanderers"
]
goalOrMiss = {
    0 : "Miss",
    1 : "Goal"
}

flag1 = False
while not flag1:
    homeTeam = input("Please enter the name of the home team\n").upper()
    if homeTeam.isalpha():
        homeTeam = str(homeTeam)
        flag1 = True
    else:
        print("Please enter a valid team name")

flag2 = False
while not flag2:
    awayTeam = input("Please enter the name of the away team\n").upper()
    if awayTeam.isalpha():
        awayTeam = str(awayTeam)
        flag2 = True
    else:
        print("Please enter a valid team name")

while not gameStart and len(penaltiesTakenHome) < 5: #or homeScore == awayScore
    if len(penaltiesTakenHome) <= 0:
        isitagoal = r.randint(0, 1)
        print(f"{homeTeam} take your first shot!")
        print(f"it's a {goalOrMiss[isitagoal]}")
        penaltiesTakenHome.append(isitagoal)
        if isitagoal == 1:
            homeScore += 1
        print(penaltiesTakenHome)
        time.sleep(1)
    else:
        isitagoal = r.randint(0, 1)
        print(f"{homeTeam} take your next shot!")
        print(f"it's a {goalOrMiss[isitagoal]}")
        penaltiesTakenHome.append(isitagoal)
        if isitagoal == 1:
            homeScore += 1
        print(penaltiesTakenHome)
        time.sleep(1)
time.sleep(1)
print(f"Well done {homeTeam} you scored {homeScore}")
time.sleep(1)
while not gameStart and len(penaltiesTakenAway) < 5: #or homeScore == awayScore
    if len(penaltiesTakenAway) <= 0:
        isitagoal = r.randint(0, 1)
        print(f"{awayTeam} take your first shot!")
        print(f"it's a {goalOrMiss[isitagoal]}")
        penaltiesTakenAway.append(isitagoal)
        if isitagoal == 1:
            awayScore += 1
        print(penaltiesTakenAway)
        time.sleep(1)
    else:
        isitagoal = r.randint(0, 1)
        print(f"{awayTeam} take your next shot!")
        print(f"it's a {goalOrMiss[isitagoal]}")
        penaltiesTakenAway.append(isitagoal)
        if isitagoal == 1:
            awayScore += 1
        print(penaltiesTakenAway)
        time.sleep(1)
time.sleep(1)
print(f"Well done {awayTeam} you scored {awayScore}")
print("---- FINAL RESULTS ----")
print(f"{homeTeam} you scored {homeScore}")
print(f"{awayTeam} you scored {awayScore}")