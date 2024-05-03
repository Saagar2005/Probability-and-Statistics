import numpy as np
from scipy.special import erfinv, erf
import matplotlib.pyplot as plt
import seaborn as sns

mu = np.double(input("Enter the mean of the normal distribution you want to sample from:"))
stdDev = np.double(input("Enter the standard deviation of the normal distribution you want to sample from:"))
print("Let [a,b] be the range you want to sample from")
a = np.double(input("Enter the value of a:"))
b = np.double(input("Enter the value of b:"))

a = (a - mu)/stdDev  # Find the values of a and b that correspond to the standard normal distribution
b = (b - mu)/stdDev

CDF_a = 0.5 * ( 1 + erf(a/np.sqrt(2)))  # Value of F(a), that is, the value that the CDF takes at 'a'
CDF_b = 0.5 * ( 1 + erf(b/np.sqrt(2)))  # Value of F(b), that is, the value that the CDF takes at 'b'

samples_from_uniform = np.random.uniform(CDF_a, CDF_b, size=1000000)  # Samples points from U[F(a),F(b)] where U is a uniform distribution

# Create subplots
fig, axs = plt.subplots(1, 2, figsize=(12, 6))

# Plot histogram of samples from uniform distribution
sns.histplot(samples_from_uniform, ax=axs[0])
axs[0].set_xlabel("Sampled value")
axs[0].set_ylabel("Frequency of occurrence")
axs[0].set_title("Histogram of Samples from Uniform distribution")

required_samples = np.sqrt(2) * erfinv(2*samples_from_uniform - 1)  # Use the Inverse CDF method. Note that F^-1 has been written in terms of erfinv (inverse of the error function)

samples_from_normal = required_samples * stdDev + mu   # Scale and shift the sampled points so that they correspond to the actual required normal distribution

# Plot the obtained samples from the required normal distribution
sns.histplot(samples_from_normal, bins=100, kde=True, ax=axs[1])
axs[1].set_xlabel("Sampled value")
axs[1].set_ylabel("Frequency of occurrence")
axs[1].set_title("Histogram of Samples from Normal distribution")

plt.tight_layout()
plt.show()