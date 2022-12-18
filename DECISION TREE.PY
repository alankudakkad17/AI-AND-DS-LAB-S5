from sklearn.datasets import load_breast_cancer
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
dat= load_breast_cancer()
X=dat.data
y=dat.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size =0.9,random_state = 1)
DTclf=tree.DecisionTreeClassifier()
DTclf=DTclf.fit(X_train,y_train)
y_pred = DTclf.predict(X_test)
tree.plot_tree(DTclf)
a = accuracy_score(y_test,y_pred)*100
print("Accuracy=",a)
