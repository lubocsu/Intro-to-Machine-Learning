#encoding=utf-8
#!/usr/bin/python

import matplotlib.pyplot as plt
from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture

features_train, labels_train, features_test, labels_test = makeTerrainData()


### the training data (features_train, labels_train) have both "fast" and "slow"
### points mixed together--separate them so we can give them different colors
### in the scatterplot and identify them visually
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]


#### initial visualization
plt.xlim(0.0, 1.0)
plt.ylim(0.0, 1.0)
plt.scatter(bumpy_fast, grade_fast, color = "b", label="fast")
plt.scatter(grade_slow, bumpy_slow, color = "r", label="slow")
plt.legend()
plt.xlabel("bumpiness")
plt.ylabel("grade")
plt.show()
################################################################################


### your code here!  name your classifier object clf if you want the
### visualization code (prettyPicture) to show you the decision boundary

# 採用 KNN 算法，讓新數據 N 去尋找鄰近的已標籤數據 Ls，選擇 Ls 中重複出現最多次的標籤來作為
# N 的預測結果

from sklearn.metrics import accuracy_score

clf = KNeighborsClassifier(n_neighbors=8) # 採用最鄰近的三個鄰居來進行投票
clf.fit(features_train,labels_train)
print("Accuracy: %f" % accuracy_score(labels_test,clf.predict(features_test)))

# 結果為 0.94400
prettyPicture(clf, features_test, labels_test)
