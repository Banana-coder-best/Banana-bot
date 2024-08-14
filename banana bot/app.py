from flask import Flask, redirect, request, session, url_for
import requests
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

CLIENT_ID = 'your_discord_client_id'
CLIENT_SECRET = 'your_discord_client_secret'
REDIRECT_URI = 'http://127.0.0.1:5000/callback'

@app.route('/')
def home():
    return '<a href="/login"><button>Log in with Discord</button></a>'

@app.route('/login')
def login():
    return redirect(
        f"https://discord.com/api/oauth2/authorize?client_id={CLIENT_ID}&redirect_uri={REDIRECT_URI}&response_type=code&scope=identify"
    )

@app.route('/callback')
def callback():
    code = request.args.get('code')
    data = {
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': REDIRECT_URI,
    }

    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    r = requests.post('https://discord.com/api/oauth2/token', data=data, headers=headers)
    r.raise_for_status()
    access_token = r.json().get('access_token')

    user_info = requests.get('https://discord.com/api/users/@me', headers={
        'Authorization': f'Bearer {access_token}'
    }).json()

    return f"Hello, {user_info['username']}!"

if __name__ == '__main__':
    app.run(debug=True)
