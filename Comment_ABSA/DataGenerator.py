# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 12:26:07 2020

@author: Mahdi Rahbar
"""

import pandas as pd

class DataGenerator:

    def __init__(self, data_path, save_path):
        self.data_path = data_path
        self.save_path = save_path
    
    def Data_Import(self):
        data = pd.read_csv(self.data_path)
        return data 
    
    def Comment_Cleaner(self):
        pass
    
    def Adv_Disadv(self):
        pass

    def PoS_Extractor(self):
        pass