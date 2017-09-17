import numpy as np
import matplotlib.pyplot as plt
nObjects = 50
nVariables = 100
# Generate matrix with standard normal random variables
mu = 0.0
sigma = 1.0
x = np.random.normal(mu, sigma, (nVariables,
nObjects))
# Compute correlations between variables
correlations = np.corrcoef(x)
dummy = np.triu(correlations, 1);
corrvector = dummy[dummy != 0];
# Plot the histogram
plt.hist(
corrvector, 20)
plt.show()