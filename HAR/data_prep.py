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

def Data_Read(path):
    data = pd.read_csv(path)
    data['gt'] = pd.Categorical(data['gt'])
    data['labels'] = data['gt'].cat.codes
    return data

def Data_Sep(path, start_index, end_index):
    data = Data_Read(path)
    data = data.drop(['Index','Arrival_Time','Creation_Time','User','Model','Device'], axis=1)
    d0 = data[data['labels']==0]
    d1 = data[data['labels']==1]
    d2 = data[data['labels']==2]
    d3 = data[data['labels']==3]
    d4 = data[data['labels']==4]
    d5 = data[data['labels']==5]
    #####============================
    d0_arr = np.reshape(np.array(d0[['x','y','z']]),(len(d0),3))
    # ====================================================================================================
    d1_arr = np.reshape(np.array(d1[['x','y','z']]),(len(d1),3))
    # ====================================================================================================
    d2_arr = np.reshape(np.array(d2[['x','y','z']]),(len(d2),3))
    # ====================================================================================================
    d3_arr = np.reshape(np.array(d3[['x','y','z']]),(len(d3),3))
    # ====================================================================================================
    d4_arr = np.reshape(np.array(d4[['x','y','z']]),(len(d4),3))
    # ====================================================================================================
    d5_arr = np.reshape(np.array(d5[['x','y','z']]),(len(d5),3))
    #####============================
    train_data = [d0_arr[start_index:end_index],d1_arr[start_index:end_index],d2_arr[start_index:end_index],
                  d3_arr[start_index:end_index],d4_arr[start_index:end_index],d5_arr[start_index:end_index]]
    return train_data


def MP_Preprocessor(data, window_size):
    Bi_labels = [BitArray([0, 0, 0, 0, 0, 1]), BitArray([0, 0, 0, 0, 1, 0]), BitArray([0, 0, 0, 1, 0, 0]),
                 BitArray([0, 0, 1, 0, 0, 0]), \
                 BitArray([0, 1, 0, 0, 0, 0]), BitArray([1, 0, 0, 0, 0, 0])]
    print("Dataset preprocessing in progress...")
    init_time = time.time()
    lock = Lock()
    #     array = Array('i', 10000, lock=lock)
    X, Y = np.empty((0, window_size, 3)), np.empty((0, 6))

    for i in range(len(data)):
        #         p = multiprocessing.Pool(processes = multiprocessing.cpu_count()-1)
        p = Process(target=data_prep, args=(i, data, X, Y, Bi_labels))
        p.start()
        p.join()
    X = np.reshape(X, (len(X), window_size, 3))
    Y = np.reshape(Y, (len(Y), 6))
    print("Dataset was preprocessed in: %.2fs" % (time.time() - init_time))
    return X, Y