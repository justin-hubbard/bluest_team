
import wikipedia as wiki
from bs4 import BeautifulSoup

def main():
    print('its ya boi')

    file = open('teams2.txt','r')

    regions = file.read().split('?')
    print(len(regions))

    matchups = [region.split(';') for region in regions]
    #for region in regions: 
     #   matchups.append(region.split(';'))

    sixtyfour = [team.split(',') for teams in matchups for team in teams]

    print(sixtyfour)

    team = 'Washington State University'
    team = 'University of North Carolina at Chapel Hill'
    team = 'Memphis University'

    res = wiki.search(team)
    print(res)
    page = wiki.page(res[0])
    html = page.html()

    soup = BeautifulSoup(html, 'html.parser')

    #print(soup.prettify())
    infobox = soup.find('table', {'class': 'infobox vcard'})

    color_spans = []#soup.find_all('span', {'class': 'legend-color'})
    #print(color_spans)

    for sp in color_spans:
        #hex = str(sp).split("#", 1)[1]
        start = str(sp).index('#')
        hex = str(sp)[start:]
        hex = hex.split(';', 1)[0]
        print(hex)





if __name__ == "__main__":
    main()