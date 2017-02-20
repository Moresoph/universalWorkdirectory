#!/usr/bin/python
# coding=UTF-8
import sys
def get_cur_info():
        print(sys._getframe().f_code.co_filename) # the file name 
        print(sys._getframe().f_code.co_name)     # the function name
        print(sys._getframe().f_lineno)           # the line of the current sentence
get_cur_info()
