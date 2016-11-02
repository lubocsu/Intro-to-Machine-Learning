#encoding:utf-8
#!/usr/bin/python


"""
    This is the code to accompany the Lesson 3 (decision tree) mini-project.

    Use a Decision Tree to identify emails from the Enron corpus by author:
    Sara has label 0
    Chris has label 1
"""

import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###
from sklearn import tree
from sklearn.metrics import accuracy_score

"""
構建一個決策樹運行的分類器，設置 `min_samples_split`=40。
開始訓練之前，這可能需要一些時間。我們的問題是，這個決策樹的精確度是多少？
"""

def getDecisonTreeClassifier(train_feature,train_label):
    clf = tree.DecisionTreeClassifier(min_samples_split=40)

    t0 = time()
    clf.fit(train_feature,train_label)
    print "training time:", round(time()-t0, 3), "s"

    return clf

def Problem1():
    clf = getDecisonTreeClassifier(features_train,labels_train)
    predict = clf.predict(features_test)
    print('Accuracy: %f' % accuracy_score(labels_test,predict))

# Problem1()
# Here is my result @zake7749
# training time: 123.366 s
# Accuracy: 0.978385

"""
你从 SVM 迷你项目中了解到，参数调整可以显著加快机器学习算法的训练时间。
一般情况下，参数可以调整算法的复杂度，越复杂的算法通常运行起来越慢。

控制算法复杂度的另一种方法是通过你在训练/测试时用到的特征数量。
算法可用的特征数越多，越有可能发生复杂拟合。
我们将在“特征选择”这节课中详细探讨，但你现在可以提前有所了解。

你数据中的特征数是多少？

（提示：数据被整理成一个 numpy 数组后，行数是数据点数，列数是特征数；要提取这个数字，只需运行代码 len(features_train[0])。）
"""

def Problem2():
    print("特徵數目為: %d" % features_train.shape[1])

# Problem2()
# Here is my result @zake7749:
# 特徵數目: 3785
#########################################################

"""
进入 ../tools/email_preprocess.py，然后找到类似此处所示的一行代码：
selector = SelectPercentile(f_classif, percentile=10)

将百分位数从 10 改为 1，然后运行 dt_author_id.py

现在，特征数是多少？
"""

# 請參照說明修改百分位數
# Problem2()
# Here is my result @zake7749:
# 特徵數目 379，也就是說我們的特徵數從訓練文本的 10% -> 1%
# 此外，特徵數目越多，會使得我們的決策數越複雜 (Problem4)

"""
當我們只使用 1% 的特徵用作訓練時，準確度又會是多少呢？
"""
# Problem1()
# Here is my result @zake7749:
# training time: 6.185 s
# Accuracy: 0.966439
# 這與 SVM 中的實驗結果相當類似
