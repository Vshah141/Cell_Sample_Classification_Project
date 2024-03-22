import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
import scipy.optimize as opt
from sklearn import svm
from sklearn.metrics import classification_report, confusion_matrix
import itertools

def Model_Training(data): 
    feature_df = data[['Clump', 'UnifSize', 'UnifShape', 'MargAdh', 'SingEpiSize', 'BareNuc', 'BlandChrom', 'NormNucl', 'Mit']]
    X = np.asarray(feature_df)
    # X[0:5]
    data['Class'] = data['Class'].astype('int')
    y = np.asarray(data['Class'])
    # y [0:5]
    X_train, X_test, y_train, y_test = train_test_split( X, y, test_size=0.2, random_state=4)
    print ('Train set:', X_train.shape,  y_train.shape)
    print ('Test set:', X_test.shape,  y_test.shape)

    clf = svm.SVC(kernel='rbf')
    clf.fit(X_train, y_train) 
    yhat = clf.predict(X_test)
    # yhat[0:5]
    # print(X_test)
    # X_new = np.array([8,10,10,8,7,10,9,7,1]).reshape(1, -1)
    # Make prediction
    prediction = clf.predict(X_test)
    print(prediction)
    return prediction

    