import pandas as pd
import cv2
import os
import numpy as np
import dill
from sketchpy import library as lib




path_test = "C:/Users/pisci/Desktop/Dataset_TRAIN/Train"
path_train = "C:/Users/pisci/Desktop/Dataset_TRAIN/Train"

x_data = dill.load(open("D:/Programmazione/Python/Progetto_biometria/x_test_0", "rb"))

print(x_data.shape)
print(len(x_data[0]))

def create_binaries (x, y, mod):
    split = input("In quante sezioni dividere i dati ? ")
    print(len(x))

    for i in range(0, int(split)):

        # j indica il numero di file.
        j = int(len(x) / int(split))

        h = i * j
        k = j * (i + 1)

        if i == (int(split) - 1):
            print(len(x[i * j:]))
            file = open("C:/Users/pisci/Desktop/Dataset_TRAIN/Saved" + mod + "_" + str(i), "wb")
            dill.dump(x[i * j:], file)
            file.close()

        else:
            print(len(x[h:k]))
            file = open("C:/Users/pisci/Desktop/Dataset_TRAIN/Saved"
                        + mod + "_" + str(i), "wb")
            dill.dump(x[h:k], file)
            file.close()

    # Creazione del file binario per le label.
    file = open("C:/Users/pisci/Desktop/Dataset_TRAIN/Saved" + mod, "wb")
    dill.dump(y, file)
    file.close()


# -----------------------------------------------------------------------------------------------------------------------


def convert_to_array(mod):
    path = "C:/Users/pisci/Desktop/Dataset_TRAIN/Train"

    if mod == "test":
        path = path_test
    elif mod == "train":
        path = path_train
        print("PATH TRAIN:=" + path)

    array_videos = []
    df_all = pd.DataFrame()
    for (s, video) in enumerate(os.listdir(path)):
        video_array = []
        n_frame = 0

        if video != ".DS_Store":

            #for video in os.listdir(path_train):
            file_without_ext = video.split(".")[0]
            label_y = file_without_ext.split("_")[0] + file_without_ext.split("_")[1] + file_without_ext.split("_")[2] + file_without_ext.split("_")[3]
            #print(file_without_ext)
            #print(label_y)
            new_row = {"Video name": file_without_ext,
                       "Label": label_y}
            df_all = df_all.append(new_row, ignore_index=True)   #DATAFRAME DECLARATION


            cap = cv2.VideoCapture(path + "/" + video)
            while cap.isOpened():
                ret, image = cap.read()
                n_frame += 1

                if not ret or n_frame > 150:
                    break

                "Parte in cui sono eseguite le operazioni di trasformazione in bianco e nero"
                image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                # Verifica esistenza dell'immagine cv2.imwrite(os.path.join("/content/drive/MyDrive/Ricco" , 'video1.jpeg'), image)

                "Resize dell'immagine"
                image = cv2.resize(image, (50, 50), interpolation=cv2.INTER_AREA)

                "Eventuale taglio dell'immagine"
                image = image[10:-10, 0:]

                "Definizione della shape dell'array"
                #cv2.imwrite(os.path.join("D:/Programmaztione/Python/Progetto_biometria/models/video_models" , 'prova.jpeg'), image)
                #exit()
                image.shape = (30, 50, 1)
                video_array.append(image)

            video_array = np.array(video_array)


            "Creazione dell'etichetta"
            parts = video.split(".")[0].split("_")
            subject = parts[0]+parts[1]+parts[2]+parts[3]
            print ("SOGGETTO :" +subject)

    x = []
    y = []

    print("Inizio ciclo per divisione degli item e delle etichette")
    for feature, label in array_videos:
        x.append(feature)
        y.append(label)

    x = np.array(x)
    y = np.array(y)

    print("Create binaries")
    create_binaries(x, y, mod)
    df_all.to_csv("C:/Users/pisci/Desktop/Dataset_TRAIN/CSV_FILE.csv")

"Alla domanda rispondere con train o test"
modality = input("Dati per training o per test ? ")

"Il valore inserito servirà per scegliere la cartella dove sono localizzati i video"
convert_to_array(modality)
