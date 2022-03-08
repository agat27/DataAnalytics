from cmdstanpy import CmdStanModel
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from textwrap import wrap
import os

# direct path to directory with csv and stan files
direct_path = os.path.dirname(__file__)

# Create a dataset (as a dictionary): F=5 L=9
bern_data = {
    "N": 14,
    "y": [1,1,0,1,0,1,1,0,1,1,0,1,1,0,]
}

# Create a cmdstanpy model from bern_1.stan code provided.
model = CmdStanModel(stan_file=os.path.join(direct_path, 'bern_1.stan'))
print(model)

# Sample from the model using the dataset and .sample() method
fit = model.sample(data=bern_data, output_dir='out')

# Extract $\theta$ variable
theta = fit.stan_variable('theta')

# Using .summary() method get mean (green), median (yellow) and 5% (red) and 95% (black) quantiles of theta,
# and mark them on the histogram.
df = fit.summary()
df_theta = df.loc['theta']
p5 = df_theta['5%']
p95 = df_theta['95%']
mediana = df_theta['50%']
mean_theta = theta.mean()

plt.hist(theta, bins=50, density=True)
plt.axvline(mean_theta, color='g', linewidth=2, linestyle='solid')
plt.axvline(mediana, color='y', linewidth=2, linestyle='solid')
plt.axvline(p5, color='r', linewidth=2, linestyle='solid')
plt.axvline(p95, color='k', linewidth=2, linestyle='solid')
plt.suptitle('\n'.join(wrap("Histogram of theta with mean (green), median (yellow) and 5% (red) and 95% (black) quantiles of theta marked", 65)))
plt.show()