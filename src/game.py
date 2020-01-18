# ############################################################# #
# Game class - contains all relevant information on a game      #
# Beef Erikson Studios 2020                                     #
# ############################################################# #

# TODO update game description/rating docstring from class once implemented

from bs4 import BeautifulSoup
import requests


class Game:
    """ Class definition for each game entry listed on retroachievements.
        Game description and rating scraped from xxxxxx
    """

    # Initialization
    def __init__(self, system_name: str = None, game_name: str = None,
                 genre: str = None, developer: str = None,
                 publisher: str = None, achievement_count: int = None,
                 description: str = None, game_rating: int = None,
                 game_url: str = None):
        self.system_name = system_name
        self.game_name = game_name
        self.genre = genre
        self.developer = developer
        self.publisher = publisher
        self.achievement_count = achievement_count
        self.description = description
        self.game_rating = game_rating
        self.game_url = game_url


def set_achievement_count(url: str, game_name: str) -> str:
    """
    Populates the game name from scraping supplied url
    :param url:
    :param game_name:
    :return:
    """
    game_name += " "
    soup = BeautifulSoup(requests.get(url).text, 'html.parser')
    tbody = soup.findAll('tbody')[1]
    num_games = len(tbody.find_all('tr')[1:]) - 1
    game_count = 0

    for row in tbody.find_all('tr')[1:]:
        game_count += 1
        if game_count <= num_games:
            column = row.find_all('td')
            name = column[1].div.string
            if str(name) == game_name:
                return column[2].string
    return "Not Found."


def get_total_game_count(url: str) -> int:
    """
    Supply url to scrape, returns total games with achievements.
    :param url: - The url to scape from
    :return: - Total number of games with achievements
    """
    soup = BeautifulSoup(requests.get(url).text, 'html.parser')
    tbody = soup.findAll('tbody')[1]
    total_games = len(tbody.find_all('tr')[1:]) - 1
    return total_games


def get_game_name(url: str, game_list: list) -> list:
    """
    Supply url to scrape and list to append game names.
    :param url: - The url to scrape from
    :param game_list: - The list to add game name to
    :return: - list
    """
    soup = BeautifulSoup(requests.get(url).text, 'html.parser')
    tbody = soup.findAll('tbody')[1]
    total_games = get_total_game_count(url)
    game_count = 0
    game_name = ""

    for row in tbody.find_all('tr')[1:]:
        game_count += 1
        if game_count <= total_games:
            column = row.find_all('td')
            game_name = column[1].div.string
            game_list.append(Game(game_name=game_name))
    return game_list
