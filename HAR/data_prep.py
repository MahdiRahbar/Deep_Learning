#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 12:59:10 2020

@author: mahdi
"""
import pandas as pd
import numpy as np
from multiprocessing import Process, Lock
from multiprocessing.sharedctypes import Array
import multiprocessing
import time

def data_read(path):
    data = pd.read_csv(path)
    data['gt'] = pd.Categorical(data['gt'])
    data['labels'] = data['gt'].cat.codes
    return data

def data_sep(path, start_index, end_index):
    data = data_read(path)
    data = data.drop(['Index','Arrival_Time','Creation_Time','User','Model','Device'], axis=1)
    final_data = []
    for i in range(6): # number of classes
        temp = data[data['labels']==i]
        temp = np.reshape(np.array(temp[['x','y','z']]),(len(temp),3))
        final_data.append(temp[start_index:end_index])
    return final_data

class MultiProcessPreprocessor:
    """

    """
    def __init__(self):
        self.Bi_labels = [BitArray([0, 0, 0, 0, 0, 1]), BitArray([0, 0, 0, 0, 1, 0]), BitArray([0, 0, 0, 1, 0, 0]),
                     BitArray([0, 0, 1, 0, 0, 0]), BitArray([0, 1, 0, 0, 0, 0]), BitArray([1, 0, 0, 0, 0, 0])]
        self.window_size = window_size
        self.data = data
        self.x, self.y = np.empty((0, window_size, 3)), np.empty((0, len(self.Bi_labels)))

    def mp_preprocessor(self):
        print("Data set pre-processing in progress...")
        init_time = time.time()
        lock = Lock()

        for i in range(len(self.data)):
            # p = multiprocessing.Pool(processes = multiprocessing.cpu_count()-1)
            p = Process(target=self.data_prep, args=(self, i))
            p.start()
            p.join()
        self.x = np.reshape(self.x, (len(self.x), self.window_size, 3))
        self.y = np.reshape(self.y, (len(self.y), 6))
        print("Data set was preprocessed in: %.2fs" % (time.time() - init_time))
        return self.x, self.y

    def data_prep(self,i):
        for j in range(len(self.data[i]) - self.window_size - 1):
            self.x = np.vstack([self.x, np.array([self.data[i][j:(j + self.window_size), ]])])
            self.y = np.vstack([self.y, np.array([self.Bi_labels[i]])])
