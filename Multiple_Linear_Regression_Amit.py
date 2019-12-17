#Simple Linear Regression

#Data Preprocessing#
#Importing the libraries

import numpy as np #for importing mathematical operations
import matplotlib.pyplot as plt #for importing plots and figures
import pandas as pd #for importing files 

#Importing the dataset
dataset=pd.read_csv('Salary_Data.csv')
x = dataset.iloc[:,:-1].values #
y = dataset.iloc[:,1].values

#Splitting data into Training Data and Test Data
from sklearn.model_selection import train_test_split 
x_train, x_test, y_train, y_test=train_test_split(x,y,test_size=1/3,random_state=0)

#Feature_Scalinng
"""from sklearn.preprocessing import StandardScaler
sc_x=StandardScaler()
x_train=sc_x.fit_transform(x_train)
x_test=sc_x.transform(x_test)"""


