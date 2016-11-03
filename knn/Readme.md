# K-最近鄰居分類

這堂課中要從：

* KNN
* adaboost
* 隨機森林

裡選擇一個自己喜歡的分類器，並認識它背後的運作原理與參數調整，我採用的是 KNN。這次的任務跟以往不太一樣，資料集是地面的坡度與顛頗程度，標籤是自動車應該加速或減速，我們要透過讓分類器去學習決策面，讓自動車在遇到新的狀況時也能知道該不該加速。

## 實驗結果

鄰居數設定為 8，精度為 0.94
![result](http://i.imgur.com/WiBODgE.png)

## Sklearn Example

```python
>>> X = [[0], [1], [2], [3]]
>>> y = [0, 0, 1, 1]
>>> from sklearn.neighbors import KNeighborsClassifier
>>> neigh = KNeighborsClassifier(n_neighbors=3)
>>> neigh.fit(X, y)
KNeighborsClassifier(...)
>>> print(neigh.predict([[1.1]]))
[0]
>>> print(neigh.predict_proba([[0.9]]))
[[ 0.66666667  0.33333333]]
```
