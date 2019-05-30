from __future__ import print_function
from sklearn import svm
from sklearn import datasets

import warnings

warnings.filterwarnings("ignore", category=FutureWarning, module="sklearn", lineno=196)

clf = svm.SVC()
iris = datasets.load_iris()
X,y = iris.data,iris.target
#print(X)
#print(y)
clf.fit(X,y)  ##构造出了模型，拟合了数据，并且训练出来分类器


#pickle 保存模型
import pickle
print('保存模型')
#save    保存模型
with open('../resource/clf2.pickle','wb') as f:
    pickle.dump(clf,f)
print('结束保存')

print('打开模型')
#restore 打开模型
with open('../resource/clf2.pickle','rb')  as f:
    clf2 = pickle.load(f)
    print(clf2.predict(X[0:1]))
print(X[0:1])
print('预测结束')

#joblib
from sklearn.externals import joblib
#save
joblib.dump(clf,'../resource/clf2.pickle')
#restore
clt3 = joblib.load('../resource/clf2.pickle')
print(clt3.predict(X[0:1]))
