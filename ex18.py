#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 15:11:09 2018

@author: howardhsu
"""

#ex 18
# this one is like your scripts with argv
# "*args" means that get the all inputs of args
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")
# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")
# this just takes one argument
def print_one(arg1):
    print(f"arg1: {arg1}")
# this one takes no arguments
def print_none():
    print("I got nothin'.")
print_two("Zed","Shaw")
print_two_again("Zed","Shaw")
print_one("First!")
print_none()
