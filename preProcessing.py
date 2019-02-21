import pandas as pd
import numpy as np
from sklearn import preprocessing

min_max_scaler = preprocessing.MinMaxScaler()
dataS1 = pd.read_csv("data/adult.data",sep=',',header = None)
dataS1.columns = ['Age','WorkClass','Fnlwgt','Education','Education_num','Marital_status','occupation','Relationship','Race','Sex','Capital-gain','Capital-loss','Hours-per-week','native-country','Income']

s1_xaux = dataS1[dataS1.columns[0:11]].copy()
s1_yaux = dataS1[['Income']].copy()

s1_yaux = pd.get_dummies(s1_yaux, columns=['Income'])
s1_y = s1_yaux[s1_yaux.columns[1]]

s1_xaux['WorkClass'] = s1_xaux['WorkClass'].astype('category')
s1_xaux['Marital_status'] = s1_xaux['Marital_status'].astype('category')
s1_xaux['occupation'] = s1_xaux['occupation'].astype('category')
s1_xaux['Relationship'] = s1_xaux['Relationship'].astype('category')
s1_xaux['Race'] = s1_xaux['Race'].astype('category')
s1_xaux['Sex'] = s1_xaux['Sex'].astype('category')
s1_xaux['WorkClass_cat'] = s1_xaux['WorkClass'].cat.codes
s1_xaux['Marital_status_cat'] = s1_xaux['Marital_status'].cat.codes
s1_xaux['occupation_cat'] = s1_xaux['occupation'].cat.codes
s1_xaux['Relationship_cat'] = s1_xaux['Relationship'].cat.codes
s1_xaux['Race_cat'] = s1_xaux['Race'].cat.codes
s1_xaux['Sex_cat'] = s1_xaux['Sex'].cat.codes

s1_x = s1_xaux.drop(columns=['WorkClass','occupation','Relationship','Race','Sex','Education','Marital_status'])

s1_x['occupation_cat'] = s1_x['occupation_cat'].replace([0],round(s1_x['occupation_cat'].mean()))
s1_x['WorkClass_cat'] = s1_x['WorkClass_cat'].replace([0],round(s1_x['WorkClass_cat'].mean()))
s1_x['Fnlwgt'] = min_max_scaler.fit_transform(pd.DataFrame(s1_x[['Fnlwgt']].values.astype(float)))

#print(dataS1)
print(s1_x)
