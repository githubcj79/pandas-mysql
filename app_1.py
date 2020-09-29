#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd

CELLS_DATA = './data/20200920.json' # <-- It's not a valid json (mysql workbench)
CELLS_DATA = "https://raw.githubusercontent.com/domoritz/maps/master/data/iris.json" # it works

def main():
    cells_data = pd.read_json(CELLS_DATA)
    print(f'type(cells_data)={type(cells_data)}')


if __name__ == '__main__':
    main()
