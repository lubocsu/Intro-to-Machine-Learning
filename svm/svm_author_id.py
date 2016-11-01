#!/usr/bin/python

"""
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:
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
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

def getSupportVectorClassifier(train, label, kernel="linear", C=1.0):

    clf = SVC(kernel=kernel,C=C)
    t0 = time()
    clf.fit(train, label)
    print "training time:", round(time()-t0, 3), "s"
    return clf

"""
 Problem 1 : Use the whole train_set to train the classifier.
"""
def Problem1():
    svc = getSupportVectorClassifier(features_train,labels_train)
    result = svc.predict(features_test)
    score = accuracy_score(labels_test, result)
    print("Accuracy: %f" % score)

#Problem1()

# Here is my result @zake7749
# training time: 217.808 s
# Accuracy: 0.984073

"""
 Problem 2 : Use the 1 percent data in train_set to train the classifier
"""
def Problem2():
    svc = getSupportVectorClassifier(features_train[:len(features_train)/100],
                                     labels_train[:len(labels_train)/100])
    result = svc.predict(features_test)
    score = accuracy_score(labels_test, result)
    print("Accuracy: %f" % score)

#Problem2()

# Here is my result @zake7749
# training time: 0.111 s
# Accuracy: 0.884528

#########################################################

"""
 Problem 3 : Change the kernel of svm to 'rbf'. we still use 1% of our datasets.
"""

def Problem3():
    svc = getSupportVectorClassifier(features_train[:len(features_train)/100],
                                     labels_train[:len(features_train)/100],
                                     kernel='rbf')

    result = svc.predict(features_test)
    score = accuracy_score(labels_test, result)
    print("Accuracy: %f" % score)

# Problem3()

# Here is my result @zake7749
# training time: 0.129 s
# Accuracy: 0.616041

"""
 Problem 4 : Change the the parameter C of svm in problem 3 to get a better accuracy.
"""

def Problem4():
    svc = getSupportVectorClassifier(features_train[:len(features_train)/100],
                                     labels_train[:len(features_train)/100],
                                     kernel='rbf',
                                     C = 10000)
    result = svc.predict(features_test)
    score = accuracy_score(labels_test, result)
    print("Accuracy: %f" % score)

# Problem4()

# When C = 10 -> Accuracy is 0.616041
# When C = 100 -> Accuracy is 0.616041
# When C = 1000 -> Accuracy is 0.821388
# When C = 10000 -> Accuracy is 0.892491
# We get a better accuracy for a higher C.

"""
 Problem 5 : It's the same as problem4, but we use the whole training dataset.
"""

def Problem5():
    svc = getSupportVectorClassifier(features_train,
                                     labels_train,
                                     kernel='rbf',
                                     C = 10000)
    result = svc.predict(features_test)
    score = accuracy_score(labels_test, result)
    print("Accuracy: %f" % score)

#Problem5()

# Here is my result @zake7749
# training time: 120.729 s
# Accuracy: 0.990899

"""
  Problem 6 : predict the label of 10th,26th,50th element in the testdataset.

  ** Notice ** (10,26,50) is an INDEX.
"""

def Problem6():
    svc = getSupportVectorClassifier(features_train[:len(features_train)/100],
                                     labels_train[:len(features_train)/100],
                                     kernel='rbf',
                                     C = 10000)
    print(svc.predict(features_test[10]))
    print(svc.predict(features_test[26]))
    print(svc.predict(features_test[50]))

#Problem6()
# Here is my result @zake7749
# It should be 1,0,1

"""
  Problem 7 : Use the whole dataset for training and to predict that how many
  email is written by Chris(label 1) in testset.

  ** Notice ** (10,26,50) is an INDEX.
"""

def Problem7():
    svc = getSupportVectorClassifier(features_train,labels_train,kernel='rbf',C = 10000)
    result = svc.predict(features_test)

    num = 0
    for label in result:
        if label == 1:
            num += 1
    print(num)

# Problem7()
# Here is my result @zake7749
# num = 877
