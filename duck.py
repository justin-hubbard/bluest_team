import duckdb as duck
import pandas as pd

def main():
    res = duck.read_csv('mm-data/MNCAATourneyCompactResults.csv')
    slots = duck.read_csv('mm-data/MNCAATourneySlots.csv')
    seeds = duck.read_csv('mm-data/MNCAATourneySeeds.csv')

    testYear = 2024

    play_in = duck.sql(f"""
                    SELECT * 
                    FROM slots 
                    WHERE Season = {testYear} AND
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
                   """)
    play_in = duck.sql("""
                    SELECT play_in.*, res.WTeamID as WinnerID
                    FROM res
                    INNER JOIN play_in ON 
                        ((play_in.StrTeamID = res.WTeamID OR
                         play_in.WkTeamID = res.WTeamID)
                         AND play_in.Season = res.Season)
                    WHERE DayNum = 134 OR DayNum = 135
                   """)
    

    round1 = duck.sql(f"""
                    SELECT *
                    FROM slots
                    WHERE Season = {testYear} AND
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
                    INNER JOIN round1 ON
                        (seeds.Season = round1.Season AND
                            seeds.Seed = round1.WeakSeed
                            )
                    UNION
                    SELECT round1.*, play_in.WinnerID as WkTeamID
                    FROM play_in
                    INNER JOIN round1 ON
                        (play_in.Season = round1.Season AND
                            play_in.Slot = round1.WeakSeed
                            )
                      """)
    round1 = duck.sql("""
                    SELECT round1.*, res.WTeamID as WinnerID
                    FROM res
                    INNER JOIN round1 ON 
                        ((round1.StrTeamID = res.WTeamID OR
                         round1.WkTeamID = res.WTeamID)
                         AND round1.Season = res.Season)
                    WHERE DayNum = 136 OR DayNum = 137
                   """)
    

    round2 = duck.sql(f"""
                    SELECT *
                    FROM slots
                    WHERE Season = {testYear} AND
                        Slot LIKE 'R2%'
                    """)
    round2 = duck.sql("""
                    SELECT round2.*, round1.WinnerID as StrTeamID
                    FROM round1
                    INNER JOIN round2 ON
                        (round1.Season = round2.Season AND
                            round1.Slot = round2.StrongSeed
                            )
                      """)
    round2 = duck.sql("""
                    SELECT round2.*, round1.WinnerID as WkTeamID
                    FROM round1
                    INNER JOIN round2 ON
                        (round1.Season = round2.Season AND
                            round1.Slot = round2.WeakSeed
                            )
                      """)
    round2 = duck.sql("""
                    SELECT round2.*, res.WTeamID as WinnerID
                    FROM res
                    INNER JOIN round2 ON 
                        ((round2.StrTeamID = res.WTeamID OR
                         round2.WkTeamID = res.WTeamID)
                         AND round2.Season = res.Season)
                    WHERE DayNum = 138 OR DayNum = 139
                   """)
                   

    round3 = duck.sql(f"""
                    SELECT *
                    FROM slots
                    WHERE Season = {testYear} AND
                        Slot LIKE 'R3%'
                    """)
    round3 = duck.sql("""
                    SELECT round3.*, round2.WinnerID as StrTeamID
                    FROM round2
                    INNER JOIN round3 ON
                        (round2.Season = round3.Season AND
                            round2.Slot = round3.StrongSeed
                            )
                      """)
    round3 = duck.sql("""
                    SELECT round3.*, round2.WinnerID as WkTeamID
                    FROM round2
                    INNER JOIN round3 ON
                        (round2.Season = round3.Season AND
                            round2.Slot = round3.WeakSeed
                            )
                      """)
    round3 = duck.sql("""
                    SELECT round3.*, res.WTeamID as WinnerID
                    FROM res
                    INNER JOIN round3 ON 
                        ((round3.StrTeamID = res.WTeamID OR
                         round3.WkTeamID = res.WTeamID)
                         AND round3.Season = res.Season)
                    WHERE DayNum = 143 OR DayNum = 144
                   """)
    

    round4 = duck.sql(f"""
                    SELECT *
                    FROM slots
                    WHERE Season = {testYear} AND
                        Slot LIKE 'R4%'
                    """)
    round4 = duck.sql("""
                    SELECT round4.*, round3.WinnerID as StrTeamID
                    FROM round3
                    INNER JOIN round4 ON
                        (round3.Season = round4.Season AND
                            round3.Slot = round4.StrongSeed
                            )
                      """)
    round4 = duck.sql("""
                    SELECT round4.*, round3.WinnerID as WkTeamID
                    FROM round3
                    INNER JOIN round4 ON
                        (round3.Season = round4.Season AND
                            round3.Slot = round4.WeakSeed
                            )
                      """)
    round4 = duck.sql("""
                    SELECT round4.*, res.WTeamID as WinnerID
                    FROM res
                    INNER JOIN round4 ON 
                        ((round4.StrTeamID = res.WTeamID OR
                         round4.WkTeamID = res.WTeamID)
                         AND round4.Season = res.Season)
                    WHERE DayNum = 145 OR DayNum = 146
                   """)
    

    round5 = duck.sql(f"""
                    SELECT *
                    FROM slots
                    WHERE Season = {testYear} AND
                        Slot LIKE 'R5%'
                    """)
    round5 = duck.sql("""
                    SELECT round5.*, round4.WinnerID as StrTeamID
                    FROM round4
                    INNER JOIN round5 ON
                        (round4.Season = round5.Season AND
                            round4.Slot = round5.StrongSeed
                            )
                      """)
    round5 = duck.sql("""
                    SELECT round5.*, round4.WinnerID as WkTeamID
                    FROM round4
                    INNER JOIN round5 ON
                        (round4.Season = round5.Season AND
                            round4.Slot = round5.WeakSeed
                            )
                      """)
    round5 = duck.sql("""
                    SELECT round5.*, res.WTeamID as WinnerID
                    FROM res
                    INNER JOIN round5 ON 
                        ((round5.StrTeamID = res.WTeamID OR
                         round5.WkTeamID = res.WTeamID)
                         AND round5.Season = res.Season)
                    WHERE DayNum = 152
                   """)
    

    round6 = duck.sql(f"""
                    SELECT *
                    FROM slots
                    WHERE Season = {testYear} AND
                        Slot LIKE 'R6%'
                    """)
    round6 = duck.sql("""
                    SELECT round6.*, round5.WinnerID as StrTeamID
                    FROM round5
                    INNER JOIN round6 ON
                        (round5.Season = round6.Season AND
                            round5.Slot = round6.StrongSeed
                            )
                      """)
    round6 = duck.sql("""
                    SELECT round6.*, round5.WinnerID as WkTeamID
                    FROM round5
                    INNER JOIN round6 ON
                        (round5.Season = round6.Season AND
                            round5.Slot = round6.WeakSeed
                            )
                      """)
    round6 = duck.sql("""
                    SELECT round6.*, res.WTeamID as WinnerID
                    FROM res
                    INNER JOIN round6 ON 
                        ((round6.StrTeamID = res.WTeamID OR
                         round6.WkTeamID = res.WTeamID)
                         AND round6.Season = res.Season)
                    WHERE DayNum = 154
                   """)
    
    complete = duck.sql("""
                            SELECT * FROM play_in
                            UNION
                            SELECT * FROM round1
                            UNION
                            SELECT * FROM round2
                            UNION
                            SELECT * FROM round3
                            UNION
                            SELECT * FROM round4
                            UNION
                            SELECT * FROM round5
                            UNION
                            SELECT * FROM round6
                        """)

    #print(round1)
    #play_in.show()
    #round1.show(max_rows=100)
    #round2.show(max_rows=100)
    #round3.show(max_rows=100)
    #round4.show(max_rows=100)
    #round5.show(max_rows=100)
    #round6.show(max_rows=100)
    #complete.show(max_rows=100)
    complete.write_csv('testdata.csv')

if __name__ == "__main__":
    main()