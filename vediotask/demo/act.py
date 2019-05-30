from __future__ import print_function
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import cross_val_score
import matplotlib.pyplot as plt

#加载数据
iris = load_iris()
X = iris.data
y = iris.target

#特征选取
ploy = PolynomialFeatures(3)
#模型训练
X_ploy =  ploy.fit_transform(X)


#交叉校验，查找最优的参数
k_range = range(1,10)
k_score = []
for k in k_range:
    knn = KNeighborsClassifier(n_neighbors=k)
    scores = cross_val_score(knn,X_ploy,y,cv=10,scoring='accuracy')
    k_score.append(scores.mean())
    print(scores)
    print(k)
    print('-----------')
plt.plot(k_range,k_score)
plt.xlabel('Value of k for knn')
plt.ylabel('cross-validated accuracy')
plt.show()

#最优参数是5，进行模型保存
import pickle
knn = KNeighborsClassifier(n_neighbors=5)
#保存模型
#with open('../resource/atc.pickle','wb') as f:
#    pickle.dump(knn,f)
#预测模型
with open('../resource/atc.pickle','rb')  as f:
    clf2 = pickle.load(f)
    print(clf2.predict(X[0:1]))
