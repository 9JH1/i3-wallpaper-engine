from res.scrape import networkBypass
import flask 
import flask_cors
import os

app = flask.Flask(__name__)
CORS = flask_cors.CORS(app)
@app.route("/frontend_main")
def show_main():
    return flask.render_template("index.html")


if __name__ == "__main__":
    app.run()