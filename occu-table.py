from flask import Flask, render_template
from occupations import random_job, get_dict

app = Flask(__name__)

d = get_dict()


@app.route("/")
def welcome():
    return "Welcome!"

@app.route("/occupations")
def webpage():
    job = random_job()
    return render_template('main.html', keys = d, job = job, percentage = d[job][0], link = d[job][1])
if __name__ == '__main__':
    app.debug = True
    app.run()
