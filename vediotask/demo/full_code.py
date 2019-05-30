from __future__ import print_function
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

## sklearn.cross_validation 逐渐废弃了，需要从sklean.model_selection import

iris = load_iris()
X = iris.data
y = iris.target
#print(X,y)

# 特征工程
# degree=2 特征两两组和
ploy = PolynomialFeatures(2)
X_ploy =  ploy.fit_transform(X)  ##打印
#print(X_ploy)

#特征工程之后的数据集进行训练
#X_train,X_test,y_train,y_test = train_test_split(X_ploy,y,random_state=4)

#原始数据集训练（模型训练），最近邻
X_train,X_test,y_train,y_test = train_test_split(X,y,random_state=4)
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train,y_train)

#预测得分
y_pred = knn.predict(X_test)
print("预测值")
print(y_pred)
print("真实值")
print(y_test)
print(knn.score(X_test,y_test))

##交叉验证
from sklearn.model_selection import cross_val_score
knn = KNeighborsClassifier(n_neighbors=5)
scores = cross_val_score(knn,X,y,cv=5,scoring='accuracy')  ##cv=5 做了5次交叉验证
print(scores)

#参数训练（参数查找），通过多做实验的方式选择参数，参数搜索
k_range = range(1,31)
k_score = []
for k in k_range:
    knn = KNeighborsClassifier(n_neighbors=k)
    scores = cross_val_score(knn,X,y,cv=10,scoring='accuracy')
    k_score.append(scores.mean())
plt.plot(k_range,k_score)
plt.xlabel('Value of k for knn')
plt.ylabel('cross-validated accuracy')
plt.show()

