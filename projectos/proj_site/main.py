import os
import flask

app = flask.Flask(__name__)

@app.route("/")
def root():
    return flask.render_template("index.html")

@app.route("/birage")
def birage():
    return "I'M BIRAGING RN FR FR!! 😠" 

@app.errorhandler(404)
def page_not_found(_):
    return flask.render_template("error.html", error=404), 404


@app.route("/favicon.ico")
def favicon():
    return flask.send_from_directory(os.path.join(app.root_path, "static"),
                               "favicon.ico", mimetype="image/vnd.microsoft.icon")

if __name__ == "__main__":
    app.run(debug=True)