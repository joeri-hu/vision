import matplotlib.pyplot as plt
from sklearn import svm
from sklearn import datasets
from sklearn.model_selection import train_test_split

digits = datasets.load_digits(return_X_y=True)
data_train, data_test, target_train, target_test \
    = train_test_split(*digits, test_size=1/3)

clf = svm.SVC(gamma=0.001, C=100)
clf.fit(data_train, target_train)
acc = clf.score(data_test, target_test)

print(acc)
