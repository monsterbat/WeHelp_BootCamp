"""

***| Main program |***

WeHelp BootCamp Assignemt - Week 7  Task
Update date: 2022/11/03
Authored by SC Siao
"""
from flask import Flask
import api_w7

app = Flask(
    __name__,
    static_folder="static",
    static_url_path="/"
    )

app.secret_key="secret key"

app.register_blueprint(api_w7.api_w7)

# Run app
if __name__ == '__main__':
    app.debug = True #Sync operator able
    app.run(port=3000)