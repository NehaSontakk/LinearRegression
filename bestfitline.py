import numpy as np

x = np.array([10,9,2,15,10,16,11,16], dtype=np.float64)
y = np.array([95,80,10,50,45,98,38,93], dtype=np.float64)

#slope
def best_fit_slope(x,y):
    s = (((np.mean(x)*np.mean(y)) - np.mean(x*y)) /
         ((np.mean(x)*np.mean(x)) - np.mean(x*x)))
    return s

s = best_fit_slope(x,y)
print(s)

#intercept
def best_fit_intercept(x,y,s):
	i = np.mean(y) - s*np.mean(x)
	return i

i = best_fit_intercept(x,y,s)
print(i)

#regression line
line = [(s*l)+i for l in x]
print(line)

import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')

plt.scatter(x,y,color='red')
plt.plot(x, line)
plt.show()
