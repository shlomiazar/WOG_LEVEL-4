import linecache
from flask import Flask, render_template

import utilis

app = Flask(__name__)


@app.route('/')
def score_server():
    filename = utilis.SCORES_FILE_NAME

    def readScore():
        s = open(filename)
        while True:
            score = s.readline()
            return score

    try:
        s = readScore()
        if int(s) < 1:
            raise ValueError
        else:
            return render_template('Scores.html', SCORE=s)
    except Exception as e:
        return render_template('Error.html', ERROR=e)


def run():
    app.run()
