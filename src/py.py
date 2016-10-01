#!/usr/bin/env python
# -*- coding: utf-8 -*-

import reader

streets = reader.read('../raw/street.xls')
areas = reader.read('../raw/area.xls')
diagnosis = reader.read('../raw/id_exitus.xls')
privs = reader.read('../raw/id_prvs.xls')
main = reader.readmain('../raw/main.xls')

for i in range(1, 5):
    obj = main[i]
    # print obj['birthday'], obj['street'], obj['area']
    print obj['id'], areas.get(obj['area']), obj['birthday']

# print area_map.get(u'ФР')
