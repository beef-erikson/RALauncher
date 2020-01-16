# ################################################################### #
#   Souped up from http://retroachievements.org/gameList.php?c=2      #
#   Beef Erikson Studios - 2020                                       #
#   Nintendo 64 games list scrape for use in random game for RA       #
# ################################################################### #

# TODO write to file
from game import Game
from game import set_achievement_count

# Starting variables
n64_url = "http://retroachievements.org/gameList.php?c=2"
file = open('n64.txt', 'w')


# TODO pretty much everything else parsing-wise. Update docstring as well
def main() -> None:
    """
    Testing setup, grabs achievement count from supplied title and url
    :return:
    """
    super_mario_64 = Game(game_name="Super Mario 64")
    super_mario_64.achievement_count = set_achievement_count(n64_url, "Super Mario 64")
    print()
    print(super_mario_64.game_name)
    print(super_mario_64.achievement_count)


file.close()

if __name__ == "__main__":
    main()


"""  LEAVING FOR REFERENCE FOR NOW - DELETE LATER
# Grabs info from supplied url
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
"""

