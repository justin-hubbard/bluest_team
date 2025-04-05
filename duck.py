import duckdb as duck
import pandas as pd

def main():
    res = duck.read_csv('mm-data/MNCAATourneyCompactResults.csv')
    slots = duck.read_csv('mm-data/MNCAATourneySlots.csv')
    seeds = duck.read_csv('mm-data/MNCAATourneySeeds.csv')

    #res = duck.sql('CREATE UNIQUE INDEX index ON res;')

    #res.show()
    #return
    testYear = 'Season = 2024 AND'
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
    play_in = duck.sql("""
                    SELECT play_in.*, res.WTeamID as WinnerID
                    FROM res
                    INNER JOIN play_in ON 
                        ((play_in.StrTeamID = res.WTeamID OR
                         play_in.WkTeamID = res.WTeamID)
                         AND play_in.Season = res.Season)
                    WHERE DayNum = 134 OR DayNum = 135
                   """).df()
    

    round1 = duck.sql(f"""
                    SELECT *
                    FROM slots
                    WHERE {testYear}
                        Slot LIKE 'R1%'
                    """).df()
    round1 = duck.sql("""
                    SELECT round1.*, seeds.TeamID as StrTeamID
                    FROM seeds
                    INNER JOIN round1 ON
                        (seeds.Season = round1.Season AND
                            seeds.Seed = round1.StrongSeed
                            )
                      """).df()
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
                      """).df()
    round1 = duck.sql("""
                    SELECT round1.*, res.WTeamID as WinnerID
                    FROM res
                    INNER JOIN round1 ON 
                        ((round1.StrTeamID = res.WTeamID OR
                         round1.WkTeamID = res.WTeamID)
                         AND round1.Season = res.Season)
                    WHERE DayNum = 136 OR DayNum = 137
                   """).df()
    

    round2 = duck.sql(f"""
                    SELECT *
                    FROM slots
                    WHERE {testYear}
                        Slot LIKE 'R2%'
                    """).df()
    round2 = duck.sql("""
                    SELECT round2.*, round1.WinnerID as StrTeamID
                    FROM round1
                    INNER JOIN round2 ON
                        (round1.Season = round2.Season AND
                            round1.Slot = round2.StrongSeed
                            )
                      """).df()
    round2 = duck.sql("""
                    SELECT round2.*, round1.WinnerID as WkTeamID
                    FROM round1
                    INNER JOIN round2 ON
                        (round1.Season = round2.Season AND
                            round1.Slot = round2.WeakSeed
                            )
                      """).df()
    round2 = duck.sql("""
                    SELECT round2.*, res.WTeamID as WinnerID
                    FROM res
                    INNER JOIN round2 ON 
                        ((round2.StrTeamID = res.WTeamID OR
                         round2.WkTeamID = res.WTeamID)
                         AND round2.Season = res.Season)
                    WHERE DayNum = 138 OR DayNum = 139
                   """).df()
                   

    round3 = duck.sql(f"""
                    SELECT *
                    FROM slots
                    WHERE {testYear}
                        Slot LIKE 'R3%'
                    """).df()
    round3 = duck.sql("""
                    SELECT round3.*, round2.WinnerID as StrTeamID
                    FROM round2
                    INNER JOIN round3 ON
                        (round2.Season = round3.Season AND
                            round2.Slot = round3.StrongSeed
                            )
                      """).df()
    round3 = duck.sql("""
                    SELECT round3.*, round2.WinnerID as WkTeamID
                    FROM round2
                    INNER JOIN round3 ON
                        (round2.Season = round3.Season AND
                            round2.Slot = round3.WeakSeed
                            )
                      """).df()
    round3 = duck.sql("""
                    SELECT round3.*, res.WTeamID as WinnerID
                    FROM res
                    INNER JOIN round3 ON 
                        ((round3.StrTeamID = res.WTeamID OR
                         round3.WkTeamID = res.WTeamID)
                         AND round3.Season = res.Season)
                    WHERE DayNum = 143 OR DayNum = 144
                   """).df()
    

    round4 = duck.sql(f"""
                    SELECT *
                    FROM slots
                    WHERE {testYear}
                        Slot LIKE 'R4%'
                    """).df()
    round4 = duck.sql("""
                    SELECT round4.*, round3.WinnerID as StrTeamID
                    FROM round3
                    INNER JOIN round4 ON
                        (round3.Season = round4.Season AND
                            round3.Slot = round4.StrongSeed
                            )
                      """).df()
    round4 = duck.sql("""
                    SELECT round4.*, round3.WinnerID as WkTeamID
                    FROM round3
                    INNER JOIN round4 ON
                        (round3.Season = round4.Season AND
                            round3.Slot = round4.WeakSeed
                            )
                      """).df()
    round4 = duck.sql("""
                    SELECT round4.*, res.WTeamID as WinnerID
                    FROM res
                    INNER JOIN round4 ON 
                        ((round4.StrTeamID = res.WTeamID OR
                         round4.WkTeamID = res.WTeamID)
                         AND round4.Season = res.Season)
                    WHERE DayNum = 145 OR DayNum = 146
                   """).df()
    

    round5 = duck.sql(f"""
                    SELECT *
                    FROM slots
                    WHERE {testYear}
                        Slot LIKE 'R5%'
                    """).df()
    round5 = duck.sql("""
                    SELECT round5.*, round4.WinnerID as StrTeamID
                    FROM round4
                    INNER JOIN round5 ON
                        (round4.Season = round5.Season AND
                            round4.Slot = round5.StrongSeed
                            )
                      """).df()
    round5 = duck.sql("""
                    SELECT round5.*, round4.WinnerID as WkTeamID
                    FROM round4
                    INNER JOIN round5 ON
                        (round4.Season = round5.Season AND
                            round4.Slot = round5.WeakSeed
                            )
                      """).df()
    round5 = duck.sql("""
                    SELECT round5.*, res.WTeamID as WinnerID
                    FROM res
                    INNER JOIN round5 ON 
                        ((round5.StrTeamID = res.WTeamID OR
                         round5.WkTeamID = res.WTeamID)
                         AND round5.Season = res.Season)
                    WHERE DayNum = 152
                   """).df()
    

    round6 = duck.sql(f"""
                    SELECT *
                    FROM slots
                    WHERE {testYear}
                        Slot LIKE 'R6%'
                    """).df()
    round6 = duck.sql("""
                    SELECT round6.*, round5.WinnerID as StrTeamID
                    FROM round5
                    INNER JOIN round6 ON
                        (round5.Season = round6.Season AND
                            round5.Slot = round6.StrongSeed
                            )
                      """).df()
    round6 = duck.sql("""
                    SELECT round6.*, round5.WinnerID as WkTeamID
                    FROM round5
                    INNER JOIN round6 ON
                        (round5.Season = round6.Season AND
                            round5.Slot = round6.WeakSeed
                            )
                      """).df()
    round6 = duck.sql("""
                    SELECT round6.*, res.WTeamID as WinnerID
                    FROM res
                    INNER JOIN round6 ON 
                        ((round6.StrTeamID = res.WTeamID OR
                         round6.WkTeamID = res.WTeamID)
                         AND round6.Season = res.Season)
                    WHERE DayNum = 154
                   """).df()
    
    complete = duck.sql("""
                            SELECT * FROM play_in
                            UNION ALL
                            SELECT * FROM round1
                            UNION ALL
                            SELECT * FROM round2
                            UNION ALL
                            SELECT * FROM round3
                            UNION ALL
                            SELECT * FROM round4
                            UNION ALL
                            SELECT * FROM round5
                            UNION ALL
                            SELECT * FROM round6
                            ORDER BY Season, Slot
                        """)

    #print(round1)
    #play_in.show()
    #round1.show(max_rows=100)
    #round2.show(max_rows=100)
    #round3.show(max_rows=100)
    #round4.show(max_rows=100)
    #round5.show(max_rows=100)
    #round6.show(max_rows=100)
    complete.show(max_rows=100)
    #complete.write_csv('testdata.csv')

if __name__ == "__main__":
    main()