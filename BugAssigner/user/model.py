import nltk
import string
import pandas as pd
import numpy as np
import tensorflow as tf
from keras.models import Model, load_model

nltk.download('punkt')

def predict_result(request_data):
    rankK = 10
    print('Predict function loaded....')
    description = request_data
    #tokenize 
    data = nltk.word_tokenize(description)

    clean_data = []
    for item in data:
        #Change to lower case
        desc = item.lower()

        #remove trailing punctuation
        stripped_desc = desc.strip(string.punctuation)

        #remove whitespaces
        stripped_desc = stripped_desc.strip()

        #filter and append to new list
        clean_data.append(stripped_desc)
        clean_data = list(filter(None, clean_data))

    unit = np.array(clean_data)
    X_test = np.empty(shape=[len(unit), 30,200], dtype='float32')
    print('X_test fully loaded...')
    model = load_model('/home/clinton/Desktop/FinalProject/BugAssigner/prediction_api/dbbrna3.h5')
    print('Model loaded')
    predict = model.predict(X_test)
    sortedIndices = []
    pred_classes = []
    labels = pd.read_csv('/home/clinton/Desktop/FinalProject/BugAssigner/prediction_api/labels.csv')
    classes = np.array(labels)
    for ll in predict:
        sortedIndices.append(sorted(range(len(ll)), key=lambda ii: ll[ii], reverse=True))
    for k in range(1, rankK+1):
        for sortedInd in sortedIndices:
            pred_classes.append(classes[sortedInd[:k]])

    array1_length = len(pred_classes)
    useremail_array = pred_classes[0:1]
    user = useremail_array[0]
    result = user[0][0]
    return result


