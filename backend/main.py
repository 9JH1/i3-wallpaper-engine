from res.scrape import networkBypass
from res.monitors import *
from res.set import getDirFiles
import flask 
import flask_cors
import os
import signal

app = flask.Flask(__name__)
CORS = flask_cors.CORS(app)

@app.route("/get_from_dir/<path>")
def return_dir(path):
    return flask.jsonify(getDirFiles(path))



@app.route("/")
def show_root():
    return "i3-wallpaper-engine"

@app.route(f"/off")
def stop_server():
    os.kill(os.getpid(), signal.SIGINT)
    return flask.jsonify({"success": True, "message": "Server is shutting down..."})


@app.route("/frontend_main")
def show_main():
    return flask.render_template("/index.html")

if __name__ == "__main__":
    app.run(port=22301)