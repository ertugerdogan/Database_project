from flask import Flask
import views
from dbconn import Database
from dbconn import ConnectionPool

def update_homepage_of_team_code(new_homapage, team_code):
    with ConnectionPool() as cursor:
        cursor.execute('UPDATE teams_profile SET homepage=%s WHERE team_code=%s', (new_homapage, team_code))

def update_country_of_team_code(new_country, team_code):
    with ConnectionPool() as cursor:
        cursor.execute('UPDATE teams_profile SET country=%s WHERE team_code=%s', (new_country, team_code))

def update_founded_of_team_code(new_founded, team_code):
    with ConnectionPool() as cursor:
        cursor.execute('UPDATE teams_profile SET founded=%s WHERE team_code=%s', (new_founded, team_code))

def update_stadium_of_team_code(new_stadium, team_code):
    with ConnectionPool() as cursor:
        cursor.execute('UPDATE teams_profile SET stadium=%s WHERE team_code=%s', (new_stadium, team_code))

def update_capacity_of_team_code(new_stadium_capacity, team_code):
    with ConnectionPool() as cursor:
        cursor.execute('UPDATE teams_profile SET stadium_capacity=%s WHERE team_code=%s', (new_stadium_capacity, team_code))

def update_nickname_of_team_code(new_nickname, team_code):
    with ConnectionPool() as cursor:
        cursor.execute('UPDATE teams_profile SET nickname=%s WHERE team_code=%s', (new_nickname, team_code))

def update_name_of_team_code(new_name, team_code):
    with ConnectionPool() as cursor:
        cursor.execute('UPDATE teams_profile SET full_name=%s WHERE team_code=%s', (new_name, team_code))


def get_teams():
    with ConnectionPool() as cursor:
        cursor.execute('SELECT * FROM teams_profile ORDER BY team_code ASC')
        teams = cursor.fetchall()
        return teams

def see_current_teams():
    return get_teams()

def add_team(country, full_name, homepage, nickname, stadium, team, stadium_capacity, team_code, founded):
    with ConnectionPool() as cursor:
        cursor.execute('INSERT INTO teams_profile VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)', (country, full_name, homepage, nickname, stadium, team, stadium_capacity, team_code, founded))
        return get_teams()

def delete_from_match_report(team_code):
    with ConnectionPool() as cursor:
        cursor.execute('DELETE FROM match_report WHERE team_code=\'{0}\''.format(team_code))

def delete_team(team_code):
    with ConnectionPool() as cursor:
        cursor.execute('UPDATE teams_profile SET nickname=%s WHERE team_code=%s', ("lololol", team_code))
        cursor.execute('DELETE FROM season_teams_v2 WHERE team_code=\'{0}\''.format(team_code))
        cursor.execute('DELETE FROM all_matches WHERE team1_code=\'{0}\''.format (team_code))
        cursor.execute('DELETE FROM all_matches WHERE team2_code=\'{0}\''.format(team_code))
        cursor.execute('DELETE FROM teams_profile WHERE team_code=\'{0}\''.format(team_code))

class Teams_Profile(object):
    def __init__(self, country, full_name, team_code):
        self.country = country
        self.team_code = team_code
        self.full_name =  full_name
        self.homepage =  None
        self.nickname =  None
        self.stadium =  None
        self.team =  None
        self.stadium_capacity =  None
        self.founded = None

    def __init__(self, country, full_name, homepage, nickname, stadium, team, stadium_capacity, team_code, founded):
        self.country = country
        self.team_code = team_code
        self.full_name =  full_name
        self.homepage =  homepage
        self.nickname =  nickname
        self.stadium =  stadium
        self.team =  team
        self.stadium_capacity =  stadium_capacity
        self.founded = founded

    def read_from_db(self):
        with ConnectionPool() as cursor:
            cursor.execute('select country, full_name, homepage, nickname, stadium, team, stadium_capacity, founded, team_code from teams_profile where team_code = %s', (self.team_code))
            team = cursor.fetchone()
            self.country = team[0]
            print(self.country)
            self.full_name = team[1]
            print(self.full_name)
            self.homepage = team[2]
            print(self.homepage)
            self.nickname = team[3]
            print(self.nickname)
            self.stadium = team[4]
            print(self.stadium)
            self.team = team[5]
            print(self.team)
            self.stadium_capacity = team[6]
            print(self.stadium_capacity)   
            self.founded = team[7]
            print(self.founded) 
            self.team_code = team[8]
            print(self.team_code) 