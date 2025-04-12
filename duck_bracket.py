import duckdb as duck
import pandas as pd

#from colors import rgbDiff
import colors

foo = duck.read_csv('mm-data/MNCAATourneyCompactResults.csv')
slots = duck.read_csv('mm-data/MNCAATourneySlots.csv')
seeds = duck.read_csv('mm-data/MNCAATourneySeeds.csv')
names = pd.read_csv('mm-data/MTeams.csv')
teamColors = pd.read_csv('teamcolors_ncaa.csv')

def main():
    make_bracket(closest_to_color)

def make_bracket(whoWins):
    #res = duck.sql('CREATE UNIQUE INDEX index ON res;')

    #res.show()
    #return
    testYear = 'Season = 2025 AND'
    #testYear = ''

    pd.set_option('display.max_rows', None)

    all_brackets = pd.DataFrame(columns=['Season','Slot',
                                         'StrongSeed','WeakSeed',
                                         'StrTeamID','WkTeamID',
                                         'WinnerID'])

    play_in = duck.sql(f"""
                    SELECT * 
                    FROM slots 
                    WHERE {testYear}
                          (Slot LIKE 'W%' OR
                           Slot LIKE 'X%' OR
                           Slot LIKE 'Y%' OR
                           Slot LIKE 'Z%'
                          )
                   """).df()
    play_in = duck.sql("""
                    SELECT play_in.*, seeds.TeamID as StrTeamID
                    FROM seeds
                    INNER JOIN play_in ON (play_in.StrongSeed = seeds.Seed AND play_in.Season = seeds.Season)
                   """).df()
    play_in = duck.sql("""
                    SELECT play_in.*, seeds.TeamID as WkTeamID
                    FROM seeds
                    INNER JOIN play_in ON (play_in.WeakSeed = seeds.Seed AND play_in.Season = seeds.Season)
                   """).df()
    
    play_in['WinnerID'] = play_in.apply(lambda row: 
                                        whoWins(row['StrTeamID'],
                                        row['WkTeamID']), axis=1)
    
    all_brackets = pd.concat([all_brackets, play_in])
    
    for i in range(1, 7):
        source = 'all_brackets' if i > 1 else 'seeds'
        s_col = 'Slot' if i > 1 else 'Seed'
        team = 'WinnerID' if i > 1 else 'TeamID'

        round = duck.sql(f"""
                        SELECT *
                        FROM slots
                        WHERE {testYear}
                            Slot LIKE 'R{i}%'
                        """).df()
        round = duck.sql(f"""
                        SELECT round.*, {source}.{team} as StrTeamID
                        FROM {source}
                        INNER JOIN round ON
                            ({source}.Season = round.Season AND
                                {source}.{s_col} = round.StrongSeed
                                )
                        """).df()
        round = duck.sql(f"""
                        SELECT round.*, {source}.{team} as WkTeamID
                        FROM {source}
                        INNER JOIN round ON
                            ({source}.Season = round.Season AND
                                {source}.{s_col} = round.WeakSeed
                                ) %s"""
                        %
                        """
                        UNION
                        SELECT round.*, play_in.WinnerID as WkTeamID
                        FROM play_in
                        INNER JOIN round ON
                            (play_in.Season = round.Season AND
                                play_in.Slot = round.WeakSeed
                                )
                        """ if not play_in.empty else '').df()
        round = duck.sql('SELECT * FROM round ORDER BY Slot').df()
        
        round['WinnerID'] = round.apply(lambda row: 
                                            whoWins(row['StrTeamID'],
                                        row['WkTeamID']), axis=1)
        all_brackets = pd.concat([all_brackets, round])

    all_brackets = duck.sql("""
                    SELECT all_brackets.*, names.TeamName as StrTeamName
                    FROM names
                    INNER JOIN all_brackets 
                            ON all_brackets.StrTeamID = names.TeamID
                   """)
    all_brackets = duck.sql("""
                    SELECT all_brackets.*, names.TeamName as WkTeamName
                    FROM names
                    RIGHT JOIN all_brackets ON all_brackets.WkTeamID = names.TeamID
                   """).df()

    all_brackets = duck.sql('SELECT * FROM all_brackets ORDER BY Season, Slot')
    
    
    #all_brackets.show(max_rows=100)
    #complete.write_csv('testdata.csv')

def getTeamColors(teamName):
    print(teamName)
    row = teamColors[teamColors['name'] == teamName].iloc[0]
    #name, league, primary, secondary, tertiary, quaternary, division = row
    #print(row.primary, row.secondary, row.tertiary, row.quaternary)
    print(row.tolist())
    return 0

def nine_over_eight(team1, team2, year, seeds):
    seed1 = seeds.loc[(seeds['Season'] == year) & (seeds['TeamID'] == team1),'Seed'].iloc[0]
    seed2 = seeds.loc[(seeds['Season'] == year) & (seeds['TeamID'] == team2),'Seed'].iloc[0]
    
    s1 = int(seed1[1:3])
    s2 = int(seed2[1:3])

    if (s1 == 8) & (s2 == 9):
        #print(team1, team2)
        return team2
    else:
        return team1
    
def closest_to_color(team1, team2):
    teamName1 = names.loc[names['TeamID'] == team1, 'TeamName'].iloc[0]
    teamName1 = names.loc[names['TeamID'] == team1, 'TeamName'].iloc[0]
    
    color1 = getTeamColors(teamName1)
    return team1


if __name__ == "__main__":
    main()