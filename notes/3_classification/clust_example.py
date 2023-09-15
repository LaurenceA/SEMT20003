
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['text.usetex'] = True

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('filename', type=str)
args = parser.parse_args()


from sklearn import datasets
iris = datasets.load_iris()
X = iris['data'][50:, [0, 2]]
Y = iris['target'][50:]-1

X0 = X[Y==0, :]
X1 = X[Y==1, :]

fig, ax = plt.subplots(figsize=(1.7, 1.7))
ax.set_xlabel("$x_1$")
ax.set_ylabel("$x_2$")
ax.scatter(X0[:, 0], X0[:, 1], c='tab:blue', marker='.', label="Class 0")
ax.scatter(X1[:, 0], X1[:, 1], c='tab:orange', marker='.', label="Class 1")
ax.legend(frameon=False, handletextpad=0.1, fontsize='small', borderpad=0.1, borderaxespad=0.1)

fig.savefig(args.filename, bbox_inches='tight')
