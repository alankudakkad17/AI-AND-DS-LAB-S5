import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn import datasets#ai support python library_ sklearn
# Importing the dataset
iris=datasets.load_iris()
al=[]
X=iris.data
y=iris.target
print(y)
# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.8, random_state = 0)
# Feature Scaling
#from sklearn.preprocessing import StandardScaler
#sc = StandardScaler()
#X_train = sc.fit_transform(X_train)
#X_test = sc.transform(X_test)
# Training the Naive Bayes model on the Training set
from sklearn.naive_bayes import GaussianNB
classifier = GaussianNB()
classifier.fit(X_train, y_train)
# Predicting the Test set results
y_pred = classifier.predict(X_test)
# Making the Confusion Matrix,and finding the accuracy,precision,recall
from sklearn.metrics import confusion_matrix, accuracy_score
ac = accuracy_score(y_test,y_pred)
cm = confusion_matrix(y_test, y_pred)
print("Accuracy:",ac)
print("Confusion matrix:")
print(cm)
precision = precision_score(y_test, y_pred, average='macro')
print('Precision: %.3f' % precision)
recall = recall_score(y_test, y_pred, average='macro')
print('Recall: %.3f' % recall)
print("FOR PREDICTION:\n")
al.append(float(input("Enter the sepal lenght:")))
al.append(float(input("Enter the width lenght:")))
al.append(float(input("Enter the petal lenght:")))
al.append(float(input("Enter the width lenght:")))
AL=[al]
y1_pred = classifier.predict(arr)
print(y1_pred)
if y1_pred[0]== 0:
    print("setosa")
elif y1_pred[0]==1:
    print('versicolor')
else:
    print('virginica')
