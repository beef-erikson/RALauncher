# ################################################################### #
#   Souped up from http://retroachievements.org/gameList.php?c=2      #
#   Beef Erikson Studios - 2020                                       #
#   Nintendo 64 games list scrape for use in random game for RA       #
# ################################################################### #

# TODO write to file
import src.game as game

# Starting variables
n64_url = "http://retroachievements.org/gameList.php?c=2"
file = open('n64.txt', 'w')


# TODO parse what's remaining and update docstring/comments
def main():
    """
    Testing setup, grabs achievement count from supplied title and url
    :return:
    """
    # Creates list of Nintendo 64 games that have achievements
    n64_games = []
    game.get_game_details(n64_url, n64_games)

    # Debug print
    for game_list in n64_games:
        print(game_list.game_name + ' - Achievements: ' +
              game_list.achievement_count)
    print('')
    print("Total number of games: " + str(game.get_total_game_count(n64_url)))
    print("Total number of achievements: " +
          str(game.get_total_achievement_count(n64_url)))


file.close()

if __name__ == "__main__":
    main()
