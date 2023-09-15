import numpy as np
np.random.seed(0)
import matplotlib.pyplot as plt
plt.rcParams['text.usetex'] = True

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('filename', type=str)
args = parser.parse_args()

N = 20
xs = np.array([-1, 1])

fig, axs = plt.subplots(ncols=3, figsize=(4*1.7,1.7), sharey=True)
axs[0].set_title("$\hat{y}_{\\rm const}(x) = w_1$")
axs[1].set_title("$\hat{y}_{\\rm slope}(x) = w_2 x$")
axs[2].set_title("$\hat{y}_{\\rm straight}(x) = w_1 + w_2 x$")

axs[0].set_xlabel('$x$')
axs[1].set_xlabel('$x$')
axs[2].set_xlabel('$x$')

w0s = np.random.randn(N)
w1s = np.random.randn(N)

for i in range(N):
    axs[0].plot(xs, np.ones(2)*w0s[i])
    axs[1].plot(xs, w1s[i]*xs)
    axs[2].plot(xs, w0s[i] + w1s[i]*xs)



fig.savefig(args.filename, bbox_inches='tight')
