import pandas as pd

def main():
    res = pd.read_csv('mm-data/MNCAATourneyCompactResults.csv')
    names = pd.read_csv('mm-data/MTeams.csv')

    slots = pd.read_csv('mm-data/MNCAATourneySlots.csv')
    seeds = pd.read_csv('mm-data/MNCAATourneySeeds.csv')

    year = res[res['Season'] == 2024]

    ySlots = slots[slots['Season'] == 2024]
    ySeeds = seeds[seeds['Season'] == 2024]

    zipSeedSlot(ySlots, ySeeds, year)

    #print()
    #scanned = scanYear(year, names)
    #print(scanned)

# returns a full bracket, broken up by round
def zipSeedSlot(ySlots, ySeeds, res):

    # Creat df for play-in games
    play_in = ySlots[(ySlots['Slot'].str.startswith('W')) |
                     (ySlots['Slot'].str.startswith('X')) |
                     (ySlots['Slot'].str.startswith('Y')) |
                     (ySlots['Slot'].str.startswith('Z'))
                     ]
    
    play_in = play_in.merge(ySeeds,
                            left_on='StrongSeed',
                            right_on='Seed',
                            how='left').drop(columns=['Seed', 'Season_y'])
    play_in = play_in.rename(columns={'TeamID' : 'StrTeamID'})

    play_in = play_in.merge(ySeeds,
                            left_on='WeakSeed',
                            right_on='Seed',
                            how='left').drop(columns=['Seed', 'Season'])
    play_in = play_in.rename(columns={'TeamID' : 'WkTeamID'})

    pi_res = res[(res['DayNum'] == 134) | (res['DayNum'] == 135)]

    # could do this the other way around, check compact line for
    # line containing strteamid in either WTeamID or LTeamID, then just pick
    # the team from the WTeamID. But then, how to pick, exactly?

    yup = pi_res.WTeamID.isin([1161])

    #test = pi_res(pi_res['WTeamID'] == )
    test = play_in.merge(pi_res, 
                         left_on=['StrTeamID','WkTeamID'],
                         right_on=['WTeamID','WTeamID'],
                         how='inner')

    #print(play_in)
    print(test)




    brack = ySlots[ySlots['Slot'].str.startswith('R1')]

    # add strong team ID
    brack = brack.merge(ySeeds, 
                 left_on='StrongSeed', 
                 right_on='Seed',
                 how='left').drop(columns=['Seed', 'Season_y'])
    brack = brack.rename(columns={'TeamID':'StrTeamID'})

    # add weak team ID
    brack = brack.merge(ySeeds, 
                 left_on='WeakSeed', 
                 right_on='Seed',
                 how='left').drop(columns=['Seed', 'Season'])
    brack = brack.rename(columns={'TeamID':'WkTeamID'})

    #print(brack)
    #print(r1.Season)



def scanYear(year, names):
    #day1 = year[year['DayNum'] == 136]
    #day2 = year[year['DayNum'] == 137]

    r1_days = [138, 139]
    round1 = year[year['DayNum'].isin(r1_days)]

    mups = []
    #for i, row in round1.iterrows():
    iter = round1.iterrows()
    #for (i, row1), (j, row2) in zip(iter, iter):
    # for row1, row2 in zip(iter, iter):    
    #     print(row1, row2)
    #     team1 = row1['']

    for row in round1.itertuples():
        teamW = row.WTeamID
        teamL = row.LTeamID
        mup = (teamIDtoName(names,teamW), 
               teamIDtoName(names,teamL))
        mups.append(mup)
        #print(mup)

    #print(round1)

    return mups

def teamIDtoName(teamData, id):
    return teamData.loc[teamData['TeamID'] == id, 'TeamName'].iloc[0]


if __name__ == "__main__":
    main()