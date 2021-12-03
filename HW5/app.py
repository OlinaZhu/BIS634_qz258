# import libraries
import jinja2
import pandas as pd
from flask import Flask, render_template, redirect, request, url_for, jsonify

# import data
# keep only state and CI columns
df = pd.read_csv("incd.csv")
df.drop(df.columns.difference(['State', 'Age-Adjusted IR']), 1, inplace=True)

# set all state names to lower case
df['State'] = df['State'].str.lower()

# implement a server that provides three routes using flask
app = Flask(__name__)

# the index/homepage written in HTML which prompts the user to enter a state
# and provides a button, which passes this information to /info
@app.route("/")
def index():
    name = request.form.get("name")
    return render_template("index.html")

# a web page that takes the name of the state as a GET argument and
# (1) if the state name is valid, displays the same information as the API in an HTML page
# or (2) displays an error if the state name is invalid
# includes a link back to the homepage
@app.route("/info", methods=["GET"])
def info():
    name = request.args.get("name", None)
    name = name.lower()
    if name in df['State']:
        state(name)
        return render_template("info.html", states=list(df['States']))
    else:
        return render_template("failure.html")

# an API that returns JSON-encoded data containing the name of the state
# and the age-adjusted incidence rate (cases per 100k)
# NOTE: in this case, the name of the state is part of the URL itself;
# it is not passed in as a GET or POST argument

@app.route("/state/<string:name>")
def state(name):
    return jsonify(
        state=name,
        age_adjusted_incidence_rate=float(df[df["State"] == name, 'Age-Adjusted IR'])
    )


if __name__ == "__main__":
    app.run(debug=True)
