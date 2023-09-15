import numpy as np
import matplotlib.pyplot as plt
import torch as t
plt.rcParams['text.usetex'] = True

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('filename', type=str)
args = parser.parse_args()

def fit_Wh(X, Y):
    return t.inverse(X.T @ X) @ X.T @ Y

N     = 100 # number of datapoints
D     = 1   # dimension of datapoints
sigma = 0.5 # output noise
X     = t.randn(N, D)
qtrue = 2  # quadratic term
ltrue = -1 # linear term
btrue = 1  # bias
Y     = qtrue*X**2 + ltrue*X + btrue + sigma*t.randn(N, 1)

def quad(X):
    return t.cat([X**2, X, t.ones(X.shape[0], 1)], 1)

Xe = quad(X)

Wh = fit_Wh(Xe, Y)

fig, ax = plt.subplots(figsize=(1.7,1.7), sharey=True)
ax.set_xlabel("$x$")
ax.set_ylabel("$y$")

ax.scatter(X, Y, marker='.', label="datapoints")

xs = t.linspace(-4, 4, 100)[:, None]
ax.plot(xs, quad(xs)@Wh, 'r', label="$\hat{y}$")
ax.legend(fontsize=6);

fig.savefig(args.filename, bbox_inches='tight')
