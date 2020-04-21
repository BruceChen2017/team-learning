from sklearn.datasets import load_boston
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import numpy as np
import matplotlib.pyplot as plt

boston = load_boston()
# description of dataset
print(boston.DESCR)
labels = np.append(["intercept"], boston.feature_names)
print(labels)

P = 13
X = boston.data[:,:P]
print("(n_samples, p_features):", X.shape)
y = boston.target
X_train, X_test, y_train, y_test = train_test_split(
     X, y, test_size=0.2, random_state=42)

# train
reg = LinearRegression()
reg.fit(X_train, y_train) 
# internally
# by default, center X and y first
# fit both centered X and y by `np.linalg.lstsq`
# this will not change estimated coefs with original X,y but intercept
# intercept would still be calculated by usual way: y_mean - beta * x_mean

# estimated coef including intercept
coefs = np.append(reg.intercept_, reg.coef_)
design_matrix = np.hstack([np.ones(len(y_train)).reshape(-1,1), X_train])
coefs2 = np.linalg.inv(design_matrix.T @ design_matrix) @ (design_matrix.T) @ y_train
assert np.allclose(coefs, coefs2)
COL_LEN = 10
col_name = ""
coef_vals = ""
for lab in labels[:len(coefs)]:
     col_name += ("{:>" + str(COL_LEN) + "}|").format(lab)
for co in coefs:
     coef_vals += ("{:>" + str(COL_LEN) + ".5f}|").format(co)
print("estimated coefs:")
print(col_name)
print(coef_vals)
# train data MSE
train_mse = reg._residues / len(y_train)
print("train MSE:", train_mse)

# test
y_test_pred = reg.predict(X_test)
test_mse = mean_squared_error(y_test, y_test_pred)
print("test MSE:", test_mse)

# Visualization for simple regression
N = 10
x1 = boston.data[:N,:1]
y1 = boston.target[:N]
reg2 = LinearRegression()
reg2.fit(x1, y1)
y1_pred = reg2.predict(x1)
# plot
plt.scatter(x1, y1,  color='black')
plt.plot(x1, y1_pred, color='blue', linewidth=3)
plt.xticks(())
plt.yticks(())
plt.show()
