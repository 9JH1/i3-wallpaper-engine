from res.scrape import networkBypass
from res.monitors import get_monitor_names
from res.set import set_background
from res.dir import getVideos
import flask 
import flask_cors
import os
import signal

app = flask.Flask(__name__)
CORS = flask_cors.CORS(app)

@app.route("/get_videos")
def return_videos():
    return getVideos()

@app.route("/get_monitors")
def return_monitors(): 
    return get_monitor_names()

@app.route("/")
def show_root():
    return "i3-wallpaper-engine"

@app.route("/set/<monitors>/<path:paths>")
def set_background_route(monitors,paths): 
    print(monitors)
    print(paths)
    set_background(monitor=monitors,path=f"/{paths}")

    return "set"

@app.route(f"/off")
def stop_server():
    os.system("killall -q xwinwrap")
    os.kill(os.getpid(), signal.SIGINT)
    return flask.jsonify({"success": True, "message": "Server is shutting down..."})

if __name__ == "__main__":
    app.run(port=22301)