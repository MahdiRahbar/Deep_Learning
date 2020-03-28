#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 12:36:47 2020

@author: mahdi
"""
from data_prep import *

# # PATH = "./Activity Recognition Dataset/Watch_gyroscope.csv"
global PATH, POP_SIZE, GEN_NUM,GENE_LEN, WIN_SIZE_GEN_NUM, SPLIT_POINT, DATA



POP_SIZE = 5  # Too big
GEN_NUM = 50  # Takes for ever to run
GENE_LEN = 14
WIN_SIZE_GEN_NUM = 8
SPLIT_POINT = 8

GEN_COUNTER = 0

PATH = "./Dataset/Watch_gyroscope.csv"

reader = DataReader(PATH)  # , START_INDEX, END_INDEX
DATA = reader.data_sep()

# def init():
#     global PATH, START_INDEX, END_INDEX, POP_SIZE, GEN_NUM, \
#             GENE_LEN, WIN_SIZE_GEN_NUM, SPLIT_POINT, DATA
#
#     DATA = DATA
#     START_INDEX = 0
#     END_INDEX = 10000
#
#     POP_SIZE = 10  # Too big
#     GEN_NUM = 15  # Takes for ever to run
#     GENE_LEN = 14
#     WIN_SIZE_GEN_NUM = 8
#     SPLIT_POINT = 8
