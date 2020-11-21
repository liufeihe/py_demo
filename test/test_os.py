#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os

def get_project_path():
    root =  os.getenv('BOIL_CTRL_ROOT')
    print(root)

if __name__ == "__main__":
    get_project_path()