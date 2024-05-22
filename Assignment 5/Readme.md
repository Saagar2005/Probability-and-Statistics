
### Bayesian Analysis

Consider that you have a certain prior belief about a coin that is in your possession, that its bias is distributed as:\
Case 1) Beta(2,5)\
Case 2) Beta(5,2)\
Case 3) Beta(1,1)\
Case 4) Beta(2,2)\
Now, tossing the coin 10 times results in the following outcome: [H, H, H, T, T, T, H, H, H, T]\
Plot the posterior distribution based on the above observation corresponding to each of the priors. Draw lines for the MLE and MAP estimates on the plots.


# Instructions to run the code:

1. Extract the files from the zip file.
2. Open terminal in the unzipped folder, i.e., the folder containg the python file (CS203assignment_5.py).
3. Make sure you have the following python libraries installed on your system: numpy, matplotlib, scipy, ipywidgets and IPython.
3. Write the following command on terminal -
```	
 python3 CS203assignment_5.py
```
4. The code will show the posterior probability density plots for all four cases of prior beliefs (beta). The plots also have MLE and MAP estimates shown on each of them.
5. Additionally, the fifth plot is shown which can be used to observe changes in the posterior beliefs as our priors change. It has a slider for a and b, which can be adjusted (or typed in the provided boxes) and the corresponding change will be reflected in the plot. 

### Team members 
Dhruv Gupta (220361)\
Pragati Agrawal (220779)\
Saagar KV (220927)\
Kundan Kumar (220568)\
Akula Venkatesh (220109)
