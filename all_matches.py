from psycopg2.sql import NULL

from dbconn import Database
from dbconn import ConnectionPool


class All_Matches_Db():

    @classmethod
    def load_season(cls):
        with ConnectionPool() as cursor:
            cls.season_arr = []
            cursor.execute('select season from all_matches group by season order by season')
            seasons = cursor.fetchall()
        for season in seasons:
            if season[0]!=None:
                cls.season_arr.append(season[0])
        return cls.season_arr

    @classmethod
    def take_match(cls, season):
        with ConnectionPool() as cursor:
            cls.date_arr = []
            cursor.execute('select * from all_matches where season=%s order by subid', (season,))
            dates = cursor.fetchall()
        for date in dates:
            cls.date_arr.append(date)
        return cls.date_arr

    @classmethod
    def edit_match(cls, match):
        with ConnectionPool() as cursor:
            cursor.execute('select * from all_matches where subid=%s ', (match,))
            cls.match = cursor.fetchone()
        return cls.match

    @classmethod
    def update_match(cls, subid,round,date_time,pso,aet,team1_code,team1_name,ht_team1_goals,ft_team1_goals,et_team1_goals,ps_team1_goals,
                     team2_code,team2_name,ht_team2_goals,ft_team2_goals,et_team2_goals,ps_team2_goals):
        with ConnectionPool() as cursor:
            try:
                cursor.execute('UPDATE all_matches SET round=%s, date_time=%s,pso=%s,aet=%s,team1_code=%s,team1_name=%s, ht_team1_goals=%s,ft_team1_goals=%s, et_team1_goals=%s,ps_team1_goals=%s,team2_code=%s,team2_name=%s,ht_team2_goals=%s,ft_team2_goals=%s,et_team2_goals=%s, ps_team2_goals=%s where subid=%s'
                               ,(round,date_time,pso,aet,team1_code,team1_name,ht_team1_goals,ft_team1_goals,et_team1_goals,ps_team1_goals,team2_code,team2_name,ht_team2_goals,ft_team2_goals,et_team2_goals,ps_team2_goals,subid,))
            except Exception as err:
                return err

    @classmethod
    def insert_match(cls,  round, date_time, pso, aet, team1_code, team1_name, ht_team1_goals, ft_team1_goals, et_team1_goals, ps_team1_goals, team2_code, team2_name, ht_team2_goals, ft_team2_goals, et_team2_goals, ps_team2_goals,saeson):
        with ConnectionPool() as cursor:
            try:
                cursor.execute("insert into all_matches (season,round,date_time,pso,aet,team1_code,team1_name, ht_team1_goals,ft_team1_goals, et_team1_goals,ps_team1_goals,team2_code,team2_name,ht_team2_goals,ft_team2_goals,et_team2_goals, ps_team2_goals) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                    ,(saeson,round, date_time, pso, aet, team1_code, team1_name, ht_team1_goals, ft_team1_goals, et_team1_goals,
                       ps_team1_goals, team2_code, team2_name, ht_team2_goals, ft_team2_goals, et_team2_goals,
                       ps_team2_goals,))
            except Exception as err:
                return err

    @classmethod
    def delete_match(cls, subid):
        with ConnectionPool() as cursor:
            cursor.execute('delete from all_matches where subid=%s ', (subid,))
