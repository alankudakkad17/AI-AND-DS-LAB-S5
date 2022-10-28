import matplotlib.pyplot as plt
from scipy import stats
import pandas as pd

#from sklearn import datasets #ai support python library_ sklearn
#iris=datasets.load_iris()

df=pd.read_csv('Iris.csv')
#print(df)
X= df.loc[:, 'SepalLengthCm']
Y= df.loc[:, 'SepalWidthCm']
print(x)
slope, intercept, r, p, std_err = stats.linregress(X,Y)

def y_value(X):
    return slope * X + intercept

model = list(map(y_value, X))
plt.title("Iris Data")
plt.scatter(X, Y)
plt.plot(X, model)
plt.xlabel("sepal length in cm")
plt.ylabel("sepal width in cm")
plt.show()


v=float(input("Enter Value of Sepal length for predict the Sepal width\t"))
print("The Predicted Values=",y_value(v))
