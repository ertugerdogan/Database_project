from datetime import datetime
from flask import current_app, render_template,request
import report
import info
from all_matches import All_Matches_Db
import array as arr
from dbconn import Database
from dbconn import ConnectionPool

def home_page():
    today = datetime.today()
    day_name = today.strftime("%A")
    return render_template("home.html", day=day_name)

def login_page():
    return render_template("login.html")


# ERTUG 

def select(array):
    with ConnectionPool() as cursor:
        line = ''
        if array[0]==1:
            if line=='':
                line='jersey_no,'
            else:
                line=line+' jersey_no,'
            print(line)
            #cursor.execute('SELECT * FROM match_report WHERE player = %s', (user_id,))
        if array[1]==1:
            if line=='':
                line='player,'
            else:
                line=line+' player,'
        if array[2]==1:
            if line=='':
                line='card_time,'
            else:
                line=line+' card_time,'
        if array[3]==1:
            if line=='':
                line='substitution_time,'
            else:
                line=line+' substitution_time,'
        if array[4]==1:
            if line=='':
                line='p_s,'
            else:
                line=line+' p_s,'
        if array[5]==1:
            if line=='':
                line='team_code,'
            else:
                line=line+' team_code,'
        if array[6]==1:
            if line=='':
                line='goal_time,'
            else:
                line=line+' goal_time,'
        if array[7]==1:
            if line=='':
                line='match_id,'
            else:
                line=line+' match_id,'
        if array[8]==1:
            if line=='':
                line='_id,'
            else:
                line=line+' _id,'
        final=line[:-1]
        print(final)
        with ConnectionPool() as cursor:
            print('Hello')
            stmr='SELECT '
            stmr+=final
            stmr+=' FROM match_report'
            cursor.execute(stmr)
            data = cursor.fetchall()
            print(data)
            #for row in data:
            #   print(row)

            return data        
            #cursor.close()

    #cursor.execute('SELECT %s FROM match_report ', (final,))

def ertug_page():
    numbers = [0] * 9
    data=[]
    new_data=[]

    if request.method=='POST' and request.form.get("type")=="playerchange" :
        print("playerchange")
        _id=request.form.get("_id")
        player=request.form.get("player")
        variable=request.form.get("variable")
        changing=request.form.get("changing")
        report.Update(_id,player, variable,changing)
        return render_template("/ertug.html",data=data,new_data=new_data)
    elif  request.method=='POST' and request.form.get("type")=="vehicleselect" :
        #numbers=arr.array('i',[0,0,0,0,0,0,0,0])
       
        if  request.form.get("feature1")=="jersey_no" :
            print("jersey_no selected")
            numbers[0]=1
            for i in range (0, 9):
               print(numbers[i], end =" ")
        if  request.form.get("feature2")=="player" :
            print("player selected")
            numbers[1]=1
            for i in range (0, 9):
               print(numbers[i], end =" ")
        if  request.form.get("feature3")=="card_time" :
            print("card_time selected")
            numbers[2]=1
            for i in range (0, 9):
               print(numbers[i], end =" ")
        if  request.form.get("feature4")=="substituion_time" :
            print("substituion_time selected")
            numbers[3]=1
            for i in range (0, 9):
               print(numbers[i], end =" ")
        if  request.form.get("feature5")=="p_s" :
            print("p_s selected")
            numbers[4]=1
            for i in range (0, 9):
               print(numbers[i], end =" ")
        if  request.form.get("feature6")=="team_code" :
            print("team_code selected")
            numbers[5]=1
            for i in range (0, 9):
               print(numbers[i], end =" ")
        if  request.form.get("feature7")=="goal_time" :
            print("goal_time selected")
            numbers[6]=1
            for i in range (0, 9):
               print(numbers[i], end =" ")
        if  request.form.get("feature8")=="match_id" :
            print("match_id selected")
            numbers[7]=1
            for i in range (0, 9):
               print(numbers[i], end =" ")
        if  request.form.get("feature9")=="_id" :
            print("_id selected")
            numbers[8]=1
            for i in range (0, 9):
               print(numbers[i], end =" ")
        data=select(numbers)
        return render_template("/ertug.html",data=data,new_data=new_data)
    elif  request.method=='POST' and request.form.get("type")=="radiobuttons" :
        if  request.form.get("FEATURE")=="1" :
            print("Top Scorer")
            data=report.load_mostcard()
        elif  request.form.get("FEATURE")=="2" :
            data=report.load_topscorer()
            print("60")

        return render_template("/ertug.html",data=data,new_data=new_data)
    elif  request.method=='POST' and request.form.get("type") == "Teams":
        print("hello")
        data=report.load_teamplayers(request.form.get("teams")) 
        return render_template("/ertug.html",data=data,new_data=new_data) 
    elif  request.method=='POST' and request.form.get("type") == "newone":
        print("Hi")
        print(request.form.get("username"))
        #data=report.validation_func(request.form.get("username"))
        new_data=report.validation_func(request.form.get("username"))
        print(new_data)
        if(new_data):
           print(new_data)
           return render_template("/ertug.html",data=data,new_data=new_data)
        else:
            new_data=["No such player found in the Indian league"]
            #updatedData.append("No such player found in the Indian league")
            return render_template("/ertug.html",data=data,new_data=new_data) 
    elif request.method=='POST' and request.form.get("type")=="createplayer" :
        print("createplayer")
        jersey_no=request.form.get("jersey_no")
        player=request.form.get("player")
        card_time=request.form.get("card_time")
        substitution_time=request.form.get("substitution_time")
        p_s=request.form.get("p_s")
        team_code=request.form.get("team_code")
        goal_time=request.form.get("goal_time")
        match_id=request.form.get("match_id")

        report.Insert_db(jersey_no,player,card_time, substitution_time, p_s,team_code,goal_time,match_id)
        return render_template("/ertug.html",data=data,new_data=new_data) 

    elif request.method=='POST' and request.form.get("type")=="deleteplayer":
        _id=request.form.get("_id")
        report.Delete_db(_id)
        return render_template("/ertug.html",data=data,new_data=new_data) 
    else:
        return render_template("/ertug.html",data=data)





