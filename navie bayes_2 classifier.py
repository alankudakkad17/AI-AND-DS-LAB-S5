import pandas as pd
import numpy as np

df=pd.read_csv('da.csv')
w=df["Weather"]
we=list(w)
#print(we)
t=df["Temperature"]
te=list(t)
#print(te)
p=df["play"]
pl=list(p)
#print(pl)

from sklearn import preprocessing
le = preprocessing.LabelEncoder()

we_en=le.fit_transform(we)
#print("Wheather:",weather_encoded)

te_en=le.fit_transform(te)
#print("Temp:",temp_encoded)

pla=le.fit_transform(pl)
#print("Play:",label)


features=zip(we_en,te_en)
lis=list(features)

from sklearn.naive_bayes import GaussianNB
model = GaussianNB()

print("FOR PREDICTION:\n")
print("LABEL FOR WEATHER:OVERCAST-0,RAINY-1,SUNNY-2")
x=int(input("ENTER THE LABEL FOR WEATHER:"))
print("\nLABEL FOR TEMPERATURE:COOL-0,HOT-1,MILD-2")
y=int(input("ENTER THE LABEL FOR TEMPERATURE:"))

model.fit(lis,pla)
predicted= model.predict([[x,y]])
print("Prediction for Play is:",le.inverse_transform(label[predicted]))
