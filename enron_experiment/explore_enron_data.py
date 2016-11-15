#encoding=utf-8
#!/usr/bin/python


"""
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000

"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

"""
Quiz 1
"""
print("數據集中一共有 %d 個人的資料" % len(enron_data))
#146

"""
Quiz 2
"""
vs = enron_data.values()
print("每個人共有 %d 個特徵可以使用" % len(vs[0]))
#21

"""
Quiz 3
"""
poi_num = 0
for p in vs:
    if p["poi"] == 1:
        poi_num += 1
print("在安然數據集的嫌疑人一共有 %d 個" % poi_num)
#18
"""
Quiz 4
"""

poi_all = open("../final_project/poi_names.txt",'r')
poi_all_num = 0

# 資料格式
# (y/n) Name
for line in poi_all:
    poi_all_num += 1
poi_all_num -= 2 # 去除描述列
print("但是在我們自己準備的資料集裡，一共有 %d 個嫌疑人" % poi_all_num)
print("也就是我們準備的資料集，與安然資料集並不一致")

"""
Quiz 5
James Prentice 名下的股票总值是多少？
"""

#請注意一下，格式是LASTNAME FIRSTNAME MIDDLENAME
#所以會找的是 Prentice James
print("James Prentice 名下股票總值: %d" % enron_data["PRENTICE JAMES"]["total_stock_value"])
#1095040

"""
Quiz 6
我们有多少来自 Wesley Colwell 发给嫌疑人的电子邮件？
"""
print("有 %d 封 Wesley Colwell 發給嫌疑人的郵件" % enron_data["COLWELL WESLEY"]["from_this_person_to_poi"])
#11

"""
Quiz 7
Jeffrey Skilling 行使的股票期权价值是多少？
"""
print("Jeff Skilling's exercised stock options: %d" % enron_data["SKILLING JEFFREY K"]["exercised_stock_options"])

"""
Quiz 8
此数据集中有多少雇员有量化的工资？已知的邮箱地址是否可用？
"""
ava_email_num  = 0
ava_salary_num = 0
nava_total_payments_num = 0.
nava_total_payments_poi_num = 0.

for v in vs:
    if v["email_address"] != "NaN":
        ava_email_num += 1
    if v["salary"] != "NaN":
        ava_salary_num += 1
    if v["total_payments"] == "NaN":
        nava_total_payments_num += 1
        if v["poi"]:
            nava_total_payments_poi_num += 1

print("有效郵件計數共有: %d" %ava_email_num)
#111

print("有效薪水計數共有: %d" %ava_salary_num)
#95

"""
Quiz 9
（当前的）E+F 数据集中有多少人的薪酬总额被设置了“NaN”？数据集中这些人的比例占多少？
"""
print("數據集中total_payments被設為NaN的比例為:%f" % (nava_total_payments_num/float(len(vs))))
#0.14 (14%)
print("數據集中total_payments被設為NaN且為Poi的比例為:%f" % (nava_total_payments_poi_num/float(len(vs))))
#ITS ZERO !
