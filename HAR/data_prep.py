#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 12:59:10 2020

@author: mahdi
"""
import pandas as pd
import numpy as np
import time

global START_INDEX, END_INDEX

START_INDEX = 0
END_INDEX = 1000

class DataReader:
    """

    """

    def __init__(self, path): # , start_index = 0 , end_index = 10000
        self.path = path
        # self.start_index = start_index
        # self.end_index = end_index
        self.data = []

    def data_read(self):
        self.data = pd.read_csv(self.path)
        self.data['gt'] = pd.Categorical(self.data['gt'])
        self.data['labels'] = self.data['gt'].cat.codes
        return self.data

    def data_sep(self):

        '''
        calls data_read inside itself
        :return: self.data
        '''
        self.data_read()
        self.data = self.data.drop(['Index', 'Arrival_Time', 'Creation_Time', 'User', 'Model', 'Device'], axis=1)
        final_data = []
        for i in range(6):  # number of classes
            temp = self.data[self.data['labels'] == i]
            temp = np.reshape(np.array(temp[['x', 'y', 'z']]), (len(temp), 3))
            final_data.append(temp[START_INDEX:END_INDEX])
        self.data = final_data
        return self.data



