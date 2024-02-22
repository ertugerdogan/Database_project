from flask import Flask
import views


def create_app():
    app = Flask(__name__)
    app.config.from_object("settings")
    app.add_url_rule("/", view_func=views.home_page)
    app.add_url_rule("/ertug", view_func=views.ertug_page,methods=[ "POST","GET"])
    app.add_url_rule("/team_profiles", view_func = views.team_profiles_page, methods = ["POST", "GET"])
    app.add_url_rule("/season_teams", view_func=views.season_teams_page, methods=["POST","GET"])
    app.add_url_rule("/said", view_func=views.said_page,methods=["POST","GET"])
    app.add_url_rule("/allmatches", view_func=views.load_season)
    app.add_url_rule("/allmatches/<season>", view_func=views.take_match)
    app.add_url_rule("/allmatches/edit_match/<match>", view_func=views.edit_match)
    app.add_url_rule("/allmatches/update_match", view_func=views.update_match, methods=[ "POST","GET"])
    app.add_url_rule("/allmatches/add_match/<season>", view_func=views.add_match)
    app.add_url_rule("/allmatches/add_new_match", view_func=views.add_new_match, methods=[ "POST","GET"])
    app.add_url_rule("/wholeseason/<season>", view_func=views.whole_season)
    app.add_url_rule("/deleted/<subid>", view_func=views.delete_match)
    return app

if __name__ == "__main__":
    app = create_app()
    port = app.config.get("PORT", 5000)
    app.run(host="0.0.0.0", port=port)

