from flask import Flask
import views
from dbconn import Database
from dbconn import ConnectionPool
import array as arr

#def create_app():
#    app = Flask(__name__)
#    app.config.from_object("settings")

#    app.add_url_rule("/", view_func=views.home_page)
#    return app

def load_user(user_id):
    with ConnectionPool() as cursor:
        cursor.execute('SELECT * FROM match_report WHERE player = %s', (user_id,))
        user_data = cursor.fetchone()
        print(user_data)

def load_teamplayers(team_id):
    with ConnectionPool() as cursor:
        cursor.execute('SELECT DISTINCT player, team_code FROM match_report WHERE team_code=  %s', (team_id,))
        user_data = cursor.fetchall()
        return user_data

def load_topscorer():
    with ConnectionPool() as cursor:
        NA='NA'
        cursor.execute('SELECT player,COUNT(*) FROM match_report WHERE goal_time !=%s GROUP BY player ORDER BY COUNT(*) DESC',(NA,))
        user_data = cursor.fetchall()
        return user_data
        #for row in user_data:
            #print(row)

def  validation_func(user_id):
    with ConnectionPool() as cursor:
        cursor.execute('SELECT DISTINCT player FROM match_report WHERE player=\'{0}\''.format(user_id,))
        user_data = cursor.fetchone()
        return user_data

def load_mostcard():
    with ConnectionPool() as cursor:
        NA='NA'
        cursor.execute('SELECT player,COUNT(*) FROM match_report WHERE card_time !=%s GROUP BY player ORDER BY COUNT(*) DESC',(NA,))
        user_data = cursor.fetchall()
        return user_data
        #for row in user_data:
            #print(row)

    
def Insert_db( jersey_no,player,card_time, substitution_time, p_s,team_code,goal_time,match_id):
    with ConnectionPool() as cursor:
        cursor.execute('INSERT INTO match_report(jersey_no,player,card_time, substitution_time, p_s,team_code,goal_time,match_id) VALUES (%s, %s, %s, %s, %s, %s,%s,%s)', (jersey_no,player,card_time, substitution_time, p_s,team_code,goal_time,match_id,))
        print('Done')

def Delete_db( _id):
    with ConnectionPool() as cursor:
        cursor.execute('DELETE FROM match_report WHERE _id=%s', (_id,))
        print('Done')


def Update_player_team_code(_id, player,team_code):
    with ConnectionPool() as cursor:
        cursor.execute('UPDATE match_report SET team_code=%s  WHERE player=%s AND _id=%s', (team_code,player,_id))
        print('Done')

def Update_player_substitution_time(_id, player,substitution_time):
    with ConnectionPool() as cursor:
        cursor.execute('UPDATE match_report SET substitution_time=%s  WHERE player=%s AND _id=%s', (substitution_time,player,_id,))
        print('Done')
    
def Update_player_jersey_no(_id, player,jersey_no):
    with ConnectionPool() as cursor:
        cursor.execute('UPDATE match_report SET jersey_no=%s  WHERE player=%s AND _id=%s', (jersey_no,player,_id,))
        print('Done')
    
def Update_player_card_time(_id, player,card_time):
    with ConnectionPool() as cursor:
        cursor.execute('UPDATE match_report SET card_time=%s  WHERE player=%s AND _id=%s', (card_time,player,_id,))
        print('Done')

def Update_player_p_s(_id, player,p_s):
    with ConnectionPool() as cursor:
        cursor.execute('UPDATE match_report SET p_s=%s  WHERE player=%s AND _id=%s', (p_s,player,_id,))
        print('Done')

def Update_player_goal_time(_id, player,goal_time):
    with ConnectionPool() as cursor:
        cursor.execute('UPDATE match_report SET goal_time=%s  WHERE player=%s AND _id=%s', (goal_time,player,_id,))
        print('Done')

def Update_player_match_id(_id, player,match_id):
    with ConnectionPool() as cursor:
        cursor.execute('UPDATE match_report SET match_id=%s  WHERE player=%s AND _id=%s', (match_id,player,_id,))
        print('Done')

def Update(_id,player, variable,changing):
    if(variable=='team_code'):
       Update_player_team_code(_id,player,changing)   
    elif(variable=='substitution_time'):
       Update_player_substitution_time(_id,player,changing) 
    elif(variable=='jersey_no'):
       Update_player_jersey_no(_id,player,changing) 
    elif(variable=='card_time'):
       Update_player_card_time(_id,player,changing) 
    elif(variable=='p_s'):
       Update_player_p_s(_id,player,changing) 
    elif(variable=='goal_time'):
       Update_player_goal_time(_id,player,changing) 
    elif(variable=='match_id'):
       Update_player_match_id(_id,player,changing) 

class Profile(object):
    def __init__(self,_id ,player):
        self._id = _id
        self.player=player
        self.jersey_no =  None
        self.card_time =  None
        self.substituion_time =  None
        self.p_s =  None
        self.team_code =  None
        self.goal_time =  None
        self.match_id = None

    def read_from_db(self):
        with ConnectionPool() as cursor:
            cursor.execute('select _id, jersey_no, card_time, substitution_time, p_s, goal_time, match_id from match_report where player = %s and _id = %s', (self.player,self._id,))
            match_inf = cursor.fetchone()
            self._id = match_inf[0]
            print(self._id)
            self.jersey_no = match_inf[1]
            print(self.jersey_no)
            self.card_time = match_inf[2]
            print(self.card_time)
            self.substituion_time = match_inf[3]
            print(self.substituion_time)
            self.p_s = match_inf[4]
            print(self.p_s)
            self.goal_time = match_inf[5]
            print(self.goal_time)
            self.match_id = match_inf[6]
            print(self.match_id)   
