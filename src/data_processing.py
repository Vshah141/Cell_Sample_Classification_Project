import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def Data_loading(path):
    df = pd.read_csv(path)
    return df

def Data_Analysis(df):
    print(df.head(10))
    # ID:Clump thickness
    # Clump: Clump thickness(mm)
    # Unif Size: 	Uniformity of cell size
    # UnifShape:	Uniformity of cell shape
    # MargAdh:	Marginal adhesion
    # SingEpiSize:	Single epithelial cell size(micrometer)
    # BareNuc:	Bare nuclei
    # BlandChrom:	Bland chromatin
    # NormNucl:	Normal nucleoli
    # Mit:	Mitoses
    # Class:	Benign or malignant
    print(df.columns)
    l = []
    for x in range(0,699):
        if df['BareNuc'].loc[x] == '?':
            l.append(x)
        
    
    print(l)
    df_new = df.drop(l)
    df_new = df_new.reset_index(drop=True, inplace=True)
    print(df_new.shape)
    print(df_new.info())
    print(df_new.describe())
    return df_new

def Data_Visialisation(df_new):
    ax = df_new[df_new['Class'] == 4][0:150].plot(kind='scatter', x='Clump', y='UnifSize', color='DarkBlue', label='malignant');
    df_new[df_new['Class'] == 2][0:150].plot(kind='scatter', x='Clump', y='UnifSize', color='Yellow', label='benign', ax=ax);
    plt.show()
    feature_df = df_new[['Clump', 'UnifSize', 'UnifShape', 'MargAdh', 'SingEpiSize', 'BareNuc', 'BlandChrom', 'NormNucl', 'Mit']]
    X = np.asarray(feature_df)
    print(X[0:5])
    df_new['Class'] = df_new['Class'].astype('int')
    y = np.asarray(df_new['Class'])
    print(y [0:5])
    return feature_df




    





    