# KERIM - TEAM_PROFILES
import team_profiles

def get_teams():
    teams = team_profiles.get_teams()
    teams_ = []
    for team in teams:
        teams_.append(team_profiles.Teams_Profile(team[0], team[1], team[2], team[3], team[4], team[5], team[6], team[7], team[8]))
    return teams_

def team_profiles_page():
    if request.method == "POST":
        if request.form.get("type") == "team_update":
            team_code = request.form.get("team_code")
            team_name = request.form.get("updated_name")
            team_homepage = request.form.get("updated_homepage")
            team_stadium = request.form.get("updated_stadium")
            team_stadium_capacity = request.form.get("updated_stadium_capacity")
            team_founded = request.form.get("updated_founded")
            team_country = request.form.get("updated_country")
            team_nickname = request.form.get("updated_nickname")

            if team_homepage != None and team_homepage != "":
                team_profiles.update_homepage_of_team_code(team_homepage, team_code)
            if team_name != None and team_name != "":
                team_profiles.update_name_of_team_code(team_name, team_code)
            if team_stadium != None and team_stadium != "":
                team_profiles.update_stadium_of_team_code(team_stadium, team_code)
            if team_stadium_capacity != None and team_stadium_capacity != "":
                team_profiles.update_capacity_of_team_code(team_stadium_capacity, team_code)
            if team_founded != None and team_founded != "":
                team_profiles.update_founded_of_team_code(team_founded, team_code)
            if team_country != None and team_country != "":
                team_profiles.update_country_of_team_code(team_country, team_code)
            if team_nickname != None and team_nickname != "":
                team_profiles.update_nickname_of_team_code(team_nickname, team_code)

            return render_template("team_profiles.html")

        elif request.form.get("type") == "see_current_teams":
            teams = get_teams()
            return render_template("team_profiles.html", teams=teams)

        elif request.form.get("type") == "delete_team":
            team_code = request.form.get("team_code")
            team_profiles.delete_from_match_report(team_code)
            team_profiles.delete_team(team_code)
            teams = get_teams()
            return render_template("team_profiles.html", teams=teams)

        elif request.form.get("type") == "add_team":
            country = request.form.get("add_country")
            full_name = request.form.get("add_full_name")
            homepage = request.form.get("add_homepage")
            nickname = request.form.get("add_nickname")
            stadium = request.form.get("add_stadium")
            team = request.form.get("add_team")
            stadium_capacity  = request.form.get("add_stadium_capacity")
            team_code = request.form.get("add_team_code")
            founded = request.form.get("add_founded")
            print(country)
            team_profiles.add_team(country, full_name, homepage, nickname, stadium, team, stadium_capacity, team_code, founded)
            teams = get_teams()
            return render_template("team_profiles.html",teams=teams)
            
        else:
            return login_page()
    else:
        return render_template("team_profiles.html")

