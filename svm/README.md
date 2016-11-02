# 支持向量機

## 簡介

使用 sklearn 的 SVM.svc() 來做文本的作者辨識，並藉由實驗過來，來認識參數 kernel 與 c 對準確度的影響，想了解更細節的實驗項目，請參見 [Udacity](https://classroom.udacity.com/courses/ud120/lessons/2252188570/concepts/30003287340923#)

## Sklearn Example

```
>>> import numpy as np
>>> X = np.array([[-1, -1], [-2, -1], [1, 1], [2, 1]])
>>> y = np.array([1, 1, 2, 2])
>>> from sklearn.svm import SVC
>>> clf = SVC()
>>> clf.fit(X, y) 
SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0,
decision_function_shape=None, degree=3, gamma='auto', kernel='rbf',
max_iter=-1, probability=False, random_state=None, shrinking=True,
tol=0.001, verbose=False)
>>> print(clf.predict([[-0.8, -1]]))
[1]
```

