from res.scrape import networkBypass
from res.monitors import get_monitor_names
from res.set import set_background
from res.dir import get_videos, get_video_info
import flask 
import flask_cors
import os
import signal

app = flask.Flask(__name__)
CORS = flask_cors.CORS(app)

@app.route("/get_videos/<path:paths>")
def return_videos(paths="/"):
    return get_videos(f"/{paths}")

@app.route("/get_videos_root")
def return_videos_root():
    return get_videos("/")
@app.route("/get_monitors")
def return_monitors(): 
    return get_monitor_names()
@app.route("/")
def show_root():
    return "i3-wallpaper-engine"

@app.route("/set/<monitors>/<path:paths>")
def set_background_route(monitors,paths):
    set_background(monitor=monitors,path=f"/'{paths}'")

    return "set"

@app.route("/video_info/<path:paths>")
def return_video_info(paths): 
    return get_video_info(f"/{paths}")


@app.route(f"/off")
def stop_server():
    os.system("killall -q xwinwrap")
    os.kill(os.getpid(), signal.SIGINT)
    return flask.jsonify({"success": True, "message": "Server is shutting down..."})

if __name__ == "__main__":
    app.run(port=22301)