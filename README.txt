Instructions to run the code:

1. Extract the files from the zip file.
2. Open terminal in the unzipped folder, that is, the folder containing the python file (cs203assignment_4.py).
3. Make sure you have numpy, matplotlib, seaborn and scipy installed.
4. Write the following command on terminal -
	python3 cs203assignment_4.py
5. Enter the mean and standard deviation of the normal distribution you want to sample from. Also, enter the range of values you want to sample from.
6. The output presented shows the uniform distribution used as well as the required normal distribution generated from the uniform distribution using the inverse CDF (Cumulative Distribution Function) method.

Description of the Inverse CDF method implemented:

We have expressed the CDF for the standard normal distribution in terms of the error function. Further, the inverse of the CDF of the standard normal distribution is expressed in terms of the inverse error function.

In the discussion that follows, F(x) denotes the CDF for the standard normal distribution and Finv(x) denotes its inverse; erf(x) denotes the error function and erfinv(x) denotes its inverse.

The relations are as follows: 

1) F(x) = 0.5 * (1 + erf(x))
2) Finv(x) = sqrt(2) * erfinv(2*x -1) where sqrt(2) is the square root of 2.

These relations directly follow from the definitions of the error function and the CDF of the standard normal distribution.

Steps followed in the code:

1) We first shift and scale 'a' and 'b' to find the values that correspond to the standard normal distribution. This is done by subtracting the mean of the required normal distribution from 'a' and 'b' and then dividing by the standard deviation of the required normal distribution.
2) We now sample points uniformly in the range [F(a), F(b)]. F(a) and F(b) are found using relation (1) above.
3) For each sampled point y, we find Finv(y) using relation(2) above. These points Finv(y) belong to a standard normal distribution, as expected.
4) We shift and scale the points Finv(y) so that they now correspond to the required normal distribution. This is done by multiplying each point Finv(y) by the standard deviation of the required normal distribution and then adding the mean of the required normal distribution to the obtained product.

Team members - Dhruv Gupta (220361), Pragati Agrawal (220779), Saagar K V (220927), Kundan Kumar (220568), Akula Venkatesh (220109)