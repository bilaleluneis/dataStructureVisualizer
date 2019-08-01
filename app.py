from flask import Flask, render_template, request, redirect, url_for
from arrays.list_impl import ArrayListImpl, ArrayIndexOutOfBoundError
import logging as log

app = Flask(__name__)

log.basicConfig(level=log.INFO)
# simulate data storage that can retain values between requests
__saved_array: ArrayListImpl = ArrayListImpl()

""" 
@app.route('/arrays')
def load_arrays():
    array: ArrayListImpl = ArrayListImpl()
    for i in range(10):
        array.insert(i)

    return render_template("arrays.html", example_array=array)
"""


@app.route("/arrays", methods=["GET"])
def get_arrays():
    return render_template("arrays.html", array=__saved_array)


@app.route("/arrays", methods=["POST"])
def post_arrays():
    value_to_insert: int = request.form['input_value']
    try:
        __saved_array.insert(value_to_insert)
        return redirect(url_for("get_arrays"))
    except ArrayIndexOutOfBoundError as insertError:
        log.error(insertError)
        return render_template("arrays.html", array=__saved_array, error=str(insertError))


"""
@app.route('/stacks')
def load_stack():
    return "stacks will go here"


@app.route('/')
def root():
    return "root application"
"""

if __name__ == '__main__':
    app.run(debug=True)
