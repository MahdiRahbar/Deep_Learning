from DataGenerator import DataGenerator 
import pandas as pd 
import numpy as np 


def main():
    NewDataset = DataGenerator("./dataset/comments_cleaned_1st_phase.csv","./dataset/test.csv")  # This line doesn't have a valid save_path

    NewDataset.Data_Import()
    saved_data=NewDataset.Data_cleaner()
    NewDataset.Save_Dataset(saved_data)