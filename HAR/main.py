#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 12:59:10 2020

@author: mahdi
"""
from . import EA
from . import data_prep
from . import model

PATH = "./Activity Recognition Dataset/Watch_gyroscope.csv"
START_INDEX = 0
END_INDEX = 10000

POP_SIZE = 10  # Too big
GEN_NUM = 15  # Takes for ever to run
GENE_LEN = 16


def main():
    reader = DataReader(PATH, START_INDEX, END_INDEX)
    data = reader.data_sep()

    preprocessor = MultiProcessPreprocessor(data, windows )