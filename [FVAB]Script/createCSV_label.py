import pandas as pd
import os
import csv

path_train = "C:\\Users\\user\\PycharmProjects\\pythonProject\\Train"
path_test = "C:\\Users\\user\\PycharmProjects\\pythonProject\\Test"

df_all = pd.DataFrame()
for video in os.listdir(path_train):
    file_without_ext = video.split(".")[0]
    label_y = file_without_ext.split("_")[0]+file_without_ext.split("_")[1]+file_without_ext.split("_")[2]+file_without_ext.split("_")[3]
    print(file_without_ext)
    print(label_y)
    new_row = {"Video name": file_without_ext,
               "Label": label_y}
    df_all = df_all.append(new_row, ignore_index=True)

df_all.to_csv("C:\\Users\\user\\PycharmProjects\\pythonProject\\(FVAB)train.csv")

