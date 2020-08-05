import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt


# True values: Vm = 20, Km = 15
# Declare the experimental data242424
x = np.array([0, 10, 20, 50, 100, 200, 300])
y = np.array([0, 9, 10, 17, 18, 20, 19])
# Define the model
def myModel(x, p):
    return p[0]*x/(p[1]+x)
# Define the objective function
def residuals (p):
    return y - myModel (x, p)
# Fit the model to the data
output = optimize.leastsq (residuals, [10, 10])
Vmax,Km = 20,15
yTrue = Vmax*x/(Km+x)
plt.figure(figsize=(10,6))
plt.plot(x, myModel (x, output[0]), '--', x, y, 'o', x, yTrue, 'b', markersize=10)
plt.title('Least-squares fit to noisy data')
# loc=10 means center the legend
plt.legend(['Fitted Curve', 'Noisy Data'], loc=10)
plt.show()
plt.plot(x, residuals(output[0]), 'r^', markersize=10)
plt.show()



