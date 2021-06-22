from sklearn import metrics
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import matplotlib.pyplot as pl
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans

# irisData = load_iris()
# df = pd.read_csv("Iris.csv")
# # print(df.to_string())
# x = df.iloc[:,[1,2,3,4]].values
# y = df['Species'].values
#
# x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=0)
# print(x_test)
# knn = KNeighborsClassifier(n_neighbors=7)
#
# knn.fit(x_train, y_train)
#
# print(knn.predict(x_test))
# print(metrics.accuracy_score(y_test, knn.predict(x_test)))

# df = pd.read_excel("Animal.xlsx")
# # print(df.to_string())
# x = df[['animal_height', 'animal_width', 'face_skill ']]
# y = df['animal_type']
#
# x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=0)
# knn = KNeighborsClassifier(n_neighbors=7)
#
# knn.fit(x_train, y_train)
# print(x_test)
# print(knn.predict(x_test))
# print(metrics.accuracy_score(y_test, knn.predict(x_test)))


# df = pd.read_csv("Iris.csv")
# # # print(df.to_string())
# # x = df.iloc[:, [1, 2, 3, 4]].values
# # kmean = KMeans(n_clusters=3)
# # km_p = kmean.fit_predict(x)
# # print(km_p)
# # pl.scatter(x[:, 0], x[:, 1], c=km_p, cmap="rainbow")
# # pl.show()


# df = pd.read_excel("Animal.xlsx")
# print(df.to_string())
# x = df.iloc[:, [0, 1, 2]].values
# print(x)
