import numpy as np
np.random.seed(0)
import matplotlib.pyplot as plt
plt.rcParams['text.usetex'] = True

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('filename', type=str)
args = parser.parse_args()

N = 20
xs = np.linspace(-3, 3, 100)

fig, axs = plt.subplots(figsize=(1.7,1.7))
axs.set_title("$\hat{y}_{\\rm quad}(x) = w_1 + w_2 x + w_3 x^2$")

axs.set_xlabel('$x$')
axs.set_xlabel('$y$')

w0s = np.random.randn(N)
w1s = np.random.randn(N)
w2s = np.random.randn(N)

for i in range(N):
    axs.plot(xs, w0s[i] + w1s[i]*xs + w2s[i]*(xs**2))

fig.savefig(args.filename, bbox_inches='tight')
