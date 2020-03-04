#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 12:59:10 2020

@author: mahdi
"""
import pandas as pd
import numpy as np

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