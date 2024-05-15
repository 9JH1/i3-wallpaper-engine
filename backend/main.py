from res.scrape import networkBypass
from res.monitors import *
from res.dir import getVideos
import flask 
import flask_cors
import os
import signal

app = flask.Flask(__name__)
CORS = flask_cors.CORS(app)

@app.route("/get_videos")
def return_dir():
    return getVideos()



@app.route("/")
def show_root():
    return "i3-wallpaper-engine"

@app.route(f"/off")
def stop_server():
    os.kill(os.getpid(), signal.SIGINT)
    return flask.jsonify({"success": True, "message": "Server is shutting down..."})

if __name__ == "__main__":
    app.run(port=22301)