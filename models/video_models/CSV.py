import pandas as pd
import os
import csv

path_train = "C:/Users/pisci/Desktop/Dataset_TRAIN/Train"
path_test = "C:/Users/pisci/Desktop/Dataset_TRAIN/Train"

df_all = pd.DataFrame()
for video in os.listdir(path_train):
    file_without_ext = video.split(".")[0]
    label_y = file_without_ext.split("_")[0]+file_without_ext.split("_")[1]+file_without_ext.split("_")[2]+file_without_ext.split("_")[3]
    print(file_without_ext)
    print(label_y)
    new_row = {"Video name": file_without_ext,
               "Label": label_y}
    df_all = pd.concat([df_all, pd.DataFrame([new_row])], ignore_index=True)

df_all.to_csv("C:/Users/pisci/Desktop/Dataset_TRAIN/CSV_FILE.csv")