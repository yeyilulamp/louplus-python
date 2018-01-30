#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import sys
from collections import namedtuple

Tax_items = namedtuple(
'Tax_items',
['start','tar_rate','quick']
)

START_POINT = 3500

LOOKUP_TABLE = [
    Tax_items(80000,0.45,13505),
    Tax_items(55000, 0.35, 5505),
    Tax_items(35000, 0.30, 2755),
    Tax_items(9000, 0.25, 1005),
    Tax_items(4500, 0.2, 555),
    Tax_items(1500, 0.1, 105),
    Tax_items(0, 0.03, 0)
]

MONEY_TABLE = dict(
    pension=0.08,
    medial=0.02,
    unemployment=0.005,
    employee=0,
    maternity=0,
    public=0.06
)


def calc(values):
    result = values * sum(MONEY_TABLE.values())
    v = values - result
    value = v - START_POINT
    if value <= 0:
        return '0.00','{:.2f}'.format(v)
    
    for item in LOOKUP_TABLE:
        if value > item.start:
            tax = value * item.tar_rate - item.quick
       	    return '{:.2f}'.format(tax),'{:.2f}'.format(v-tax)

def main():
    for item in sys.argv[1:]:
        employee_id,value_str = item.split(':')
        try:
            values = int(value_str)
        except ValueError:
            print('Parameter Error')
        _,y = calc(values)
        print('{}:{}'.format(employee_id,y))

if __name__ == '__main__':
    main()