# KERIM - SEASON TEAMS
import season_teams
def season_teams_page():
    if request.method == "POST":
        if request.form.get("type") == "season_selection_submit":
            season = request.form.get("seasons_selector")
            teams = season_teams.get_teams_of_season(season=season)
            print(teams)
            teams_ = []
            for team in teams:
                teams_.append(season_teams.Season_Teams(team[1], team[2], team[3], team[4]))
                print(team[1], team[2], team[3], team[4])
            return render_template("season_teams.html", teams=teams_)
        return render_template("season_teams.html")
    else:
        seasons = sorted(set(season_teams.get_seasons()))
        return render_template("season_teams.html", seasons=seasons)


# CEDAN
def load_season():
    seasons = All_Matches_Db.load_season()
    return render_template("all_matches.html", seasons=seasons)


def take_match(season):
    dates = All_Matches_Db.take_match(season)
    return render_template("match.html", dates=dates)

def edit_match(match):
    match = All_Matches_Db.edit_match(match)
    return render_template("editmatch.html", match=match)

def update_match():
    if request.method == 'POST' and request.form.get("type") == "matchupdate":
        subid= request.form.get("subid")
        round = request.form.get("round")
        date_time = request.form.get("date_time")
        pso = request.form.get("pso")
        aet = request.form.get("aet")
        team1_code = request.form.get("team1_code")
        team1_name = request.form.get("team1_name")
        ht_team1_goals = request.form.get("ht_team1_goals")
        ft_team1_goals = request.form.get("ft_team1_goals")
        et_team1_goals = request.form.get("et_team1_goals")
        ps_team1_goals = request.form.get("ps_team1_goals")
        team2_code = request.form.get("team2_code")
        team2_name = request.form.get("team2_name")
        ht_team2_goals = request.form.get("ht_team2_goals")
        ft_team2_goals = request.form.get("ft_team2_goals")
        et_team2_goals = request.form.get("et_team2_goals")
        ps_team2_goals = request.form.get("ps_team2_goals")
        All_Matches_Db.update_match(subid, round, date_time, pso, aet, team1_code, team1_name, ht_team1_goals, ft_team1_goals, et_team1_goals, ps_team1_goals, team2_code, team2_name, ht_team2_goals, ft_team2_goals, et_team2_goals, ps_team2_goals)
        seasons=All_Matches_Db.load_season()
        return render_template("all_matches.html", seasons=seasons)

def add_match(season):
    return render_template("addmatch.html",season=season)

def add_new_match():
    if request.method == 'POST' and request.form.get("type") == "addmatch":
        saeson=request.form.get("season")
        round = request.form.get("round")
        date_time = request.form.get("date_time")
        pso = request.form.get("pso")
        aet = request.form.get("aet")
        team1_code = request.form.get("team1_code")
        team1_name = request.form.get("team1_name")
        ht_team1_goals = request.form.get("ht_team1_goals")
        ft_team1_goals = request.form.get("ft_team1_goals")
        et_team1_goals = request.form.get("et_team1_goals")
        ps_team1_goals = request.form.get("ps_team1_goals")
        team2_code = request.form.get("team2_code")
        team2_name = request.form.get("team2_name")
        ht_team2_goals = request.form.get("ht_team2_goals")
        ft_team2_goals = request.form.get("ft_team2_goals")
        et_team2_goals = request.form.get("et_team2_goals")
        ps_team2_goals = request.form.get("ps_team2_goals")
        All_Matches_Db.insert_match(round, date_time, pso, aet, team1_code, team1_name, ht_team1_goals, ft_team1_goals, et_team1_goals, ps_team1_goals, team2_code, team2_name, ht_team2_goals, ft_team2_goals, et_team2_goals, ps_team2_goals,saeson)
        seasons=All_Matches_Db.load_season()
        return render_template("all_matches.html", seasons=seasons)

