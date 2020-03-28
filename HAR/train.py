#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 13:21:20 2020

@author: mahdi
"""

from keras.layers import LSTM, Input, Dense
from keras.models import Model
from keras.utils import to_categorical
from keras import optimizers

from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split as split

from bitstring import BitArray
from MultiProcessPreprocessor import MultiProcessPreprocessor
import time
from settings import *





def train_model(best_window_size, best_num_units):
    # Decode GA solution to integer for window_size and num_units

    train_data = DATA
    split_point = SPLIT_POINT

    window_size = best_window_size
    num_units = best_num_units

    #     window_size =  200
    #     num_units = 150

    print('\nWindow Size: ', window_size, ', Num of Units: ', num_units)

    # Return fitness score of 100 if window_size or num_unit is zero
    if window_size == 0 or num_units == 0:
        return 100,

    print("DEBUG: The data size is : ", len(train_data[0]))
    mp_prep = MultiProcessPreprocessor(train_data, window_size)
    X,Y = mp_prep.mp_preprocessor()
    del mp_prep
    # X,Y = prepare_dataset(train_data,window_size)
    print("DEBUG: The X size is : ", len(X))

    X_train, X_val, y_train, y_val = split(X, Y, test_size = 0.20, random_state = 1120)

    inputs = Input(shape=(window_size, 3))
    x = LSTM(num_units, input_shape=(window_size, 3))(inputs)
    ##
    x = Dense(50, activation='relu')(x)
    ##
    predictions = Dense(6, activation='softmax')(x)
    opt = optimizers.SGD(lr=0.01, momentum=0.9)
    model = Model(inputs=inputs, outputs=predictions)
    model.compile(optimizer=opt, loss='categorical_crossentropy', metrics=['accuracy'])
    model.fit(X_train, y_train, epochs=3, batch_size=20, shuffle=True)

    _, train_acc = model.evaluate(X_train, y_train, verbose=0)
    _, test_acc = model.evaluate(X_val, y_val, verbose=0)
    print('Train: %.3f, Test: %.3f' % (train_acc, test_acc))

    return model, test_acc
