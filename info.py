from dbconn import ConnectionPool

class Profile(object):
    def __init__(self, infoid):
        self.infoid = infoid
        self.stadium = None
        self.attendance = None
        self.referee = None
        self.asst_referee_1 = None
        self.asst_referee_2 = None
        self.matchid = None
    def readDb(self):
        with ConnectionPool() as cursor:
            cursor.execute('infoid,stadium,attendance,referee,asst_referee_1,asst_referee_2,matchid from match_info where infoid = %s', (self.infoid,))
            match_info = cursor.fetchone()
            self.infoid = match_info[0]
            self.stadium = match_info[1]
            self.attendance = match_info[2]
            self.referee = match_info[3]
            self.asst_referee_1 = match_info[4]
            self.asst_referee_2 = match_info[5]
            self.matchid = match_info[6]

def GetMatch(infoid):
    with ConnectionPool() as cursor:
        cursor.execute('SELECT * FROM match_info WHERE infoid = %s', (infoid,))
        return cursor.fetchall()

def GetAttendance(infoid):
    with ConnectionPool() as cursor:
        cursor.execute('SELECT DISTINCT stadium, attendance FROM match_info WHERE infoid = %s', (infoid,))
        return cursor.fetchall()

def GetReferee(infoid):
    with ConnectionPool() as cursor:
        cursor.execute('SELECT DISTINCT referee,asst_referee_1,asst_referee_2 FROM match_info WHERE infoid = %s', (infoid,))
        return cursor.fetchall()

def GetMostMachesForReferee():
    with ConnectionPool() as cursor:
        cursor.execute('SELECT referee, COUNT(*) FROM match_info GROUP BY referee ORDER BY COUNT(*) DESC')
        return cursor.fetchall()

def GetTopAttendanceMatch():
    with ConnectionPool() as cursor:
        NA='NA'
        cursor.execute('SELECT stadium,attendance FROM match_info WHERE attendance != %s GROUP BY stadium,attendance ORDER BY CAST(attendance as float) DESC',(NA,))
        return cursor.fetchall()

    
def InsertDb(stadium,attendance,referee,asst_referee_1,asst_referee_2, matchid):
    with ConnectionPool() as cursor:
        cursor.execute('INSERT INTO match_info(stadium,attendance,referee,asst_referee_1,asst_referee_2,matchid) VALUES (%s, %s, %s, %s, %s, %s)', (stadium,attendance,referee,asst_referee_1,asst_referee_2,matchid,))

def DeleteDb(infoid):
    with ConnectionPool() as cursor:
        try:
            cursor.execute('DELETE FROM match_info WHERE infoid=%s', (infoid,))
            return 0
        except Exception:
            return "err"

def UpdateStadium(stadium,infoid):
    with ConnectionPool() as cursor:
        try:
            cursor.execute('UPDATE match_info SET stadium=%s  WHERE infoid=%s', (stadium,infoid,))
            return 0
        except Exception:
            return "err"

def UpdateAttendance(attendance,mathchid):
    with ConnectionPool() as cursor:
        try:
            cursor.execute('UPDATE match_info SET attendance=%s  WHERE infoid=%s', (attendance,mathchid,))
            return 0
        except Exception:
            return "err"

def UpdateReferee(referee,infoid):
    with ConnectionPool() as cursor:
        try:
            cursor.execute('UPDATE match_info SET referee=%s  WHERE infoid=%s', (referee,infoid,))
            return 0
        except Exception:
            return "err"
    
def UpdateAsstReferees(infoid,asst_referee_1,asst_referee_2):
    with ConnectionPool() as cursor:
        try:
            cursor.execute('UPDATE match_info SET asst_referee_1=%s AND asst_referee_2=%s  WHERE infoid=%s', (asst_referee_1,asst_referee_2,infoid,))
            return 0
        except Exception:
            return "err"
    
def UpdateAllAsstReferees(referee,asst_referee_1,asst_referee_2):
    with ConnectionPool() as cursor:
        try:
            cursor.execute('UPDATE match_info SET asst_referee_1=%s AND asst_referee_2=%s  WHERE referee=%s', (asst_referee_1,asst_referee_2,referee,))
            return 0
        except Exception:
            return "err"

def Update(infoid,column,changing):
    if(column=='stadium'):
       UpdateStadium(changing,infoid)
    elif(column=='attendance'):
       UpdateAttendance(changing,infoid)
    elif(column=='referee'):
       UpdateReferee(changing,infoid)

def UpdateReferee(column,changing1,changing2):
    if(column=='asstreferees'):
       UpdateAsstReferees(column,changing1,changing2)
    elif(column=='refereeasst'):
       UpdateAllAsstReferees(column,changing1,changing2)