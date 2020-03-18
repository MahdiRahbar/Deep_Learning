#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 12:59:10 2020

@author: mahdi
"""
from EA import *
# from data_prep import DataReader
from settings import *

# init()



print("SUCCESS!!!")

def main():

    # pass
    ea = EA(POP_SIZE, GEN_NUM, GENE_LEN)
    ea.evo_algorithm()
