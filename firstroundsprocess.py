import pandas as pd

rounds = ['WXYZ', 'R1', 'R2', 'R3', 'R4', 'R5', 'R6']

def main():

    #intakeBrackets(2016, 2025)
    intakeBrackets(1985, 1985)
    intakeBrackets(2024, 2025)

    return 1

def intakeBrackets(strt, end):
    brackets = pd.read_csv('firstrounds.csv')

    season = None
    for year in range(strt, end):
        season = brackets[brackets['Season'] == year]
        seasonToBracket(season)

def seasonToBracket(season):
    # 4/7/25 Pick up here
    pi_mup = {}

    play_in = season[(season['Slot'].str.startswith('W')) |
                     (season['Slot'].str.startswith('X')) |
                     (season['Slot'].str.startswith('Y')) |
                     (season['Slot'].str.startswith('Z')) ]
    
    for i, mup in play_in.iterrows():
        teams = (mup['StrTeamName'], mup['WkTeamName'])
        pi_mup[mup['Slot']] = {'StrTeam' : teams[0],
                                 'WkTeam' : teams[1],
                                 'Winner' : teams[whoWins(teams[0], teams[1])]
                                 }
        
    mup64 = {}

    round1 = season[season['Slot'].str.startswith('R1')]

    for i, mup in round1.iterrows():
        teams = [mup['StrTeamName'], None]
        if pd.isnull(mup['WkTeamName']):
            teams[1] = pi_mup[mup['WeakSeed']]['Winner']
        else:
            teams[1] = mup['WkTeamName']

        mup64[mup['Slot']] = {'StrTeam' : teams[0],
                                 'WkTeam' : teams[1],
                                 'Winner' : teams[whoWins(teams[0], teams[1])]
                                 }

    #print(round1)
    
    for k, v in mup64.items():
        print(k, v)
                     
    #print(matchups)
    #print(play_in)
    return 1

def whoWins(team1, team2):
    return 0

if __name__ == "__main__":
    main()