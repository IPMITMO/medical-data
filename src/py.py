#!/usr/bin/env python
# -*- coding: utf-8 -*-
# coding=utf-8
import sys
import reader
import sys
import os

reload(sys)
sys.setdefaultencoding('utf-8')

streets = reader.read('../raw/street.xls')
areas = reader.read('../raw/area.xls')
id_exitus = reader.read('../raw/id_exitus.xls')
id_prvs = reader.read('../raw/id_prvs.xls')
main = reader.readmain('../raw/main.xls')



def deleteContent(fName):
    with open(fName, "w"):
        pass

deleteContent('bump')

f = open('bump', 'w')

for i in range(1, 3):
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

os.system( 'tail bump')
