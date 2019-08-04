__author__ = "Jieshu Wang and Bilal El Uneis"
__since__ = "Aug 2019"
__email__ = "foundwonder@gmail.com and bilaleluneis@gmail.com"

from flask import Blueprint, render_template, redirect, request, url_for
from data_structure.stacks.stack_object import Stack
from data_structure.arrays.list_impl import ArrayListImpl
from data_structure.arrays.node_impl import ArrayNodeImpl
import logging as log

stacks: Blueprint = Blueprint("stacks", __name__, template_folder="templates")
log.basicConfig(level=log.INFO)

stacks_render_template_dic = {"stack_list_impl": Stack(ArrayListImpl()),
                              "stack_node_impl": Stack(ArrayNodeImpl())}


@stacks.route("/stacks", methods=["GET"])
def get_stacks():
    return render_template("stacks.html", **stacks_render_template_dic)


@stacks.route("/stacks", methods=["POST"])
def post_stack():
    if request.form.get("push_to_stack") is not None:
        return push_to_stack()
    elif request.form.get("pop_from_stack") is not None:
        return pop_from_stack()


def push_to_stack():
    value_to_push: int = int(request.form['push_value'])
    global stacks_render_template_dic
    stacks_render_template_dic["stack_list_impl"].push(value_to_push)
    return redirect(url_for(".get_stacks"))


def pop_from_stack():
    global stacks_render_template_dic
    stacks_render_template_dic["stack_list_impl"].pop()
    return redirect(url_for(".get_stacks"))
