from sklearn.datasets import load_digits
from sklearn import svm
from sklearn.model_selection import train_test_split

X, y = load_digits(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42)

# linear SVC
clf1 = svm.SVC(kernel="linear")
clf1.fit(X_train, y_train)
acc1 = clf1.score(X_test, y_test)
print("linear SVC has accuracy: {:.2f}%".format(acc1*100))

# nonlinear SVC
clf2 = svm.SVC(kernel="rbf",gamma="scale")
clf2.fit(X_train, y_train)
acc2 = clf2.score(X_test, y_test)
print("nonlinear SVC has accuracy: {:.2f}%".format(acc2*100))
