#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 13:17:35 2020

@author: mahdi
"""
import numpy as np
from multiprocessing import Process, Lock, Manager
from multiprocessing.sharedctypes import Array
import multiprocessing
from settings import *
from bitstring import BitArray


class MultiProcessPreprocessor:

    def __init__(self, data, window_size ):
        self.data = data
        self.Bi_labels = [BitArray([0, 0, 0, 0, 0, 1]), BitArray([0, 0, 0, 0, 1, 0]), BitArray([0, 0, 0, 1, 0, 0]),
                     BitArray([0, 0, 1, 0, 0, 0]), BitArray([0, 1, 0, 0, 0, 0]), BitArray([1, 0, 0, 0, 0, 0])]
        self.window_size = window_size
        self.x = []
        self.y = []
        # self.x, self.y = np.empty((0, self.window_size, 3)), np.empty((0, len(self.Bi_labels)))
        manager = multiprocessing.Manager()
        self.Z = manager.list()

    def mp_preprocessor(self):
        '''
        calls data_prep & data_sep functions inside itself
        :return:
        '''

        print("Data set pre-processing in progress...")
        init_time = time.time()

        # for i in range(len(self.data)):
        #     p = Process(target=self.data_prep, args=(i, self.data, self.x,self.y,self.Bi_labels))
        #     p.start()
        #     p.join()
        p1 = Process(target=self.data_prep, args=(0, self.data[0], self.Bi_labels,))
        p2 = Process(target=self.data_prep, args=(1, self.data[1], self.Bi_labels,))
        p3 = Process(target=self.data_prep, args=(2, self.data[2], self.Bi_labels,))
        p4 = Process(target=self.data_prep, args=(3, self.data[3], self.Bi_labels,))
        p5 = Process(target=self.data_prep, args=(4, self.data[4], self.Bi_labels,))
        p6 = Process(target=self.data_prep, args=(5, self.data[5], self.Bi_labels,))
        p1.start()
        p2.start()
        p3.start()
        p4.start()
        p5.start()
        p6.start()

        p1.join()
        p2.join()
        p3.join()
        p4.join()
        p5.join()
        p6.join()

        self.x, self.y = zip(*list(self.Z))
        self.x = np.array(self.x)
        self.y = np.array(self.y)
        self.x = np.reshape(self.x, (len(self.x),self.window_size,3))
        self.y = np.reshape(self.y, (len(self.y), 6))
        print("Data set was preprocessed in: %.2fs" % (time.time() - init_time))
        return self.x, self.y

    def data_prep(self,i, data,  Bi_labels):
        for j in range(len(data) - self.window_size - 1):
            self.Z.append([np.array([data[j:(j + self.window_size),]]),np.array([Bi_labels[i]])])
