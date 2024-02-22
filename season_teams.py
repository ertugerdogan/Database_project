from flask import Flask
import views
from dbconn import Database
from dbconn import ConnectionPool

def get_seasons():
    with ConnectionPool() as cursor:
        cursor.execute('SELECT season FROM season_teams_v2 ORDER BY season ASC')
        seasons = cursor.fetchall()
        return seasons
def get_teams_of_season(season):
    with ConnectionPool() as cursor:
        cursor.execute('SELECT * FROM season_teams_v2 WHERE season=\'{0}\''.format(season))
        teams = cursor.fetchall()
        return teams

class Season_Teams(object):
    def __init__(self, season, team_name, team_code, playoff):
        self.season = season
        self.team_name = team_name
        self.team_code =  team_code
        self.playoff =  playoff