from flask import Flask, render_template, request, redirect, url_for
from data_structure.arrays.list_impl import ArrayListImpl, ArrayIndexOutOfBoundError, Optional
from data_structure.arrays.node_impl import ArrayNodeImpl
import logging as log
from random import randint
from data_structure.stacks.stack_object import Stack

app = Flask(__name__)

log.basicConfig(level=log.INFO)

arrays_render_template_dic = {"array": ArrayListImpl(),
                              "random_array": ArrayListImpl()}

stacks_render_template_dic = {"stack_list_impl": Stack(ArrayListImpl()),
                              "stack_node_impl": Stack(ArrayNodeImpl())}


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
        global arrays_render_template_dic
        arrays_render_template_dic["array"].insert(value_to_insert, index_to_insert)
        return redirect(url_for("get_arrays"))
    except ArrayIndexOutOfBoundError as insertError:
        log.error(insertError)
        return render_template("arrays.html", array=arrays_render_template_dic["array"], error=str(insertError))


def gen_random():
    global arrays_render_template_dic
    arrays_render_template_dic["random_array"] = ArrayListImpl()
    size_to_generate: int = int(request.form['input_size'])
    for i in range(size_to_generate):
        int_to_insert: int = randint(0, 100)
        arrays_render_template_dic["random_array"].insert(int_to_insert)
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
    global stacks_render_template_dic
    stacks_render_template_dic["stack_list_impl"].push(value_to_push)
    return redirect(url_for("get_stacks"))


def pop_from_stack():
    global stacks_render_template_dic
    stacks_render_template_dic["stack_list_impl"].pop()
    return redirect(url_for("get_stacks"))


if __name__ == '__main__':
    app.run(debug=True)
