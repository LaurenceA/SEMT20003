import math
import numpy as np
import torch as t
import torch.nn as nn
t.manual_seed(0)

import matplotlib.pyplot as plt 
plt.rcParams['text.usetex'] = True

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('filename', type=str)
args = parser.parse_args()

N = 20

xs = t.linspace(-5, 5, 100)[:, None]
X = t.linspace(-4, 4, N)[:, None]
y = t.sin(X) + 0.5*t.randn(N, 1)

plt.scatter(x=X, y=y, label='Data', c='k')
plt.xlabel('$x$')
plt.ylabel('$y$')
#plt.plot(xs, t.sin(xs), label='"True" (noise-free) line', c='r')

input_features = 1 
hidden_features = 100
output_features = 1 

def train(opt, opt_kwargs, col, label, alpha=1, minibatch=False, epochs=3000):
    net = nn.Sequential(
        nn.Linear(input_features, hidden_features),
        nn.ReLU(),
        nn.Linear(hidden_features, hidden_features),
        nn.ReLU(),
        nn.Linear(hidden_features, output_features)
    )
    opt = opt(net.parameters(), **opt_kwargs)

    if minibatch:
        for _ in range(epochs):
            for i in np.random.permutation(N):
                L = ((net(X[i, :]) - y[i, :])**2).mean()
                L.backward()
                opt.step()
                opt.zero_grad()
    else:
        for _ in range(epochs):
            L = ((net(X) - y)**2).mean()
            L.backward()
            opt.step()
            opt.zero_grad()

    plt.plot(xs, net(xs).detach(), c=col, label=label, alpha=alpha)

train(t.optim.SGD, {'lr': 0.01, 'momentum':0.8}, 'tab:blue', 'Full batch, lr=0.01, mom=0.8', minibatch=False)
train(t.optim.SGD, {'lr': 0.01/N, 'momentum':0.8}, 'tab:purple', 'Minibatch, lr={0.01/N}, mom=0.8', minibatch=True)

#20 epochs updates, but with 100 times less 


plt.legend()
plt.savefig(args.filename, bbox_inches='tight')
