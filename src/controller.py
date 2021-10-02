#!/bin/python3

import json

def getRLineal(v_x, v_y, x_pos):
    #v_x = [2014, 2015, 2016, 2017, 2018, 2019]
    #v_y = [530, 560, 610, 690, 720, 830]
    #x_pos = 2020
    n = len(v_x)
    x, y, xy, xx = [0.0 for _ in range(4)]
    for i in range(n):
        x += v_x[i]
        y += v_y[i]
        xy += v_x[i] * v_y[i]
        xx += v_x[i] ** 2
    m = ((n * xy) - (x * y)) / ((n * xx) - x ** 2)
    b = (y - (m * x)) / n
    y_obj = (m * x_pos) + b
    return json.dumps({"status": "ok", "y_obj": y_obj});
