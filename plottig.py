import matplotlib.pyplot as plt
import seaborn as sns
x=[1,2,3,4]
y=[20,30,22,50]
z=sns.stripplot(x,y);
z.set(xlabel="Roll no",ylabel="Marks")
plt.figure()
plt.plot(x,y)
plt.show()
plt.bar(x,y)
plt.show()
plt.stem(x,y)
plt.show()

import pandas as pd
df=pd.read_csv('csvFile.csv')
print(df)
h=df.sort_values(["Gender"],ascending=[True])
print("\t\nSorted csv file\n",h)
