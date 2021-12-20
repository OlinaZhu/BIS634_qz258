from flask import Flask, render_template, request, abort
import json
import pandas as pd

app = Flask(__name__)

# I've downloaded incd.csv from
# https://statecancerprofiles.cancer.gov/incidencerates/index.php?stateFIPS=00&areatype=state&cancer=001&race=00&sex=0&age=001&stage=999&year=0&type=incd&sortVariableName=rate&sortOrder=default&output=0#results
# NOTE: I'm using the CSV unedited. You may have chosen to edit it.

# here we're skipping 8 rows of headers and the last several lines... you could
# have also just edited the file you got from cancer.gov
data = pd.read_csv("incd.csv", skiprows=list(range(0, 8)) + list(range(63, 97)))

# get rid of the parentheses in the state names
# I'm also lower-casing the state name to make it easier to do case-insensitive
# matches later
data["State"] = data["State"].apply(lambda name: name.split("(")[0].strip().lower())


@app.route("/")
def index():
    return render_template("index.html")


def get_state_data(name):
    name_lower = name.lower()
    incidence = data[data["State"] == name_lower][
        "Age-Adjusted Incidence Rate([rate note]) - cases per 100,000"
    ].values
    # should be exactly one match; if not, the state is missing or something
    # is wrong with our dataframe
    assert len(incidence) == 1
    return incidence[0]


@app.route("/state/<string:name>")
def state(name):
    try:
        incidence = get_state_data(name)
    except:
        # if that fails, then no such state so 404 error
        abort(404)
    return json.dumps({"state": name, "age_adjusted_incidence_rate": incidence})


@app.route("/info", methods=["GET"])
def info():
    name = request.args.get("name")
    print(f"name={name}")
    try:
        incidence = get_state_data(name)
    except:
        # if that fails, then no such state so display the failure page
        # important: this is not a 404 here
        return render_template("info-failure.html", name=name)
    return render_template("info.html", name=name, incidence=incidence)


if __name__ == "__main__":
    app.run(debug=True)
