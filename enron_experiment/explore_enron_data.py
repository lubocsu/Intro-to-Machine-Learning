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
print("嫌疑人一共有 %d 個" % poi_num)
