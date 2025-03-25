import pandas
import os

def main():

    #file = open('matchups.csv', 'r')

    #data = pandas.read_csv('matchups.csv')

    #print(data)

    #print(data[data['YEAR'] == 2024])

    #teamData = pandas.read_csv('mm-data/MTeams.csv')

    #print(teamIDtoName(teamData, 1439))
    teams = generateTeams(64)
    #printTeams(teams)
    mups = teamsToMatchups(teams)
    runBracket(mups)


def runBracket(mups64):
    mups32 = runRound(mups64, comp)
    printMatchups(mups64)
    print('NEXT ROUND')
    mups16 = runRound(mups32, comp)
    printMatchups(mups32)
    print('NEXT ROUND')
    printMatchups(mups16)

def runRound(mups, compareTeams):
    nxtRound = []
    for mup in mups:
        teams = mup['teams']
        winner = compareTeams(teams[0], teams[1])
        mup['winner'] = winner
        nxtRound.append(teams[winner])
    return teamsToMatchups(nxtRound)
    
    

def comp(team1, team2):
    return 1

def teamsToMatchups(teams):
    round_of = len(teams)
    matchups = []
    for i in range(0, round_of - 1, 2):
        mup = {
            #'matchup' : teams[i]['matchup'],
            'matchup' : i // 2,
            #'region' : i // 16,
            'teams' : (teams[i], teams[i+1]),
            'winner' : None
        }
        matchups.append(mup)
    return matchups

def teamIDtoName(teamData, id):
    #return teamData[teamData['TeamID'] == 1450]
    return teamData.loc[teamData['TeamID'] == id, 'TeamName'].iloc[0]

def generateTeams(qty):
    teams = []
    for i in range(0, qty):
        name = "Team #%d" % i 
        team = { 'name' : name,
                 'color' : randomHex(),
                 'seed' : i % 16,
                 'matchup' : i // 2 }
        teams.append(team)
    return teams

def printTeams(teams):
    for team in teams:
        print(team)

def printMatchups(mups):
    for mup in mups:
        print('Matchup #%d' % mup['matchup'])
        #print('Region: %d' % mup['region'])
        print(mup['teams'][0])
        print(mup['teams'][1])
        if mup['winner']: 
            print('Winner: %s' % mup['teams'][mup['winner']]['name'])
        #print('Winner: bonk')
        print('----------')

def randomHex():
    return '#%s' % os.urandom(3).hex()

if __name__ == "__main__":
    main()