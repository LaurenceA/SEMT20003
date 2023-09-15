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
D     = 2   # dimension of datapoints
sigma = 0.3 # output noise
X     = t.randn(N, D)
Wtrue = t.ones(D, 1)
Y     = X @ Wtrue + sigma*t.randn(N, 1)

Wh = fit_Wh(X, Y)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlabel("$x_1$")
ax.set_ylabel("$x_2$")
ax.set_zlabel("$y$")
ax.scatter(X[:, 0], X[:, 1], Y[:, 0])

Xp = t.tensor([
    [-4., -4.],
    [-4.,  4.],
    [ 4., -4.],
    [ 4.,  4.]
])

ax.plot_trisurf(
    np.array(Xp[:, 0]), 
    np.array(Xp[:, 1]), 
    np.array((Xp @ Wh)[:, 0]), 
    color='r', 
    alpha=0.3
)

fig.savefig(args.filename, bbox_inches='tight')
