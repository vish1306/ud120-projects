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
features_train, features_test, labels_train, labels_test = preprocess(test_size=0.3)
from email_preprocess import accuracy_score
clf=preprocess()
clf.fit(features_train,label_train)
pred=clf.predict(features_test)
print accuracy_score(pred,label_test)





#########################################################
### your code goes here ###


#########################################################


