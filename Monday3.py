from tabulate import tabulate
from sklearn import datasets, svm
from sklearn.model_selection import train_test_split, cross_val_score
import pandas as pd
from sklearn import preprocessing
import numpy as np

data = datasets.load_iris()
# print(type(data))
# x = data.data
# y = data.target
# print(x.shape, y.shape)
# x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.5)
# print(x_train.shape, x_test.shape)
# print(y_train.shape, y_test.shape)
# print(tabulate(data.data[:5],headers=data.feature_names))
# print("x_train",x_train[:5])
# print("x_test",x_test[:5])
# print(y)
# print("y_train",y_train[:5])
# print("y_test",y_test[:5])

# print(x_test[:5])
# print("Normalisation")
# print("\nl1\n", preprocessing.normalize(x_test, norm='l1')[:5])
# print("\nl2\n", preprocessing.normalize(x_test, norm='l2')[:5])
#
# print("\nBinarisation")
# temp = preprocessing.normalize(x_test, norm='l2')[:5]
# print("\nData\n", temp)
# print("\nBinarlisation\n", preprocessing.Binarizer(threshold=0.5).transform(temp))

# mod1 = svm.SVC(kernel="linear")
# mod1.fit(x_train, y_train)
# print(y_test)
# print(mod1.predict(x_test))
# print(mod1.score(x_test, y_test))
# sco = cross_val_score(mod1, x, y, cv=5)
# print(sco)
# print(sco.mean(), sco.std())

# data1 = datasets.load_diabetes(as_frame=True)
# print(data1)
# print(tabulate(data1.data[:10], headers=data1.feature_names, tablefmt="fancy_grid"))
# df = pd.DataFrame(data1.target[:10])
# print(df.to_string())


data1 = pd.read_excel("train.xlsx")
x = np.array(data1[['Pclass', 'Sex', 'Age']], dtype=int)
y = np.array(data1['Survived'])
# print(x.to_string())

xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=0.545)
# print(xtest[:10])
# xtest = preprocessing.normalize(xtest, norm='l1')
# print(xtest[:10])

mod1 = svm.SVC(kernel="linear")
mod1.fit(xtest, ytest)
print("expected output:\n", ytest, "\n")
print("prediction:\n", mod1.predict(xtest), "\n")
print("model score:",mod1.score(xtest, ytest))
sco = cross_val_score(mod1, x, y, cv=5)
print("cross validation score:", sco)
print("cross validation mean:", sco.mean(), "\ncross validation deviation:", sco.std())
