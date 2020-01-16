# ################################################################### #
#   Souped up from http://retroachievements.org/gameList.php?c=2      #
#   Beef Erikson Studios - 2020                                       #
#   Nintendo 64 games list scrape for use in random game for RA       #
# ################################################################### #

# TODO write to file

from bs4 import BeautifulSoup
import requests

# Starting variables
url = "http://retroachievements.org/gameList.php?c=2"
file = open('n64.txt', 'w')
soup = BeautifulSoup(requests.get(url).text, 'html.parser')
game_count = 0
achievement_count = 0
achievements = 0

# Grabs title names and achievement counts from list
tbody = soup.findAll('tbody')[1]
num_games = len(tbody.find_all('tr')[1:]) - 1

for row in tbody.find_all('tr')[1:]:
    game_count += 1
    if game_count <= num_games:
        column = row.find_all('td')
        name = column[1].div.string
        achievements = column[2].string
        achievement_count += int(achievements)
        print('{:<6s}{:<55s}{:>20s}{:>4}'.format(str(game_count) +
              ':', name, 'Achievements: ', achievements))
    else:
        print('\n' + str(game_count - 1) + ' games with ' +
              str(achievement_count) + ' achievements in total.')
        break

file.close()
