#!/usr/bin/python

"""
    This is the code to accompany the Lesson 1 (Naive Bayes) mini-project.

    Use a Naive Bayes Classifier to identify emails by their authors

    authors and labels:
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
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

def getGaussianBayesClassifer(train,label):
    clf = GaussianNB()
    t0 = time()
    clf.fit(train,label)
    print "training time:", round(time()-t0, 3), "s"
    return clf

clf = getGaussianBayesClassifer(features_train, labels_train)
result = clf.predict(features_test)
score = accuracy_score(labels_test,result)
print("The score is %f" % score)

# Here is my result @zake7749
# training time: 2.881 s
# The score is 0.973265

#########################################################
