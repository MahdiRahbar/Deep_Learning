from DataGenerator import DataGenerator 
import pandas as pd 
import numpy as np 
import time

def main():
    NewDataset = DataGenerator("./dataset/comments_cleaned_1st_phase.csv","./dataset/digi_cleaned_phase2_3000_4000.csv")  # This line doesn't have a valid save_path
    start_time = time.time()
    NewDataset.Data_Import()
    NewDataset.Data_cleaner()
    NewDataset.Save_Dataset()
    print("============================")
    print("Finished in %.2f s"%(time.time()-start_time))
