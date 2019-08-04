__author__ = "Jieshu Wang and Bilal El Uneis"
__since__ = "Aug 2019"
__email__ = "foundwonder@gmail.com and bilaleluneis@gmail.com"

from flask import Blueprint, render_template, redirect, request, url_for
from data_structure.arrays.abstract import AbstractArray
from data_structure.arrays.list_impl import ArrayListImpl, ArrayIndexOutOfBoundError
from typing import Optional
import logging as log
from random import randint

arrays: Blueprint = Blueprint("arrays", __name__, template_folder="templates")
log.basicConfig(level=log.INFO)
arrays_render_template_dic: {str: AbstractArray} = {"array": ArrayListImpl(),
                                                    "random_array": ArrayListImpl()}


@arrays.route("/arrays", methods=["GET"])
def get_arrays():
    return render_template("arrays.html", **arrays_render_template_dic)


@arrays.route("/arrays", methods=["POST"])
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
        return redirect(url_for(".get_arrays"))
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
    return redirect(url_for(".get_arrays"))
