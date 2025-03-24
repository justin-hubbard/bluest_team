import pandas

def main():

    file = open('matchups.csv', 'r')

    data = pandas.read_csv('matchups.csv')

    #print(data)

    #print(data[data['YEAR'] == 2024])

    teamData = pandas.read_csv('mm-data/MTeams.csv')

    print(teamIDtoName(teamData, 1439))




def teamIDtoName(teamData, id):
    #return teamData[teamData['TeamID'] == 1450]
    return teamData.loc[teamData['TeamID'] == id, 'TeamName'].iloc[0]


if __name__ == "__main__":
    main()