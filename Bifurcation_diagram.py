import numpy as np
import matplotlib.pyplot as plt

#The main idea behind this code is that we
#essentially want to plot the same sort of
#histograms we've been making in question 4 iv - viii
#but for many values of r, and put them all on the 
#same graph. To do this, we'll make a scatter plot
#with a range of r values as the x-axis, and the 
#different values of x as the y-axis. We'll go through
#the same process as we did with the previous questions, but now
#when we have an x-value, instead of placing it in a
#histogram bin, we place it at a coordinate whose x-component
#is the r-value being evaluted at the time, 
#and whose y-component is the given x-value. Such that
#we can get a sense of which x-values have a greater number
#for a given r (i.e. the histogram bar height), we'll also make the
#scatter plot points fairly transparent so that the density of points
#within a given region is apparent  

#Here we set up our parameters
x0 = 0.01
r = np.arange(2.4,4,0.001) #the range of r values we want to evaluate
n = np.arange(0,999,1)#This will act as our index
R = [] #the purpose of these empty lists will become apparent soon
X = []
#Since we want to do the same process with every r, we make a for loop
for i in r:
    #These lists and the seed must be reset when switching r values 
    xT = [] 
    rT = []
    x = x0
    for j in n:
        #When updating the x-value, not only do we save the x-value
        #in list, but also the r-value being evaluted at the time.
        #The reason for this is because we want to create a point
        #in the form of [r-value,x-value]
        xT.append(x)
        rT.append(i)
        x = i*x*(1-x)
    #Slicing the first 100 points, we then save xT and rT into bigger lists
    #that will eventually contain all the r values 900 times over, and the
    #corresponding x values
    R.append(rT[100:])
    X.append(xT[100:])
#The usually prettiness
plt.xlim(2.4,4)
plt.ylim(0,1)
plt.xlabel("$r$")
plt.ylabel("$x$")
plt.title("Physics 2110B: Assignment #3 Question 4x): Bifurcation Diagram")
#The important part of the scatter plot settings is that the size
#of the points are small (this corresponds to "s") since there will be
#around a lot of points, and the transparency of the points is fairly high
#(this corresponds to the alpha parameter which is set pretty low)
plt.scatter(R,X, s=5, c = "black", alpha = 0.02 )
plt.show()    
    
