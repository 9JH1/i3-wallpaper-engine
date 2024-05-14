from res.scrape import networkBypass
import flask 
import flask_cors
import os
import signal

app = flask.Flask(__name__)
CORS = flask_cors.CORS(app)


@app.route("/")
def show_root():
    return "you have found the i3-wallpaper-engine"

@app.route(f"/off")
def stopServer():
    os.kill(os.getpid(), signal.SIGINT)
    return flask.jsonify({"success": True, "message": "Server is shutting down..."})


@app.route("/frontend_main")
def show_main():
    return flask.render_template("/index.html")

if __name__ == "__main__":
    app.run(port=22301)