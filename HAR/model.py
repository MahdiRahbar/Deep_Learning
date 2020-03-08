#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 12:59:10 2020

@author: mahdi
"""
from keras.layers import LSTM, Input, Dense
from keras.models import Model
from keras.utils import to_categorical
from keras import optimizers

def model_test(window_size, num_units):
    # Decode GA solution to integer for window_size and num_units
    window_size_bits = BitArray(ga_individual_solution[0:8])
    num_units_bits = BitArray(ga_individual_solution[8:])
    window_size = window_size_bits.uint
    num_units = num_units_bits.uint

    #     window_size =  200
    #     num_units = 150

    print('\nWindow Size: ', window_size, ', Num of Units: ', num_units)

    # Return fitness score of 100 if window_size or num_unit is zero
    #     if window_size == 0 or num_units == 0:
    #         return 100,

    X,Y = prepare_dataset(train_data,window_size)
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
    model.fit(X_trainـMT, y_trainـMT, epochs=5, batch_size=10, shuffle=True)

    _, train_acc = model.evaluate(X_train, y_train, verbose=0)
    _, test_acc = model.evaluate(X_val, y_val, verbose=0)
    print('Train: %.3f, Test: %.3f' % (train_acc, test_acc))

    return test_acc,