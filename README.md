# LinearRegression

###### refer to Linear_reg_scratch.py 

Files bestfitline.py, Figure-1.png, output.txt are to find optimum equation for best fit line for a few given points.

## Algorithm 

I've generated some dummy data values to test our procedure but with a few small modifications it will work on any dataset.

The procedure is extremely simple:
1.  Find the mean values of x (independent variable) and y (dependent variable)
2.  Using these values find the standard deviation and variance 
3.  Find covariance of x and y
4.  Then find the correlation between these (this tells us whether x and y are strongly/weakly related)
5.  Now we calculate the coefficients in the line equation
6.  Predict new values of y (I've done it for the same dataset)
7.  Check the error between new y and old y values (using root mean squared error measure)
