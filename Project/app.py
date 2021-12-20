# import libraries
import pandas as pd
import seaborn as sns
import numpy as np
from statistics import mode
from matplotlib import pyplot as plt
from flask import Flask, render_template, redirect, request, url_for, jsonify
import jinja2

# import data
# data retrieved from  https://catalog.data.gov/dataset/accidental-drug-related-deaths-2012-2018
# Public Access: This dataset is intended for public access and use
# Publisher: data.ct.gov
data = pd.read_csv("Accidental_Drug_Related_Deaths_2012-2020.csv")
data.columns= data.columns.str.lower()

# _________________________________________________ DATA PREPARATION __________________________________________________

# drop redundant variables
# set to lower case column names
data = data.drop(columns=['residence city', 'residence county', 'residence state', 'death city', 'death county', 'location', 'location if other', 'injury city', 'injury county', 'injury state', 'manner of death', 'deathcitygeo', 'residencecitygeo', 'injurycitygeo'])

# set type of variable of date column to Datetime
data['date'] = pd.to_datetime(data['date'])

# clean dataset - NaN values in type of drug columns are to be interpreted as 'N' for No and not missing
# only keep NaN if all entries in row for columns in type_of_drug is NaN
type_of_drug = data[["heroin", "cocaine", "fentanyl", "fentanyl analogue", "oxycodone", "oxymorphone", "ethanol", "hydrocodone",	"benzodiazepine", "methadone", "amphet", "tramad", "morphine (not heroin)", "hydromorphone", "xylazine", "other", "opiate nos",	"any opioid"]]
row = 0
col_num = len(type_of_drug.columns)
while row < len(type_of_drug):
    num_nan = type_of_drug.iloc[row].isna().sum()
    if num_nan != col_num: type_of_drug.iloc[row].fillna("N", inplace=True)
    row += 1
data[["heroin", "cocaine", "fentanyl", "fentanyl analogue", "oxycodone", "oxymorphone", "ethanol", "hydrocodone",	"benzodiazepine", "methadone", "amphet", "tramad", "morphine (not heroin)", "hydromorphone", "xylazine", "other", "opiate nos",	"any opioid"]] = type_of_drug


# _________________________________________________ END DATA PREPARATION ______________________________________________
# _________________________________________________ API FUNCTIONS _____________________________________________________

# finding relationship between age and accidental drug-caused death
def by_age():
    ages = data.groupby('age')['id'].count().reset_index()
    age_plt = sns.lineplot(data=ages, x='age', y='id')
    age_plt.set(ylabel='Count')
    return age_plt

# find relationship between age and accidental drug-caused death by gender
def by_gender_age():
    age_gender = data.groupby(['sex', 'age'])['id'].count().reset_index()
    age_gender = age_gender[age_gender.sex != 'unknown']
    age_gender_plt = sns.lineplot(data=age_gender, x='age', y='id', hue='sex')
    age_gender_plt.set(ylabel='Count')
    return age_gender_plt

# count missing values and the proportion of each column that is missing
def missing_vals():
    nan_dict = {}
    cols = data.columns
    for col in cols:
        nan_dict[col] = [data[col].isna().sum(), round(data[col].isna().sum()/len(data[col]), 3)]
    return nan_dict

# select type of drug used and show stats
def show_drug_type_stats(drug):
    selected_drug = data[data[drug] == "Y"]
    total_count = len(selected_drug)
    if total_count == 0: return "There are no data for this drug."
    male_count = len(selected_drug[selected_drug["sex"] == 'Male'])
    female_count = len(selected_drug[selected_drug["sex"] == 'Female'])
    average_age = np.mean(selected_drug['age'])
    race_mode = mode(selected_drug['race'])

    tc = "There were " + str(total_count) + " incidences related to "+str(drug)
    mc = "Of which, the number of males is " + str(male_count)
    fc = "The number of females is " + str(female_count)
    aa = 'The average age is ' + str(average_age)
    rm = 'The most seen race is ' + str(race_mode)

    # age distribution
    age = selected_drug.groupby('age')['id'].count().reset_index()
    plt.figure()
    age_plt = sns.lineplot(data=age, x='age', y='id')
    age_plt.set(ylabel='Count')
    age_plt.set(title=drug)
    return [tc, mc, fc, aa, rm]


# _________________________________________________ END API FUNCTIONS _________________________________________________
# _________________________________________________ FLASK FUNCTIONS ___________________________________________________

# global variables to be used in html pages
# select options for generating and viewing analysis
drug_types = ["heroin", "cocaine", "fentanyl", "fentanyl analogue", "oxycodone", "oxymorphone", "ethanol", "hydrocodone",	"benzodiazepine", "methadone", "amphet", "tramad", "morphine (not heroin)", "hydromorphone", "xylazine", "other", "opiate nos",	"any opioid"]
analysis_options = ["Drug type: " + i for i in drug_types]
analysis_options = ["Age", "Age by sex", "Missing values"] + analysis_options

# implement a server that provides three routes using flask
app = Flask(__name__)

# the index/homepage written in HTML which prompts the user to select an item for analysis
# and provides a button, which passes this information to /info
@app.route("/")
def index():
    return render_template("index.html", analysis_options=analysis_options)

# a web page that takes the name of the state as a GET argument and
# (1) if one item is selected, displays the same information as the API 'view' in an HTML page
# or (2) displays an error page if none chosen
# includes a link back to the homepage
@app.route("/info", methods=["GET"])
def info():
    analysis_type = request.args.get("Actions")
    if str(analysis_type) in analysis_options:
        if str(analysis_type).split(" ")[0] == "Drug":
            # if chosen to analyze a type of drug
            drug = str(analysis_type).split(": ")[1]
            drug = drug.lower()
            response = show_drug_type_stats(drug)
            if response != "There are no data for this drug.":
                tc = str(response[0])
                mc = str(response[1])
                fc = str(response[2])
                aa = str(response[3])
                rm = str(response[4])
                src = "/static/"+drug+".png"
                render_template("info.html", analysis_type=analysis_type, src=src, total_count=tc, male_count=mc, female_count=fc, average_age=aa, race_mode=rm)
        # other analysis: return template
        else:
            src = "/static/"+analysis_type.lower()+".png"
            return render_template("info.html", analysis_type=analysis_type, src=src)
    # analysis type not included in choices: failure
    return render_template("failure.html")


# _________________________________________________ END FLASK FUNCTIONS _______________________________________________

if __name__ == "__main__":
    app.run(debug=True)
