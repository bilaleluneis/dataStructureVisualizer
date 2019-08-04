from flask import Flask
import logging as log
from blueprint.arrays import arrays
from blueprint.stacks import stacks

app = Flask(__name__)
app.register_blueprint(arrays)
app.register_blueprint(stacks)

log.basicConfig(level=log.INFO)


if __name__ == '__main__':
    app.run(debug=True)
