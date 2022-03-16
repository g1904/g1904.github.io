
import flask
import pandas as pd
import joblib

app = flask.Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hw2():
    if (flask.request.method == 'POST'):
        return calculate();
    return flask.render_template("homework2.html")

def calculate():
    if flask.request.method == 'POST':
        clf = joblib.load("/home/guest1904/mysite/myregr.pkl")
        age = flask.request.form['age']
        weight = flask.request.form['weight']
        x = pd.DataFrame([[age, weight]], columns=["Age", "Weight"])
        prediction = clf.predict(x)[0]
        return flask.render_template("homework2.html", result = prediction)
