import requests, os, urllib.parse
from flask import Flask, render_template, redirect, url_for, request
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


def exchange_token(code):
    print("yes")
    strava_request = requests.post(
        'https://www.strava.com/oauth/token',
        data={
            'client_id': os.environ.get('client_id'),
            'client_secret': os.environ.get('client_secret'),
            'code': code,
            'grant_type': 'authorization_code'
        },
        timeout=10
    )
    print(strava_request.json())


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/strava_authorise', methods=['GET'])
def strava_authorise():
    params = {
        'client_id': os.environ.get('client_id'),
        'redirect_uri': 'http://localhost:5000/strava_token',
        'response_type': 'code',
        'scope': 'activity:read_all'
    }
    return redirect('{}?{}'.format('https://www.strava.com/oauth/authorize',
                                   urllib.parse.urlencode(params)))


@app.route('/strava_token', methods=['GET'])
def strava_token():
    code = request.args.get('code')
    print(code)
    exchange_token(code)
    return redirect(url_for('index'))


if __name__ == '__main__':
    my_host = '127.0.0.1'
    app.run(host=my_host, debug=True)