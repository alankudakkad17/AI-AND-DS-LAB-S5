import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
#import the breast _cancer dataset
from sklearn.datasets import load_breast_cancer
data=load_breast_cancer()
data.keys()
# Check the output classes
print(data['target_names'])
# Check the input attributes
print(data['feature_names'])
# construct a dataframe using pandas
df1=pd.DataFrame(data['data'],columns=data['feature_names'])
# Scale data before applying PCA
scaling=StandardScaler()
# Use fit and transform method
scaling.fit(df1)
Scaled_data=scaling.transform(df1)
# Set the n_components=3
principal=PCA(n_components=2)
principal.fit(Scaled_data)
x=principal.transform(Scaled_data)
print(x)
# Check the dimensions of data after PCA
print(x.shape)
plt.figure(figsize=(10,10))
plt.scatter(x[:,0],x[:,1],c=data['target'],cmap='plasma')
plt.xlabel('pc1')
plt.ylabel('pc2')
