# ################################################################### #
#   Souped up from http://retroachievements.org/gameList.php?c=2      #
#   Beef Erikson Studios - 2020                                       #
#   Nintendo 64 games list scrape for use in random game for RA       #
# ################################################################### #

# TODO write to file
import src.game as game

# Starting variables
n64_url = "http://retroachievements.org/gameList.php?c=2"
genesis_url = "http://retroachievements.org/gameList.php?c=1"
file = open('n64.txt', 'w')


# TODO parse what's remaining and update docstring/comments
def main() -> None:
    """
    Testing setup, grabs achievement count from supplied title and url
    """
    # Creates list of Nintendo 64 games that have achievements
    n64_games = []
    game.get_game_details(n64_url, n64_games)

    # Creates list of Sega Genesis games that have achievements
    genesis_games = []
    game.get_game_details(genesis_url, genesis_games)

    # Debug print
    # N64
    for game_list in n64_games:
        print(game_list.game_name + ' - Achievements: ' +
              game_list.achievement_count)
    print('')
    print("Total number of games: " + str(game.get_total_game_count(n64_url)))
    print("Total number of achievements: " +
          str(game.get_total_achievement_count(n64_url)))

    # Genesis
    for game_list in genesis_games:
        print(game_list.game_name + ' - Achievements: ' +
              game_list.achievement_count)
    print('')
    print("Total number of games: " +
          str(game.get_total_game_count(genesis_url)))
    print("Total number of achievements: " +
          str(game.get_total_achievement_count(genesis_url)))


file.close()

if __name__ == "__main__":
    main()
