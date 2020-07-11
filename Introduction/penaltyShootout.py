"""
Ideas to add:
    - player base
        - players with different abilities
        -
"""
# Welcome to Jux's penalty shootout (Premier League 2019/20)
import random as r
import time

penaltiesTakenHome = []
penaltiesTakenAway = []
suddenDeathHome = []
suddenDeathAway = []
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
    if homeTeam == "CHARLIE":
        print("Hi there, in Jux's penalty shootout simulator we refrain from using profanity,\n"
              "please ensure the name you entered is not an offensive one\n"
              "I have displayed a list of all the offensive names we will not accept\n"
              "1. Charlie")
    elif homeTeam.isalpha():
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

flag3 = False
while not flag3:
    penaltyCount = input("How many penalties\n")
    if penaltyCount.isnumeric():
        penaltyCount = int(penaltyCount)
        flag3 = True
    else:
        print("please enter a number in integer form ie: 6 instead of six")

while not gameStart and len(penaltiesTakenHome) < penaltyCount: #or homeScore == awayScore
    if len(penaltiesTakenHome) <= 0:
        isitagoal = r.randint(0, 1)
        print(f"{homeTeam} take your first shot!")
        print(f"it's a {goalOrMiss[isitagoal]}")
        penaltiesTakenHome.append(isitagoal)
        if isitagoal == 1:
            homeScore += 1
        print(penaltiesTakenHome)
        time.sleep(2)
    else:
        isitagoal = r.randint(0, 1)
        print(f"{homeTeam} take your next shot!")
        print(f"it's a {goalOrMiss[isitagoal]}")
        penaltiesTakenHome.append(isitagoal)
        if isitagoal == 1:
            homeScore += 1
        print(penaltiesTakenHome)
        time.sleep(2)
time.sleep(1)
print(f"Well done {homeTeam} you scored {homeScore}")
time.sleep(2)

while not gameStart and len(penaltiesTakenAway) < penaltyCount: #or homeScore == awayScore
    if len(penaltiesTakenAway) <= 0:
        isitagoal = r.randint(0, 1)
        print(f"{awayTeam} take your first shot!")
        print(f"it's a {goalOrMiss[isitagoal]}")
        penaltiesTakenAway.append(isitagoal)
        if isitagoal == 1:
            awayScore += 1
        print(penaltiesTakenAway)
        time.sleep(2)
    else:
        isitagoal = r.randint(0, 1)
        print(f"{awayTeam} take your next shot!")
        print(f"it's a {goalOrMiss[isitagoal]}")
        penaltiesTakenAway.append(isitagoal)
        if isitagoal == 1:
            awayScore += 1
        print(penaltiesTakenAway)
        time.sleep(2)

time.sleep(2)
print(f"Well done {awayTeam} you scored {awayScore}")
time.sleep(1)
print("---- FINAL RESULTS ----")
time.sleep(1)
print(f"{homeTeam} you scored {homeScore}")
time.sleep(1)
print(f"{awayTeam} you scored {awayScore}")
time.sleep(2)

if homeScore == awayScore:
    print("--------------------------")
    print("its time for sudden death!")
    flag4 = False
    suddenDeathCount = 0
    suddenDeathHomeScore = 0
    suddenDeathAwayScore = 0
    while not flag4:
        time.sleep(1)
        if suddenDeathCount < 6:
            isitagoal = r.randint(0,1)
            print(f"{homeTeam} take your shot!")
            print(f"it's a {goalOrMiss[isitagoal]} for {homeTeam}")
            suddenDeathHome.append(isitagoal)
            print(suddenDeathHome)
            if isitagoal == 1:
                suddenDeathHomeScore += 1
            print(f"{awayTeam} take your shot!")
            print(f"it's a {goalOrMiss[isitagoal]} for {awayTeam}")
            suddenDeathAway.append(isitagoal)
            print(suddenDeathAway)
            if isitagoal == 1:
                suddenDeathAwayScore += 1
            suddenDeathCount += 1
        else:
            print(f"Suddent death is over the scores are {homeTeam}:{suddenDeathHomeScore} - {awayTeam}:{suddenDeathAwayScore}")
            if suddenDeathHomeScore > suddenDeathAwayScore:
                print(f"{homeTeam} WINS!!!")
            elif suddenDeathAwayScore > suddenDeathHomeScore:
                print(f"{awayTeam} WINS!!!")
            else:
                print("If you are able to see this message idk how you got here, but if its another draw this is where i draw the line")
                time.sleep(7)
                print("---------------------------------------------------------------------------------------------------------------")
            flag4 = True
elif homeScore > awayScore:
    print(f"{homeTeam} wins!!!!")
else:
    print(f"{awayTeam} wins!!!!")