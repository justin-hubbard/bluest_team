import duckdb as duck
import pandas as pd

def main():
    res = duck.read_csv('mm-data/MNCAATourneyCompactResults.csv')
    slots = duck.read_csv('mm-data/MNCAATourneySlots.csv')
    seeds = duck.read_csv('mm-data/MNCAATourneySeeds.csv')
    names = duck.read_csv('mm-data/MTeams.csv')

   
    testYear = 'Season = 2025 AND'
    testYear = ''

    play_in = duck.sql(f"""
                    SELECT * 
                    FROM slots 
                    WHERE {testYear}
                          (Slot LIKE 'W%' OR
                           Slot LIKE 'X%' OR
                           Slot LIKE 'Y%' OR
                           Slot LIKE 'Z%'
                          )
                   """)
    play_in = duck.sql("""
                    SELECT play_in.*, seeds.TeamID as StrTeamID
                    FROM seeds
                    INNER JOIN play_in ON (play_in.StrongSeed = seeds.Seed AND play_in.Season = seeds.Season)
                   """)
    play_in = duck.sql("""
                    SELECT play_in.*, seeds.TeamID as WkTeamID
                    FROM seeds
                    INNER JOIN play_in ON (play_in.WeakSeed = seeds.Seed AND play_in.Season = seeds.Season)
                    ORDER BY Slot
                   """)
    play_in = duck.sql("""
                    SELECT play_in.*, names.TeamName as StrTeamName
                    FROM names
                    INNER JOIN play_in ON play_in.StrTeamID = names.TeamID
                   """)
    play_in = duck.sql("""
                    SELECT play_in.*, names.TeamName as WkTeamName
                    FROM names
                    INNER JOIN play_in ON play_in.WkTeamID = names.TeamID
                   """)
    
    ############

    round1 = duck.sql(f"""
                    SELECT *
                    FROM slots
                    WHERE {testYear}
                        Slot LIKE 'R1%'
                    """)
    round1 = duck.sql("""
                    SELECT round1.*, seeds.TeamID as StrTeamID
                    FROM seeds
                    INNER JOIN round1 ON
                        (seeds.Season = round1.Season AND
                            seeds.Seed = round1.StrongSeed
                            )
                      """)
    round1 = duck.sql("""
                    SELECT round1.*, seeds.TeamID as WkTeamID
                    FROM seeds
                    RIGHT OUTER JOIN round1 ON
                        (seeds.Season = round1.Season AND
                            seeds.Seed = round1.WeakSeed
                            )
                    ORDER BY Slot
                    """)
    round1 = duck.sql("""
                    SELECT round1.*, names.TeamName as StrTeamName
                    FROM names
                    INNER JOIN round1 ON round1.StrTeamID = names.TeamID
                   """)
    round1 = duck.sql("""
                    SELECT round1.*, names.TeamName as WkTeamName
                    FROM names
                    RIGHT JOIN round1 ON round1.WkTeamID = names.TeamID
                   """).df()


    ############
    
    if play_in.fetchone():
        round1 = duck.sql("""
                            SELECT * FROM play_in
                            UNION
                            SELECT * FROM round1
                            ORDER BY Slot
                          """)
        
    round1 = duck.sql('SELECT * FROM round1 ORDER BY Season, Slot')
    

    #print(round1)
    #play_in.show() 
    #print(round1)
    round1.show(max_rows=100)
    #round2.show(max_rows=100)
    #round3.show(max_rows=100)
    #round4.show(max_rows=100)
    #round5.show(max_rows=100)
    #round6.show(max_rows=100)
    #complete.show(max_rows=100)
    #complete.write_csv('testdata.csv')
    round1.write_csv('firstrounds.csv')

if __name__ == "__main__":
    main()