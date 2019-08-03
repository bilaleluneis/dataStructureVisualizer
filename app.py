from flask import Flask, render_template, request, redirect, url_for
from data_structure.arrays.list_impl import ArrayListImpl, ArrayIndexOutOfBoundError, Optional
from data_structure.arrays.node_impl import ArrayNodeImpl
import logging as log
from random import randint
from data_structure.stacks.stack_object import Stack

app = Flask(__name__)

log.basicConfig(level=log.INFO)
# simulate data storage that can retain values between requests
__saved_array: ArrayListImpl = ArrayListImpl()
__random_array: ArrayListImpl = ArrayListImpl()
__saved_stack_list_impl: Stack = Stack(ArrayListImpl())
__saved_stack_node_impl: Stack = Stack(ArrayNodeImpl())

arrays_render_template_dic = {"array": __saved_array,
                              "random_array": __random_array}

stacks_render_template_dic = {"stack_list_impl": __saved_stack_list_impl,
                              "stack_node_impl": __saved_stack_node_impl}

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
    return render_template("arrays.html", **arrays_render_template_dic)


@app.route("/arrays", methods=["POST"])
def post_arrays():
    if request.form.get("update_list") is not None:
        return update_list()
    elif request.form.get("gen_random_list") is not None:
        return gen_random()


def update_list():
    value_to_insert: int = int(request.form['input_value'])
    index_to_insert: Optional[int]
    if len(request.form.get('input_index')) == 0:
        index_to_insert = None
    else:
        index_to_insert = int(request.form['input_index'])

    try:
        __saved_array.insert(value_to_insert, index_to_insert)
        return redirect(url_for("get_arrays"))
    except ArrayIndexOutOfBoundError as insertError:
        log.error(insertError)
        return render_template("arrays.html", array=__saved_array, error=str(insertError))


def gen_random():
    global __random_array
    __random_array = ArrayListImpl()
    size_to_generate: int = int(request.form['input_size'])
    for i in range(size_to_generate):
        int_to_insert: int = randint(0, 100)
        __random_array.insert(int_to_insert)
    return redirect(url_for("get_arrays"))


@app.route("/stacks", methods=["GET"])
def get_stacks():
    return render_template("stacks.html", **stacks_render_template_dic)


@app.route("/stacks", methods=["POST"])
def post_stack():
    if request.form.get("push_to_stack") is not None:
        return push_to_stack()
    elif request.form.get("pop_from_stack") is not None:
        return pop_from_stack()


def push_to_stack():
    value_to_push: int = int(request.form['push_value'])
    __saved_stack_list_impl.push(value_to_push)
    return redirect(url_for("get_stacks"))


def pop_from_stack():
    __saved_stack_list_impl.pop()
    return redirect(url_for("get_stacks"))


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
