from flask import Flask
import os
from datetime import datetime
import subprocess

app = Flask(_name_)

@app.route('/htop')
def htop():
    # Get system username
    username = os.getlogin()

    # Get current server time in IST
    server_time = datetime.now().astimezone().strftime("%Y-%m-%d %H:%M:%S")

    # Get top command output
    top_output = subprocess.check_output(['top', '-bn', '1']).decode('utf-8')

    return f'''
    <h1>System Information</h1>
    <p>Name: Your Full Name</p>
    <p>Username: {username}</p>
    <p>Server Time (IST): {server_time}</p>
    <h2>Top Output:</h2>
    <pre>{top_output}</pre>
    '''

if _name_ == '_main_':
    app.run(host='0.0.0.0', port=5000)
