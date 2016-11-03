# 樸素貝葉斯分類器

我們要使用 sklearn 的 `GaussianNB()` 來做文本的作者辨識，詳情請參見 [Udacity](https://classroom.udacity.com/courses/ud120/lessons/2254358555/concepts/30109586140923#)

## Sklearn Example

```python
>>> from sklearn import datasets
>>> iris = datasets.load_iris()
>>> from sklearn.naive_bayes import GaussianNB
>>> gnb = GaussianNB()
>>> y_pred = gnb.fit(iris.data, iris.target).predict(iris.data)
>>> print("Number of mislabeled points out of a total %d points : %d"
...       % (iris.data.shape[0],(iris.target != y_pred).sum()))
Number of mislabeled points out of a total 150 points : 6

```