def whole_season(season):
    dates = All_Matches_Db.take_match(season)
    return render_template("whole_season.html", dates=dates)

def delete_match(subid):
    All_Matches_Db.delete_match(subid)
    seasons = All_Matches_Db.load_season()
    return render_template("all_matches.html", seasons=seasons)

def said_page():
    data_=[]
    updatedData_=[]
    if request.method=='POST' and request.form.get("type")=="matchchange" :
        infoid=request.form.get("infoid")
        column=request.form.get("column")
        changing=request.form.get("changing")
        message = info.Update(infoid,column,changing)
        if message == "err":
            updatedData_ = ["Please try again and enter valid variables"]
        else:
            updatedData_ = ["Match Updated with infoid: "  + infoid]
        return render_template("/said.html",data_=data_,updatedData_=updatedData_)
    elif request.method=='POST' and request.form.get("type")=="refereechange" :
        column=request.form.get("column")
        changing1=request.form.get("changing1")
        changing2=request.form.get("changing2")
        if message == "err":
            updatedData_ = ["Please try again and enter valid variables"]
        else:
            updatedData_ = ["Match Updated: "  + column]
        info.UpdateReferee(column,changing1,changing2)
        
        return render_template("/said.html",data_=data_,updatedData_=updatedData_)
    elif  request.method=='POST' and request.form.get("type")=="typeselect" :
        column = ''
        if  request.form.get("column1")=="infoid" :
            column=column+' infoid,'
        if  request.form.get("column2")=="stadium" :
            column=column+' stadium,'
        if  request.form.get("column3")=="attendance" :
            column=column+' attendance,'
        if  request.form.get("column4")=="referee" :
            column=column+' referee,'
        if  request.form.get("column5")=="asst_referee_1" :
            column=column+' asst_referee_1,'
        if  request.form.get("column6")=="asst_referee_2" :
            column=column+' asst_referee_2,'
        if  request.form.get("column7")=="matchid" :
            column=column+' matchid,'
        final=column[:-1]
        with ConnectionPool() as cursor:
            str='SELECT '
            str+=final
            str+=' FROM match_info'
            cursor.execute(str)
            data_ = cursor.fetchall()
        return render_template("/said.html",data_=data_,updatedData_=updatedData_)
    elif  request.method=='POST' and request.form.get("type")=="radiobuttons" :
        if  request.form.get("FEATURE")=="1" :
            data_=info.GetTopAttendanceMatch()
        elif  request.form.get("FEATURE")=="2" :
            data_=info.GetMostMachesForReferee()
        return render_template("/said.html",data_=data_,updatedData_=updatedData_)
    elif request.method=='POST' and request.form.get("type")=="creatematch" :
        stadium=request.form.get("stadium")
        attendance=request.form.get("attendance")
        referee=request.form.get("referee")
        asst_referee_1=request.form.get("asst_referee_1")
        asst_referee_2=request.form.get("asst_referee_2")
        matchid=request.form.get("matchid")
        message = info.InsertDb(stadium,attendance,referee, asst_referee_1,asst_referee_2,matchid)
        updatedData_ = ["Match Insterted with infoid: " + infoid]
        return render_template("/said.html",data_=data_,updatedData_=updatedData_) 
    elif request.method=='POST' and request.form.get("type")=="deletematch":
        infoid=request.form.get("infoid")
        message = info.DeleteDb(infoid)
        if message == "err":
            updatedData_ = ["Please try again and enter valid infoid"]
        else:
            updatedData_ = ["Match Deleted with infoid: " + infoid]
        return render_template("/said.html",data_=data_,updatedData_=updatedData_) 
    elif  request.method=='POST' and request.form.get("type") == "getmatch":
        data_=info.GetMatch(request.form.get("infoid"))
        return render_template("/said.html",data_=data_,updatedData_=updatedData_) 
    elif  request.method=='POST' and request.form.get("type") == "getattendance":
        data_=info.GetAttendance(request.form.get("infoid"))
        return render_template("/said.html",data_=data_,updatedData_=updatedData_) 
    elif  request.method=='POST' and request.form.get("type") == "getreferees":
        data_=info.GetReferee(request.form.get("infoid"))
        return render_template("/said.html",data_=data_,updatedData_=updatedData_)
    else:
        return render_template("/said.html",data_=data_)
