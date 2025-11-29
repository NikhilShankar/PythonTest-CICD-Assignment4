from flask import Flask
from datetime import datetime

app = Flask(__name__)

# This will be set during deployment
DEPLOYMENT_TIME = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

@app.route('/')
def hello():
    return f"""Hello from Richard and Nikhil.  This is the version deployed on {DEPLOYMENT_TIME}

    Triggering pipeline for CICD Assignment 4.
"""

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9876)
