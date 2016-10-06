#!/usr/bin/env python
# -*- coding: utf-8 -*-
# coding=utf-8

import sys
import reader
import sys
import os

reload(sys)
sys.setdefaultencoding('utf-8')
dir = os.path.dirname(__file__)

streets = reader.read(os.path.join(dir, '../raw/street.xls'))
areas = reader.read(os.path.join(dir, '../raw/area.xls'))
id_exitus = reader.read(os.path.join(dir, '../raw/id_exitus.xls'))
id_prvs = reader.read(os.path.join(dir, '../raw/id_prvs.xls'))
main = reader.readmain(os.path.join(dir, '../raw/main.xls'))

OUT_FILE = os.path.join(dir, '../out/bump.csv')

f = open(OUT_FILE, 'w')

for i in range(1, len(main)):
    obj = main[i]
    s = "{0}; {1}; {3}; {4}; {5}; {6}; {7}; \n".format(
        obj['id'],
        areas.get(obj['area']),
        streets.get(obj['street']),
        id_exitus.get(obj['id_exitus']),
        obj['birthday'],
        obj['diagnosis'],
        obj['dateout'],
        id_prvs.get(str(int(obj['id_prvs']))))
    f.write(s)
