@app.route('/')
def home():
    return '''
    <html>
    <head>
        <style>
            body {
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                background-color: #7289da;
            }
            .login-button {
                background-color: #5865F2;
                color: white;
                padding: 15px 30px;
                font-size: 18px;
                border: none;
                border-radius: 5px;
                cursor: pointer;
                text-decoration: none;
            }
            .login-button:hover {
                background-color: #4752c4;
            }
        </style>
    </head>
    <body>
        <a href="/login" class="login-button">Log in with Discord</a>
    </body>
    </html>
    '''
