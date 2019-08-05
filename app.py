__author__ = "Jieshu Wang and Bilal El Uneis"
__since__ = "Aug 2019"
__email__ = "foundwonder@gmail.com and bilaleluneis@gmail.com"

from flask import Flask
from blueprint.arrays import arrays
from blueprint.stacks import stacks

app = Flask(__name__)
app.register_blueprint(arrays)
app.register_blueprint(stacks)

if __name__ == '__main__':
    app.run(debug=True)
